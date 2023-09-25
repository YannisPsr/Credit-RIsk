# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 2021

@author: PSARRAS IOANNIS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class COLLINEARITY:   
    #Initializing the class and create the appropriate variables
    def __init__(self, data):
        self.CorMatrix = data.corr().apply(np.abs, axis = 0)
        self.data = data
        
    def HeatMap(self):
        #Visualiser la matrice de correlation
        top_corr_features = self.CorMatrix.index
        plt.figure(figsize=(10,10))
        #plot heat map
        g=sns.heatmap(self.CorMatrix,annot=True,cmap="RdYlGn")
        
        
    def Combinations(self,threshold):
        # The correlation of the independent variables with the target is the indicator if the quantitative explanation of the linear regression
        Data = self.CorMatrix.corr().apply(np.abs, axis = 0)
        dataToBeAssociated = Data[Data < threshold]
        dataToBeAssociated.drop(index = 'Indep_Var', inplace = True)
        dataToBeAssociated.drop(columns = ['Indep_Var'], inplace = True)
        return [list(dataToBeAssociated.iloc[i].dropna().index) + [dataToBeAssociated.index[i]] for i in range(8)] #Combinations
    