# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 01:05:24 2020

@author: nyamochir
"""
limit = 0
with open("testing_new.txt", "r") as file:
    for row in file.readlines():
        #row = row.split("\\")
        #new_row = ""
        #for i in row:
        #    new_row += i+ "/"
        #new_row = new_row[:-1]
        if limit >10:
            break
        limit+=1
        print(row)
