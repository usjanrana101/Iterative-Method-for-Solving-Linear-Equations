#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 03:11:44 2020

@author: jaga
"""

import numpy as np
#actual solution (given)
x_true=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
# Given matrix
A=np.array([[0.2,0.1,1.0,1.0,0.],[0.1,4.0,-1.,1.,-1.],[1.,-1.,60.0,0.,-2.],[1.,1.,0.,8.0,4],[0,-1,-2,4,700.0]])
b=np.array([1.,2.,3.,4.,5.])
x_sol=np.zeros(5) # initial guess
count=0  # for counting the no of iteration
while max(abs(x_true-x_sol))>=0.01:   #  tolerance checking
    sum=np.zeros(5)
    for i in range(len(b)):
        for j in range(len(b)):
            if j!=i:
               sum[i]=sum[i]+A[i][j]*x_sol[j]     # Gauss_Seidal formula  
        x_sol[i]=(-sum[i]+b[i])/A[i][i]
    count=count+1
print("No of iteration taken  by Gauss_Seidal Method to reach this accuracy: ",count)
print ("Then the sol : ",x_sol)