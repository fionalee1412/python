#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd 

f = open(r'C:/Users/Fionali/Desktop/xxx.csv','r')
fufei = pd.read_csv(f,encoding='utf8')
print fufei