# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:56:40 2020

@author: Tanvy
"""

import pandas as pd
import numpy as np

from GetDataset import GetData
from Process import ProcessData

def main():
    gt = GetData('../datasets/AI_dataset.txt')
    gt.convertToDataframe()
    
    X  = gt.X
    Y  = gt.Y
    
    dfX = pd.DataFrame(X, columns=['review'])
    
    processData = ProcessData(dfX)
    processData.connvertLowerCase()
    processData.removeUnwantedItems()
    processData.lemmatization()
    processData.tokenizing()
    
    X_TextSeq = processData.txtSeq
    
    print(X_TextSeq)
    

if __name__ == '__main__':
    main()