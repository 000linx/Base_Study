import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class CelebADataLoader:
    """CelebA数据集加载器"""
    
    def __init__(self, data_dir="celeba_data"):
        self.data_dir = data_dir
        self.attr_file = os.path.join(data_dir, "list_attr_celeba.csv")
        self.image_dir = os.path.join(data_dir, "img_align_celeba")
        
        if not os.path.exists(self.attr_file):
            error_msg = f"属性文件未找到: {self.attr_file}"
            if st:
                st.error(error_msg)
                st.markdown("""
                - 请检查路径是否正确: `F:\\Base_Study\\Python\\数据分析\\大作业\\celeba_data\\list_attr_celeba.csv`
                - 确保文件存在且路径正确
                """)
            else:
                print(error_msg)
            raise FileNotFoundError(error_msg)

        if not os.path.exists(self.image_dir):
            error_msg = f"图像目录未找到: {self.image_dir}"
            if st:
                st.error(error_msg)
            else:
                print(error_msg)
            raise FileNotFoundError(error_msg)
        
        # 加载属性数据
        self.attr_df = self._load_attributes()
        
        # 选择关键属性
        self.selected_attrs = [
            'Male', 'Young', 'Eyeglasses', 'Smiling', 
            'Wavy_Hair', 'Bald', 'Mustache', 'Chubby'
        ]
        
    def _load_attributes(self):
        """加载属性CSV文件"""
        df = pd.read_csv(self.attr_file)
        # 将-1转换为0
        if 'File_name' in df.columns:
            df = df.rename(columns = {'File_name' : 'image_id'})
        else:
            if df.columns[0] != 'image_id':
                df = df.rename(columns = {df.columns[0]: 'image_id'})
        for col in df.columns:
            if col != 'image_id':
                df[col] = df[col].replace(-1,0)
                df[col] = pd.to_numeric(df[col], errors = 'coerce').fillna(0).astype(int)
        return df
    
    def get_image_path(self, image_id):
        """获取图像路径"""
        if not image_id.endswith('.jpg'):
            image_id += '.jpg'
        return os.path.join(self.image_dir, image_id)
    
    def get_sample_data(self, sample_size=1000):
        """获取样本数据"""
        return self.attr_df.sample(min(sample_size, len(self.attr_df)))
    
    def get_image(self, image_id, size=(256, 256)):
        """加载并调整图像大小"""
        image_path = self.get_image_path(image_id)

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图像文件未找到: {image_path}")
        image = cv2.imread(image_path)
        if image is None:
            raise IOError(f"无法读取图像: {image_path}")
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if size:
            image = cv2.resize(image, size)
        return image
    
    def show_sample_images(self, num_samples=5):
        """显示样本图像"""
        sample_df = self.get_sample_data(num_samples)
        if len(sample_df) == 0:
            fig, ax = plt.subplots(figsize = (10, 5))
            ax.text(0.5,0.5,"没有可用的样本数据", ha = 'center', va = 'center', fontsize = 18, color = 'red')
            ax.axis('off')
            return fig
        fig, axes = plt.subplots(1, min(num_samples, len(sample_df)), figsize = (20, 5))
        if num_samples == 1:
            axes = [axes]
        for i, (idx, row) in enumerate(sample_df.iterrows()):
            try:
                image_id = row['image_id']

                if not isinstance(image_id, str):
                    image_id = str(image_id)
                
                image = self.get_image(image_id, size = (128, 128))
                axes[i].inshow(image)

                attrs = []
                for attr in self.selected_attrs:
                    if attr in row and row[attr] == 1:
                        attrs.append(attr)
                
                title = f"ID: {image_id}\n{','.join(attrs)}"
                axes[i].set_title(title, fontsize = 10)
                axes[i].axis('off')
            except Exception as e:
                error_msg = f"处理图像: {str(e)}"
                print(error_msg)
                axes[i].text(0.5,0.5,error_msg, ha = 'center', va = 'center', transform = axes[i].transAxes, fontsize = 8, color = 'red')
                axes[i].axis('off')
        plt.tight_layout()
        return fig