# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:06:46 2021

@author: AMD_PC
"""
from scipy.stats import stats
import pandas as pd
import numpy as np
df = pd.read_excel('data_total.xlsx', index_col=False)
g = df['green']
b = df['blue']
r = df['red']
e = df['rededge']
n = df['nir']
data = {'g': df['green'], 'b': df['blue'], 'r': df['red'], 'e': df['rededge'], 'n': df['nir'],
        'a': np.log(df['blue']+2), 's': np.log(df['green']+2), 'd': np.log(df['red']+2),
        'f': np.log(df['rededge']+2), 'h': np.log(df['nir']+2)}
# 種類跟數量
substance = input("代測物質:")
substance = df[substance]


def triple_plus(n1, n2, n3):
    value = n1+n2+n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_minus(n1, n2, n3):
    value = n1-n2-n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_multiply(n1, n2, n3):
    value = n1*n2*n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_plus1(n1, n2, n3):
    value = (n1+0.000001)/(n2+n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_minus1(n1, n2, n3):
    value = n1/(n2-n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_divide(n1, n2, n3):
    value = (n1+0.000001)/(n2*n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_minusmultiply(n1, n2, n3):
    value = (n1-n2)*n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_plusmultiply(n1, n2, n3):
    value = (n1+n2+0.000001)*n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_minusdivide(n1, n2, n3):
    value = (n1-n2)/n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_plusdivide(n1, n2, n3):
    value = (n1+n2)/n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_multiplydivide(n1, n2, n3):
    value = (n1*n2+0.000001)/n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_totaldivide(n1, n2, n3):
    value = 1/(n1*n2*n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def triple_lnplus(n1, n2, n3):
    value = np.log(n1+n2+n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnminus(n1, n2, n3):
    value = np.log(n1-n2-n3+4)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnmultiply(n1, n2, n3):
    value = np.log(n1*n2*n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnplus1(n1, n2, n3):
    value = np.log((n1+0.000001)/(n2+n3))
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnminus1(n1, n2, n3):
    value = np.log(n1/(n2-n3+2))
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lndivide(n1, n2, n3):
    value = np.log((n1+0.000001)/(n2*n3))
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnminusmultiply(n1, n2, n3):
    value = np.log((n1-n2+2)*n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnplusmultiply(n1, n2, n3):
    value = np.log((n1+n2+0.000001)*n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnplusdivide(n1, n2, n3):
    value = np.log((n1+n2)/n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def triple_lnmultiplydivide(n1, n2, n3):
    value = np.log(((n1*n2)+0.000001)/n3)
    p = stats.pearsonr(value, substance)
    return abs(p[0])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def normal(value):
    p = stats.pearsonr(value, substance)
    return abs(p[0])

def plus(n1, n2):
    value = n1+n2
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def minus(n1, n2):
    value = n1-n2
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def ln_plus(n1, n2):
    value = np.log(n1+n2)
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def ln_minus(n1, n2):
    value = np.log(n1-n2+2)  # +2的原因是怕相減為負數無法進行對數運算
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def divide(n1, n2):
    value = n1/n2
    p = stats.pearsonr(value, substance)
    return abs(p[0])


def ln_divide(n1, n2):
    value = np.log(n1/n2)
    p = stats.pearsonr(value, substance)
    return abs(p[0])
