import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import umap
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import streamlit as st

class FaceFeatureVisualizer:
    def __init__(self, feature, attr_df):
        self.feature = feature
        self.attr_df = attr_df
        self.scaled_feature = StandardScaler().fit_transform(feature)
        self.umap_embedding = self._calculate_umap()
        self.clusters = self._calculate_clusters()

    def _calculate_umap(self):
        if st:
            with st.spinner("正在计算UMAP..."):
                reducer = umap.UMAP(n_components=2, random_state=42)
                return reducer.fit_transform(self.scaled_feature)
        else:
            reducer = umap.UMAP(n_components = 2, random_state = 42)
            return reducer.fit_transform(self.scaled_feature)
    
    def plot_attribute_distribution(self, attribute):
        fig, ax = plt.subplots(figsize = (10,6))
        sns.histplot(data = self.attr_df, x = attribute, kde = True, bins = 20)
        plt.title(f"{attribute}分布", fontsize = 14)
        plt.xlabel(attribute, fontsize = 12)
        plt.ylabel('数量', fontsize = 12)
    
    def plot_correlation_heatmap(self):
        combined = np.hstack((self.scaled_feature, self.attr_df.values))
        corr_matrix = pd.DataFrame(
            np.corrcoef(combined.T),
            columns = list(range(self.feature.shape[1])) + list(self.attr_df.colums)
        )

        attr_corr = corr_matrix.iloc[self.feature.shape[1]:, :self.feature.shape[1]]
        plt.title("人脸特征与属性的相关性", fontsize = 16)
        plt.xlabel("人脸特征维度", fontsize = 12)
        plt.ylabel("面部属性", fontsize = 12)
        return plt.gcf()
    
    def plt_umap_projection(self, color_by = 'cluster'):
        if color_by == 'clusters':
            color_data = self.clusters
            title = 'UMAP投影（按聚类）'
            camp = 'tab10'
        else:
            color_data = self.attr_df[color_by]
            title = f'UMAP投影（按{color_by}）'
            camp = 'viridis'

        fig  = plt.figure(figsize = (10,8))
        scatter = plt.scatter(
            self.umap_embedding[:,0],self.umap_embedding[:, 1],
            c = color_data, cmap = camp, alpha = 0.7, s = 50
        )

        if color_by == 'cluster':
            plt.legend(*scatter.legend_elements(), title = '聚类')
        else:
            plt.colorbar(label = color_by)
        
        plt.title(title, fontsize = 14)
        plt.xlabel('UMAP 1', fontsize = 12)
        plt.ylabel('UMAP 2', fontsize = 12)
        return fig
    
    def analyze_age_related_features(self):
        young_mask = self.attr_df['Young'] == 1
        old_mask = self.attr_df['Young'] == 0

        feature_diffs = []
        for i in range(self.feature.shape[1]):
            young_mean = self.feature[young_mask, i].mean()
            old_mean = self.feature[old_mask, i].mean()
            feature_diffs.append(old_mean - young_mean)

        fig1 = plt.figure(figsize = (12 ,6))
        plt.bar(range(len(feature_diffs)), feature_diffs)
        plt.axhline(0, color = 'k', linestyle = '--')
        plt.title('年龄相关特征差异', fontsize = 14)
        plt.xlabel('维度特征', fontsize = 12)
        plt.ylabel('特征差异', fontsize = 12)

        age_values = np.where(self.attr_df['Young'], 0, 1)
        reg = LinearRegression().fit(self.feature, age_values)

        top_indices = np.argsort(np.abs(reg.coef_))[-5:][::-1]
        fig2 = plt.figure(figsize = (10,6))
        plt.bar(range(5), reg.coef_[top_indices])
        plt.xticks(range(5), top_indices)
        plt.title('年龄预测特征', fontsize = 14)
        plt.xlabel('维度特征', fontsize = 12)
        plt.ylabel('系数', fontsize = 12)

        return fig1, fig2
    
