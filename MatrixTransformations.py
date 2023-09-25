# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 2021

@author: PSARRAS IOANNIS
"""

import numpy as np
import pandas as pd
from scipy.stats import norm


class TransMatrix:
    
    # Initialising with the crosstab
    def __init__(self, crossTab, datetime):
        self.initialMatrix = crossTab
        # List which contains matrices with rows of classes and columns with transitions on each class.
        self.ListDesMatricesDeNombreDeContreparties = []
        # List which contains the rate of transitions from each class(row) to other classes(columns).
        self.ListDesMatricesDuTauxDeMigration = []
        # List which contains lists with the sum of each row of the matrix
        self.ListLineSum = []
        # Numpy object with all the dates that interests us
        self.dates = datetime
        # List of Matrices that we need to transform
        self.MatricesAnnuelles = []
        self.MatricesAnnuellesAjusted = []
        #List of annu]al cumumative Matrices
        self.MatricesCumulativeAnnuelles = []
        # La matrice TTC( Throuth the cycle)
        self.MatriceTTC = pd.DataFrame()  #Nombre de transitions par classe
        self.MatriceTTCAjusted = pd.DataFrame()  #Probabilité de transitions
    
    def NumberOfCounterPartiesCalculation(self,result):
        # We use the matrix of two months concatenate and we produce the Number of counterparties from i to j
        NombreDeContreparties = []
        LineSum = []
        for i in range(1,12):
            listDeContreparties = []
            lineSum = 0
            for y in range(1,12):
                listDeContreparties.append(result.loc[(result['Class1']==i) & (result['Class2']==y)].shape[0])
                lineSum += result.loc[(result['Class1']==i) & (result['Class2']==y)].shape[0]
            NombreDeContreparties.append(listDeContreparties)
            LineSum.append(lineSum)
        return (NombreDeContreparties,LineSum)
    
    def setNumberOfConterparties(self, index):
            # We take two months and concatenate their values at common index and columns
            NombreDeContreparties1 = self.initialMatrix.loc[(self.dates[index],)]
            NombreDeContreparties2 = self.initialMatrix.loc[(self.dates[index+1],)]
            result = pd.concat([NombreDeContreparties1, NombreDeContreparties2], axis=1)
            result.columns = ['Class1','Class2']
            result.dropna(inplace=True)
            (NombreDeContreparties,LineSum) = self.NumberOfCounterPartiesCalculation(result)
            self.ListDesMatricesDeNombreDeContreparties.append(NombreDeContreparties)
            self.ListLineSum.append(LineSum)
    
    
    def getNumberOfContreparties(self,index):
        NombreDeContreparties = self.ListDesMatricesDeNombreDeContreparties[index]
        NombreDeContreparties = pd.DataFrame(NombreDeContreparties)
        NombreDeContreparties.columns = [str(i) for i in range(1,12)] 
        NombreDeContreparties.index= range(1,12)
        return NombreDeContreparties
    
    
    def setMatricesOfMigrationRate(self,NombreDeContreparties,LineSum,listToAdd):
        dd = pd.concat([NombreDeContreparties.iloc[i]/LineSum[i] for i in range(11)],axis=1)
        MatriceDeMigration = dd.T*100
        listToAdd.append(MatriceDeMigration)
    
        
        
    def DataTransition(self):
        length = self.dates.shape[0]
        print('The number of months is : {}\n\n' .format(length))
        for i in range(length-1):
            self.setNumberOfConterparties(i)
            self.setMatricesOfMigrationRate(self.getNumberOfContreparties(i),self.ListLineSum[i],self.ListDesMatricesDuTauxDeMigration)
    
    
    def AnnualMigrationMatrices(self):
        length = self.dates.shape[0]
        year = int(length/12)
        for i in range(year):
            #Sum = []
            for y in range(i*12,(i+1)*12):
                if( y == 95): break
                if(y % 12 == 0):
                    MatricesParAn = self.getNumberOfContreparties(y)
                else:
                    MatricesParAn = self.getNumberOfContreparties(y) + MatricesParAn
            self.MatricesAnnuelles.append(MatricesParAn)
            
            Sum = MatricesParAn.apply(np.sum,axis=1).to_list()
            self.setMatricesOfMigrationRate(MatricesParAn,Sum,self.MatricesAnnuellesAjusted)
            
    
    def Cumulative(self,series):
        return pd.DataFrame([pd.DataFrame(series[range(series.shape[0]-1,i-1,-1)]).apply(np.sum).T for i in range(series.shape[0])])
    

    def TransformationToCumulativematrix(self,matrix):
        return pd.concat([matrix.apply(self.Cumulative,axis=1).iloc[i].T for i in range(matrix.shape[0])],ignore_index=True)
        
    
    def setMatricesCumulativeAnnuelles(self):
        for _,matrix in enumerate(self.MatricesAnnuellesAjusted):
            self.MatricesCumulativeAnnuelles.append(self.TransformationToCumulativematrix(matrix))
            
            
    def setMatriceTTC(self):
        self.MatriceTTC = self.MatricesAnnuelles[0]
        for ind,matrix in enumerate(self.MatricesAnnuelles):
            if(ind == 0) : continue
            self.MatriceTTC = self.MatriceTTC + matrix        
        
        LineSum = self.MatriceTTC.apply(np.sum,axis=1).to_list()
        dd = pd.concat([self.MatriceTTC.iloc[i]/LineSum[i] for i in range(11)],axis=1)
        self.MatriceTTCAjusted = dd.T*100
    
    
    def ThresholdCalcutors(self, Prob):
        # e the minimum difference
        Prob = float(Prob)
        Probability1 = norm.cdf(-2)*100
        Probability2 = norm.cdf(-1)*100
        Probability3 = norm.cdf(0)*100
        Probability4 = norm.cdf(1)*100
        Probability5 = norm.cdf(2)*100

        if(Prob < Probability1):
            result = self.Calculate(Prob, -2, Direction = 'Negative')
        elif(Prob < Probability2):
            result = self.Calculate(Prob, -1, Direction = 'Negative')
        elif(Prob < Probability3):
            result = self.Calculate(Prob, 0, Direction = 'Negative')
        elif(Prob < Probability4):
            result = self.Calculate(Prob, 1, Direction = 'Negative')  
        elif(Prob < Probability5):
            result = self.Calculate(Prob, 2, Direction = 'Negative')
        else:
            result = self.Calculate(Prob, 2, Direction = 'Positive')    
        return result

    def Calculate(self, Prob, threshold, Direction):
        if Direction == 'Negative':
            Difference = norm.cdf(threshold)*100 - Prob
            if Difference > 0.005 :          
                threshold = threshold - 0.01
                threshold = self.Calculate(Prob, threshold, 'Negative')
        else : 
            Difference = - norm.cdf(threshold)*100 + Prob
            if Difference > 0.005 :
                threshold = threshold + 0.01            
                threshold = self.Calculate(Prob, threshold, 'Positive')
        return threshold   
     
     
    def RowForThresholdCalcutors(self, series):
        return series.apply(self.ThresholdCalcutors)
        
    
    def getThresholdCalcutors(self, matrix):
        return matrix.apply(lambda row : self.RowForThresholdCalcutors(row))
        
        
        