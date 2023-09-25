# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 2021

@author: PSARRAS IOANNIS
@approuved by : RAZAGHI Aryan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class COLLINEARITY:   

    def HeatMap(self, result):
        #Visualiser la matrice de correlation
        corrmat = result.corr()
        top_corr_features = corrmat.index
        plt.figure(figsize=(10,10))
        #plot heat map
        g=sns.heatmap(corrmat,annot=True,cmap="RdYlGn")
        
        
    def Choose(self,result,threshold):
        correlationMatrix = result.corr()
        size = correlationMatrix.shape[0]
        variablesToInclude = []
        variablesToExclude = []
        for i in range(size-1):
            #List of booleans with the comparison between the value of the correlation for each column and the threshold, 
            #True if the value is superior of the threshold, False if not.
            listOfCorrelation = correlationMatrix.iloc[i+1:10,i] > threshold
            
            #Symmetric matrix, so we iterate only the Lower Trianguler without the diagonal.
            for y, bool in enumerate(listOfCorrelation): 
                if(bool):   
                    CorrelationWithTargetVarY = np.abs(correlationMatrix.iloc[y+1,10])
                    CorrelationWithTargetVarX = np.abs(correlationMatrix.iloc[10,i])
                    #We keep the variable whose correlation with the target is superior
                    if(CorrelationWithTargetVarX > CorrelationWithTargetVarY):
                        variablesToInclude.append(correlationMatrix.columns[i])
                        variablesToExclude.append(correlationMatrix.columns[y+i+1])
                    else:
                        variablesToInclude.append(correlationMatrix.columns[y+i+1])
                        variablesToExclude.append(correlationMatrix.columns[i])

        #Returns the List of the included variables and the List of the excluded.
        return (variablesToInclude,variablesToExclude)
     