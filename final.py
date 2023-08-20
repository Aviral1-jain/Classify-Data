import pandas as pd
from pycaret.classification import *
import os
import sys
file='data.csv'
myDataSet = pd.read_csv(file)
myDataSet.set_index('Peptide_Sequence',inplace=True)
myDataSet.head()
setup(data = myDataSet, target='target')
cm = compare_models()
df= pull()
sd=pd.DataFrame(df['Accuracy'])
sd.rename(columns={'Accuracy' :'Accuracy without normalization'}, inplace=True)
sd1=sd.copy()
normalize_method = ['zscore', 'minmax', 'maxabs', 'robust']
for meth in normalize_method:
  setup(data=myDataSet, target='target', normalize = True, normalize_method = meth)
  cm = compare_models()
  df1= pull()
  sd1[meth]=df1['Accuracy']

sd1.to_csv('output-Normalization.csv')

