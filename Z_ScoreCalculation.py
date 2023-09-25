from scipy.stats import norm
import scipy.optimize as spo
import numpy as np

def Z_ScoreCalcul(transitionMatrix, transitionMatrixOfProbs, TTC, cor ): 

    def AnnualMatricesLineSum():
        return transitionMatrix.apply(np.sum,axis=1) 
    
    def numberOfTransition(line, col):
        return transitionMatrix.iloc[line,col]
    
    def probs(line,rating):
        return transitionMatrixOfProbs.iloc[line,rating]
    
    def f(Z):  
        brk = 0
        AnnualmatrixLineSum = AnnualMatricesLineSum()
        for line in range(AnnualmatrixLineSum.shape[0]):   
            lineSum = AnnualmatrixLineSum.iloc[line]
            for col in range(10):
                Xu = TTC.iloc[line,col]
                Xv = TTC.iloc[line,col+1]
                numberOfMigrations = lineSum - numberOfTransition(line, col)
                def IC(value, Z, r):  
                    return ((value - np.sqrt(r)*Z)/(np.sqrt(1-r)))

                def setTrProbOfIdioComp(Z):
                    return (norm.cdf(IC(Xu, Z, cor)) - norm.cdf(IC(Xv, Z, cor)))
                    
                def sumToMinimize(Z):
                    return ((numberOfMigrations * ( (probs(line,col) - setTrProbOfIdioComp(Z))**2 ) ) / (setTrProbOfIdioComp(Z) + (1 - setTrProbOfIdioComp(Z))))  
                    
                if(brk == 0):
                    res = sumToMinimize(Z)
                    brk = 1
                else:
                    res += sumToMinimize(Z) 
        return res
    
    x_start = 0
    result = spo.minimize(f, x_start, method='Nelder-Mead', options={"disp": False})
    
    return result.x[0]

