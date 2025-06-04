import os 
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import load_model
import streamlit as st

class AgeProgressionModel:
    def __init__(self, model_path = None, model_dir = 'models'):
        if model_path:
            model_path = os.path.join(model_dir, "age_progression_model.h5")
        
        self.model_path = model_path
        self.model = None

        if os.path.exists(model_path):
            try:
                self.model = load_model(model_path)
            except Exception as e:
                if st:
                    st.warning(f'加载模型时出错: {e}')
                else:
                    print(f'加载模型时出错: {e}')
        else:
            if st:
                st.warning(f'年龄转换模型未找到，跨年龄生成功能不可用')
            else:
                print(f'年龄转换模型未找到，跨年龄生成功能不可用')
    
    def generate_age_progression(self, image, target_ages = [20, 40, 60, 80]):
        if self.model is None:
           return []
        if image.shape[0] != 256 or image.shape[1] != 256:
            image_resized = cv2.resize(image, (256,256))
        else:
            image_resized = image
        
        image_normalized = (image_resized.astype(np.float32) / 127.5) - 1.0

        generated_images = []
        for age in target_ages:
            age_label = np.array([age / 100.0])
            input_data = [np.expand_dims(image_normalized, 0),
                          np.expand_dims(age_label, 0)]
            generated = self.model.predict(input_data)[0]
            generated = ((generated  + 1) * 127.5).astype(np.uint8)
            generated_images.append(generated)
        
        return generated_images
    
    def visualize_age_progression(self, original_image, generated_images, target_ages):
        fig, axes = plt.subplots(1, len(target_ages) + 1, figsize = (15, 5))
        axes[0].imshow(original_image)
        axes[0].set_title('原图')
        axes[0].axis('off')

        for i, (gen_image, age) in enumerate(zip(generated_images, target_ages)):
            axes[i + 1].imshow(gen_image)
            axes[i + 1].set_title(f"预测年龄:{age}")
            axes[i + 1].axis('off')

        plt.tight_layout()
        return fig