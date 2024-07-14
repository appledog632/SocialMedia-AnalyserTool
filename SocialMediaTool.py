import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from random import choice

class DataAnalysisTool:
    def __init__(self, num_records=1000):
        self.data = self.generate_dummy_data(num_records)
        print("-----WELCOME TO THE SOCIAL MEDIA ANALYSER-----")
        
    def generate_dummy_data(self, num_records):
        topics = ['Technology', 'Sports', 'Fashion', 'Politics', 'Food']
        genders = ['Male', 'Female']
        age_mean = 30
        age_std = 10
        watchtime_mean = 60
        watchtime_std = 20
        
        data = {
            'topic': [choice(topics) for _ in range(num_records)],
            'gender': [choice(genders) for _ in range(num_records)],
            'age': np.random.normal(age_mean, age_std, num_records).astype(int),
            'watchtime': np.random.normal(watchtime_mean, watchtime_std, num_records)
        }
        
        return pd.DataFrame(data)
        
    def trending_topics(self, n=5):
        trending_topics = self.data['topic'].value_counts().head(n)
        plt.figure(figsize=(10, 6))
        trending_topics.plot(kind='bar', color='skyblue')
        plt.title('Top Trending Topics')
        plt.xlabel('Topics')
        plt.ylabel('Count')
        plt.show()
        
    def gender_distribution(self):
        plt.figure(figsize=(8, 6))
        sns.countplot(x='gender', data=self.data, palette='pastel')
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()
        
    def age_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.data, x='age', bins=20, kde=True, color='salmon')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.show()
        
    def watchtime_based_on_gender(self):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='gender', y='watchtime', data=self.data, palette='Set2')
        plt.title('Watch Time Based on Gender')
        plt.xlabel('Gender')
        plt.ylabel('Watch Time')
        plt.show()


data_tool = DataAnalysisTool(num_records=1000)
data_tool.trending_topics()
data_tool.gender_distribution()
data_tool.age_distribution()
data_tool.watchtime_based_on_gender()