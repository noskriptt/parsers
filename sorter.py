#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import numpy


def mergeSort(a, lb=0, rb=-1):
	""" Сортировка слиянием"""
    def merge(a, lb, split, rb):
        pos1 = lb
        pos2 = split + 1
        pos3 = 0
        temp = [i for i in range(rb - lb + 1)]
        while pos1 <= split and pos2 <= rb:
            if a[pos1] < a[pos2]:
                temp[pos3] = a[pos1]
                pos1 += 1
                pos3 += 1
            else:
                temp[pos3] = a[pos2]
                pos2 += 1
                pos3 += 1

        while pos2 <= rb:
            temp[pos3] = a[pos2]
            pos3 += 1
            pos2 += 1
        while pos1 <= split:
            temp[pos3] = a[pos1]
            pos3 += 1
            pos1 += 1

        a[lb:rb + 1] = temp

        del(temp)
    if lb < rb:
        split = (lb + rb) / 2
        mergeSort(a, lb, split)
        mergeSort(a, split + 1, rb)
        merge(a, lb, split, rb)

def ShellSort(a):
	""" Сортировка методом Шелла"""
	def new_incremet(a):
		i = int(len(a)/2)
		yield i
		while i != 1:
			if i == 2:
				i=1
			else:
				i = int(numpy.round(i/2.2))
			yield i
	for increment in new_incremet(a):
		for i in range(increment,len(a)):
			for j in range(i,increment-1,-increment):
				if a[j-increment] < a[j]:
					break
				a[j],a[j-increment] = a[j-increment],a[j]
	return a

def select_sort(a):
	""" Сортировка выбором (усточивая)"""
	if len(a) == 0: return
	for j in range(len(a)):
		min = j
		for i in range(j+1,len(a)):
			if a[i]<a[min]: min=i
		if min != j:
			value = a[min]
			for l in range(min,j-1,-1):
				a[l] = a[l-1]
			a[j]= value
