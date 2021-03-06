# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:51:36 2021

@author: User
"""

## Marketing Mix Modeling in Python


# Tested in python 2.7.6, scipy-0.13.3, numpy 1.9.0, and Linux Redhat 5.0/Windows 7


# -*- coding: cp950 -*-
import datetime  
import numpy as np  
import pandas as pd
import numpy.random as random
import statsmodels.api as sm
import statsmodels.tsa as tsa
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

# Create dataset

def create_dataset():
 
    data = pd.DataFrame()
    
    np.random.seed(0); np.random.seed(1) # Random seed needs to reset here for reproducibility

    data ['sales'] = [100,200,300,500,750,900,1000,1300,1450,1500,1600,1400]

    print data['sales'].mean(), data['sales'].std()

    data ['TV']=[10,10,10,10,20,30,45,40,30,35,35,37]

    print data['TV'].mean(), data['TV'].std()

    data ['Social_media'] = [10,20,30,30,40,40,45,50,60,55,60,62]
    
    print data['Social_media'].mean(), data['Social_media'].std()
    
    data ['Radio'] = random.choice(range(1, 11), data.shape[0])

    print data['Radio'].mean(), data['Radio'].std(),data['Radio'].max(),data['Radio'].min()

    data ['Paper-Media']=[5,7,8,10,10,13,12,15,12,14,10,10]
    
    print data['Paper-Media'].mean(), data['Paper-Media'].std()

    return data

#create dataset and print first and last rows of data

data = create_dataset()  

### Incude adstock

ar_coeff = .5

TV_adstock = tsa.filters.filtertools.recursive_filter(data ['TV'], ar_coeff)

Social_media_adstock = tsa.filters.filtertools.recursive_filter(data ['Social_media'], ar_coeff)

Radio_adstock = tsa.filters.filtertools.recursive_filter(data['Radio'], ar_coeff)

Paper_Media_adstock = tsa.filters.filtertools.recursive_filter(data ['Paper-Media'], ar_coeff)

# Combine all the pandas series together

df_ad= pd.concat([data ['TV'],TV_adstock,data ['Social_media'],Social_media_adstock,data ['Radio'],Radio_adstock, data ['Paper-Media'],Paper_Media_adstock],axis=1)

sales=data ['sales'] 

modelfit2 = smf.ols(formula='sales ~ TV_adstock + Social_media_adstock + Radio_adstock+Paper_Media_adstock',data=df_ad).fit()

print modelfit2.summary()
