import os
import dlib
import cv2
import numpy as np
import urllib.request
import bz2
import streamlit as st

class FaceFeatureExtractor:
    """人脸特征提取器"""
    def __init__(self,model_dir="models"):
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)
        
        self.detector = dlib.get_frontal_face_detector()
        predictor_path = os.path.join(model_dir, "shape_predictor_68_face_landmarks.dat")
        if not os.path.exists(predictor_path):
            self._download_predictor_model(predictor_path)
        
        self.predictor = dlib.shape_predictor(predictor_path)
        recognition_model_path = os.path.join(model_dir, "dlib_face_recognition_resnet_model_v1.dat")
        if not os.path.exists(recognition_model_path):
            self._download_recognition_model(recognition_model_path)
        
        self.face_recognition_model = dlib.face_recognition_model_v1(recognition_model_path)
    
    def _download_predictor_model(self, save_path):
        url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
        compressed_path = save_path + ".bz2"

        if st:
            st.info(f"下载预测器模型...")
        else:
            print("下载预测器模型...")
        
        urllib.request.urlretrieve(url, compressed_path)
        with bz2.BZ2File(compressed_path) as fr, open(save_path,'wb') as fw:
            fw.write(fr.read())
        
        os.remove(compressed_path)

    def extract_features(self, image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image
        
        face = self.detector(gray)
        if len(face) == 0:
            return None
        landmarks = self.predictor(gray, face[0])
        geometric_features = self._extract_geometric_features(landmarks)
        face_descriptor = self._extract_deep_features(image, landmarks)
        return geometric_features, face_descriptor
    
    def _extract_geometric_features(self, landmarks):
        points = np.array([[landmarks.part(i).x, landmarks.part(i).y]for i in range(68)])

        features = {}
        
        left_eye = points[36:42]
        right_eye = points[42:48]
        features['eye_distance'] = np.linalg.norm(np.mean(left_eye, axis = 0) - np.mean(right_eye, axis = 0))
        features['left_eye_width'] = np.linalg.norm(left_eye[0] - left_eye[3])
        features['right_eye_width'] = np.linalg.norm(right_eye[0] - right_eye[3])

        nose_bridge = points[27:31]
        nose_tip = points[31:36]
        features['nose_width'] = np.linalg.norm(nose_tip[0] - nose_tip[4])
        features['nose_height'] = np.linalg.norm(nose_bridge[0] - nose_tip[2])

        mouth = points[48:60]
        features['mouth_width'] = np.linalg.norm(mouth[0] - mouth[6])
        features['mouth_height'] = np.linalg.norm(mouth[2] - mouth[10])

        jawline = points[0:17]
        face_width = np.linalg.norm(jawline[0] - jawline[16])
        face_height = np.linalg.norm(points[8] - points[27])
        features['face_ratio'] = face_width / face_height

        return np.array(list(features.values()))
    
    def _extract_deep_features(self, image, landmarks):
        aligned_face = dlib.get_face_chip(image, landmarks)

        descriptor = self.face_recognition_model.compute_face_descriptor(aligned_face)
        return np.array(descriptor)
    
    def extract_dataset_features(self, data_loader, sample_df):
        geometric_features = []
        deep_features = []
        valid_ids = []

        if st:
            progress_bar = st.progress(0)
            status_text = st.empty()
        
        for i,(idx, row) in enumerate(sample_df.iterrows()):
            try:
                image = data_loader.get_image(row['image_id'])
                features = self.extract_features(image)
                if features:
                    geo, deep = features
                    geometric_features.append(geo)
                    deep_features.append(deep)
                    valid_ids.append(idx)
            except Exception as e:
                print(f"处理图像 {row['image_id']} 时出错: {e}")

            if st:
                progress_bar.empty()
                status_text.empty()

            geometric_features = np.array(geometric_features)
            deep_features = np.array(deep_features)    

            from sklearn.decomposition import PCA
            pca = PCA(n_components=16)
            reduced_deep_features = pca.fit_transform(deep_features)


            all_features = np.hstack((geometric_features, reduced_deep_features))

            valid_df = data_loader.attr_df.loc[valid_ids, data_loader.selected_attrs]

            return all_features, valid_df, geometric_features, deep_features