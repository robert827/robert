# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:01:03 2021

@author: AMD_PC
"""
from itertools import product as prod
import triplefunction
from triplefunction import substance, data
import pandas as pd
import triplevaluefunction

sequence = list(prod('bgrneasdfh', repeat=3))
times = len(sequence)
sequence_1 = list(prod('bgrneasdfh', repeat=2))
times_1 = len(sequence_1)
polynomial_list = []
key = 'n1+n2'
name_1 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.plus(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1-n2'
name_2 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.minus(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1+n2)'
name_3 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.ln_plus(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1-n2)'
name_4 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.ln_minus(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1/n2'
name_5 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.divide(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1/n2)'
name_6 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = format(triplefunction.ln_divide(
        data[zxc[0]], data[zxc[1]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1+n2+n3'
name = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_plus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1-n2-n3'
name1 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_minus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1*n2*n3'
name2 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_multiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1/n2/n3'
name3 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_divide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'n1/(n2+n3)'
name4 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_plus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

    key = 'n1/(n2-n3)'
    name5 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_minus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = '(n1-n2)*n3'
name6 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_minusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = '(n1+n2)*n3'
name7 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_plusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = '(n1-n2)/n3'
name8 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_minusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]
# 出錯主要是因為這組合(b+b)/b 都為固定值 所以無法推算

key = '(n1+n2)/n3'
name9 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_plusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = '(n1*n2)/n3'
name10 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_multiplydivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]
# 出錯主要是因為這組合(b+b)/b 都為固定值 所以無法推算
key = '1/(n1*n2*n3)'
name11 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_totaldivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1+n2+n3)'
name12 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnplus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1-n2-n3)'
name13 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnminus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1*n2*n3)'
name14 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1/(n2+n3))'
name15 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnplus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1/(n2-n3))'
name16 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnminus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1/(n2*n3))'
name17 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lndivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln((n1-n2)*n3)'
name18 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnminusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln(n1+n2)*n3)'
name19 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnplusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln((n1+n2)/n3)'
name20 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnplusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

key = 'ln((n1*n2)/n3)'
name21 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = format(triplefunction.triple_lnmultiplydivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]]), '.10f')
    polynomial_list += [zxcv_value]

total_name = list(zip(name_1+name_2+name_3+name_4+name_5+name_6+name+name1+name2+name3+name4+name5+name6+name7+name8+name9+name10+name11
                      + name12+name13+name14+name15+name16+name17+name18+name19+name20+name21,
                      sequence_1*int(6)+sequence*int(len(polynomial_list)/1000)))
drop_series = pd.Series(polynomial_list, index=total_name,
                        dtype='float64')  # float64 是重
drop_series = drop_series.drop_duplicates()

value_list = []

key = 'n1+n2'
name_1 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_plus(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'n1-n2'
name_2 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_minus(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'ln(n1+n2)'
name_3 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_ln_plus(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'ln(n1-n2)'
name_4 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_ln_minus(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'n1/n2'
name_5 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_divide(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'ln(n1/n2)'
name_6 = [key]*times_1
for i in range(0, times_1):
    zxc = sequence_1[i]
    zxcv_value = triplevaluefunction.value_ln_divide(
        data[zxc[0]], data[zxc[1]])
    value_list += [zxcv_value]

key = 'n1+n2+n3'
name = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_plus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'n1-n2-n3'
name1 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_minus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'n1*n2*n3'
name2 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_multiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'n1/n2/n3'
name3 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_divide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'n1/(n2+n3)'
name4 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_plus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'n1/(n2-n3)'
name5 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_minus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = '(n1-n2)*n3'
name6 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_minusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = '(n1+n2)*n3'
name7 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_plusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = '(n1-n2)/n3'
name8 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_minusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]
# 出錯主要是因為這組合(b+b)/b 都為固定值 所以無法推算

key = '(n1+n2)/n3'
name9 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_plusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = '(n1*n2)/n3'
name10 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_multiplydivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]
# 出錯主要是因為這組合(b+b)/b 都為固定值 所以無法推算
key = '1/(n1*n2*n3)'
name11 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_totaldivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1+n2+n3)'
name12 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnplus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1-n2-n3)'
name13 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnminus(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1*n2*n3)'
name14 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1/(n2+n3))'
name15 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnplus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1/(n2-n3))'
name16 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnminus1(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1/(n2*n3))'
name17 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lndivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln((n1-n2)*n3)'
name18 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnminusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln(n1+n2)*n3)'
name19 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnplusmultiply(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln((n1+n2)/n3)'
name20 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnplusdivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

key = 'ln((n1*n2)/n3)'
name21 = [key]*times
for i in range(0, times):
    zxc = sequence[i]
    zxcv_value = triplevaluefunction.triplevalue_lnmultiplydivide(
        data[zxc[0]], data[zxc[1]], data[zxc[2]])
    value_list += [zxcv_value]

name_list = pd.Series(tuple(value_list), index=total_name)
biggest = drop_series.nlargest(11)
polynomial = biggest.index
