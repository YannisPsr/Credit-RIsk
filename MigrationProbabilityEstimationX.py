from scipy.stats import norm
import numpy as np
import pandas as pd


    
def Delta(sizes, TTC, cor, Z): 
    zero_data =  np.zeros(shape=(sizes[0],sizes[1]))
    DeltaMatrix = pd.DataFrame(zero_data, columns=range(1,sizes[1]+1))
    
    for line in range(sizes[0]):

        for col in range(sizes[1]-1):
            Xu = TTC.iloc[line,col]
            Xv = TTC.iloc[line,col+1]
        
            def setTrProbOfIdioComp(Xu, Xv):
                return (norm.cdf(IC(Xu, Z, cor)) - norm.cdf(IC(Xv, Z, cor)))
        
            def IC(value, Z, r):  
                return ((value - np.sqrt(r)*Z)/(np.sqrt(1-r)))
    
            DeltaMatrix.iloc[line,col] = setTrProbOfIdioComp(Xu, Xv)
        
        
        DeltaMatrix.iloc[line,10] = setTrProbOfIdioComp(TTC.iloc[line,10], -5)   
    return DeltaMatrix        
    
    
def ListOfDelta(length, TTC, cor, Z):
    ListOfDeltas = []
    
    for i in range(length):
        ListOfDeltas.append(Delta(TTC.shape, TTC, cor, Z.iloc[i]).round(8) * 100)
    
    return ListOfDeltas