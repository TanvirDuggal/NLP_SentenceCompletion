# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:55:12 2020

@author: Tanvy
"""

import pandas as pd
import numpy as np

class GetData:
    dataList = []
    
    def __init__(self, path):
        self.readData(path)
    
    def readData(self, path):
        with open(path, 'r',  encoding="utf8") as f:
            for line in f.readlines():
                if line.strip('\n') != "":
                    print(">> ", line)
    
    def convertToDataframe(self):
        pass
    
gt = GetData('../datasets/AI_dataset.txt')