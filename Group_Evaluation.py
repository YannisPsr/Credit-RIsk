import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import Bootstrap
from sklearn.metrics import mean_squared_error


class Evaluation:
    
    # Initialising 
    def __init__(self, subgroup, numberOfIterations):  
        self.subgroup = subgroup
        self.data_size = subgroup.shape[0]
        self.columns = subgroup.columns
        self.numberOfIterations = numberOfIterations
    

    def modelEvaluation(self):
        MeanRMSE = 0
        for iter in range(self.numberOfIterations):
            sample, OutOfBagSample = Bootstrap.btstrap(self.subgroup, iter)
            sample = sample.apply(pd.to_numeric)
            mco = smf.ols('Indep_Var'+'~' + '+'.join(sample.columns),data = sample).fit()
            predictedValues = mco.predict(OutOfBagSample)

            rmse = mean_squared_error(self.subgroup.loc[OutOfBagSample.index].loc[:,'Indep_Var'],predictedValues, squared=False)
            MeanRMSE += rmse
        return MeanRMSE / self.numberOfIterations
