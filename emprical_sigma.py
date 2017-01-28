# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:41:25 2017

@author: KimuKook
"""

import numpy as np

def emprical_sigma(x,s):
    N = len(x)
    sigma = np.zeros(len)
    for jj in range(len(s)):
        mu = np.zeros([len(s)])
        for i in range(N//s[jj]-1):
            inds = np.arange(i*s[jj],(i+1)*s[jj])
            mu[i] = mean(x[np.unravel_index(inds,x.shape,'F')])
        sigma = 
#%%
import numpy as np
x = np.array([[1,2,3],[4,2,1],[2,4,3]])
s = np.array([2,2,2])
inds = np.arange(0*s[1],1*s[1])
result = x[np.unravel_index(inds,x.shape,'F')]
print(result)