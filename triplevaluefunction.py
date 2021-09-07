# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:45:49 2021

@author: AMD_PC
"""
from itertools import combinations as comb
from itertools import product as prod
from scipy.stats import stats
import pandas as pd
import numpy as np

def triplevalue_plus(n1, n2, n3):
    value = n1+n2+n3
    return value


def triplevalue_minus(n1, n2, n3):
    value = n1-n2-n3
    return value


def triplevalue_multiply(n1, n2, n3):
    value = n1*n2*n3
    return value


def triplevalue_plus1(n1, n2, n3):
    value = n1/(n2+n3)  
    return value


def triplevalue_minus1(n1, n2, n3):
    value = n1/(n2-n3)
    return value


def triplevalue_divide(n1, n2, n3):
    value = n1/(n2*n3)   
    return value


def triplevalue_minusmultiply(n1, n2, n3):
    value = (n1-n2)*n3    
    return value


def triplevalue_plusmultiply(n1, n2, n3):
    value = (n1+n2)*n3   
    return value


def triplevalue_minusdivide(n1, n2, n3):
    value = (n1-n2)/n3    
    return value


def triplevalue_plusdivide(n1, n2, n3):
    value = (n1+n2)/n3    
    return value


def triplevalue_multiplydivide(n1, n2, n3):
    value = (n1*n2)/n3   
    return value


def triplevalue_totaldivide(n1, n2, n3):
    value = 1/(n1*n2*n3)  
    return value
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def triplevalue_lnplus(n1, n2, n3):
    value = np.log(n1+n2+n3)
    return value


def triplevalue_lnminus(n1, n2, n3):
    value = np.log(n1-n2-n3+4)
    return value


def triplevalue_lnmultiply(n1, n2, n3):
    value = np.log(n1*n2*n3)
    return value


def triplevalue_lnplus1(n1, n2, n3):
    value = np.log(n1/(n2+n3))
    return value


def triplevalue_lnminus1(n1, n2, n3):
    value = np.log(n1/(n2-n3+2))
    return value


def triplevalue_lndivide(n1, n2, n3):
    value = np.log(n1/(n2*n3))
    return value


def triplevalue_lnminusmultiply(n1, n2, n3):
    value = np.log((n1-n2+2)*n3)
    return value


def triplevalue_lnplusmultiply(n1, n2, n3):
    value = np.log((n1+n2)*n3)
    return value


def triplevalue_lnplusdivide(n1, n2, n3):
    value = np.log((n1+n2)/n3)
    return value


def triplevalue_lnmultiplydivide(n1, n2, n3):
    value = np.log((n1*n2)/n3)
    return value

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def value_normal(value):
    return value

def value_plus(n1, n2):
    value = n1+n2
    return value


def value_minus(n1, n2):
    value = n1-n2 
    return value


def value_ln_plus(n1, n2):
    value = np.log(n1+n2)
    return value


def value_ln_minus(n1, n2):
    value = np.log(n1-n2+2)  # +2的原因是怕相減為負數無法進行對數運算
    return value


def value_divide(n1, n2):
    value = n1/n2
    return value


def value_ln_divide(n1, n2):
    value = np.log(n1/n2)
    return value
