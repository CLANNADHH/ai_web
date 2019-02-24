from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import *
import numpy as np

from aiweb import Aiapi

class BostonPredict(object):
    
    def __init__(self):
        """ 加载数据集 """
        self.boston = load_boston()
        self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.boston.data,self.boston.target,random_state = 33,test_size = 0.25)
        self.ss_x = StandardScaler()
        self.ss_y = StandardScaler()
        
    def deal_data(self):
        #分别对训练集合测试集 及特征值进行标准化处理
        self.x_train = self.ss_x.fit_transform(self.x_train)
        self.x_test = self.ss_x.transform(self.x_test)
 
        #将标签数据转换为 m行1列
        self.y_train = np.array(self.y_train).reshape(-1,1)
        self.y_train = self.ss_y.fit_transform(self.y_train)
        self.y_test = np.array(self.y_test).reshape(-1,1)
        self.y_test = self.ss_y.transform(self.y_test)
    
    def train(self):
        """ 训练模型 """
        self.lr = LinearRegression()
        self.lr.fit(self.x_train,self.y_train)
    
    def predict(self,test_data):
        """ 预  测 """
        lr_predict_value = self.lr.predict(test_data)
        # print(self.x_test[:1])
        print(self.y_test[:1])
        print(lr_predict_value[:1])
        return lr_predict_value


boston = BostonPredict()
boston.deal_data()
boston.train()
# data = [[-0.37110656,-0.4963544,2.18871165,-0.28784917,0.28736315,-0.47123717,
           # 0.86786682,-0.84267867,-0.83882256,-1.27962268,0.3076075, 0.16256399,
           # 0.79860059]]
# data = boston.x_test[:1]
# boston.predict(data)


ai = Aiapi('config.ini')
ai.predict_class = boston
ai.predict_func = boston.predict
ai.predict_func_args = ['test_data']
ai.run()
