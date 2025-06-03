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
        
        # 检查数据集是否存在
        if not os.path.exists(self.attr_file):
            if st:
                st.error("CelebA数据集未找到。请从以下链接下载并解压到data_dir目录:")
                st.markdown("""
                - 属性文件: [list_attr_celeba.csv](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
                - 图像文件: [img_align_celeba.zip](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
                """)
                st.stop()
            else:
                raise FileNotFoundError("CelebA数据集未找到，请下载并解压到指定目录")
        
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
        df = df.replace(-1, 0)
        return df
    
    def get_image_path(self, image_id):
        """获取图像路径"""
        return os.path.join(self.image_dir, image_id)
    
    def get_sample_data(self, sample_size=1000):
        """获取样本数据"""
        return self.attr_df.sample(sample_size)
    
    def get_image(self, image_id, size=(256, 256)):
        """加载并调整图像大小"""
        img_path = self.get_image_path(image_id)
        img = cv2.imread(img_path)
        if img is None:
            raise FileNotFoundError(f"图像未找到: {img_path}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if size:
            img = cv2.resize(img, size)
        return img
    
    def show_sample_images(self, num_samples=5):
        """显示样本图像"""
        sample_df = self.get_sample_data(num_samples)
        fig, axes = plt.subplots(1, num_samples, figsize=(20, 5))
        
        for i, (idx, row) in enumerate(sample_df.iterrows()):
            try:
                img = self.get_image(row['image_id'], size=(128, 128))
                axes[i].imshow(img)
                attrs = ", ".join([attr for attr in self.selected_attrs if row[attr] == 1])
                axes[i].set_title(f"ID: {row['image_id']}\n{attrs}")
                axes[i].axis('off')
            except Exception as e:
                print(f"加载图像错误: {e}")
        
        plt.tight_layout()
        return fig