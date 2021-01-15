# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:55:12 2020

@author: Tanvy
"""

import pandas as pd
import numpy as np

class GetData:
    dataList = []
    X        = []
    Y        = []
    
    X_df     = ''
    Y_df     = ''
    
    def __init__(self, path):
        self.readData(path)
    
    def readData(self, path):
        with open(path, 'r',  encoding="utf8") as f:
            for line in f.readlines():
                if line.strip('\n') != "":
                    for word in line.split('.'):
                        if len(word) > 1:
                            self.dataList.append(word.strip())
                            
    def convertToDataframe(self):
        for data in self.dataList:
            statement = data.split(" ")
            for i in range(len(statement)):
                if i < len(statement)-4:
                    self.X.append(' '.join(statement[i:i+4]))
                    self.Y.append(statement[i+4])
        
gt = GetData('../datasets/AI_dataset.txt')
gt.convertToDataframe()