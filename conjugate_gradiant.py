#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:06:41 2020

@author: jaga
"""

import numpy as np
#actual solution (given)
x_true=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
# Given matrix
A=np.array([[0.2,0.1,1.0,1.0,0.],[0.1,4.0,-1.,1.,-1.],[1.,-1.,60.0,0.,-2.],[1.,1.,0.,8.0,4],[0,-1,-2,4,700.0]])
b=np.array([1.,2.,3.,4.,5.])
x_sol=np.zeros(5) # initial guess
r=b-x_sol #Residual vector along the negative gradiant 
d=r
count=0  # for counting the no of iteration
while max(abs(x_true-x_sol))>=0.01:   #  tolerance checking
    '''
        Into this loop the recurrence formulaues are updated
        '''
    Ad=np.dot(A,d)
    s=np.dot(r,r)/np.dot(d,Ad)
    x_sol=x_sol+np.dot(s,d)    
    r=r-np.dot(s,Ad)
    c=-np.dot(d,np.dot(A,r))/np.dot(d,Ad)
    d=r+np.dot(c,d)
    count=count+1
print("No of iteration taken by Conjugate Gradient Method to reach this accuracy: ",count)
print ("Then the sol :\n ",x_sol)         