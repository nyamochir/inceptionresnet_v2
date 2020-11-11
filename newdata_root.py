# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:02:31 2020

@author: nyamochir
"""

import os
current = 'a0'
index = 1
video_file_list = []
try:
    os.mkdir("data")
except:
    pass
try:
    os.mkdir('data/k28dtm7tr6-1')
except:
    pass

try:
    os.mkdir("data/k28dtm7tr6-1/train")
except:
    pass
try:
    os.mkdir("data/k28dtm7tr6-1/test")
except:
    pass
if len(os.listdir("data")) == 0:
    print("Please prepare data!")


for i in os.listdir('data/k28dtm7tr6-1/'):
    npart = current+str(index)
    #try:
    #    os.mkdir('data/k28dtm7tr6-1/'+current+str(index))
    #except:
    #    pass
    if ".mp4" in i:
        video_file_list.append(i)
        
    
    
    index+=1
dirnames = []
for video in video_file_list:
    if video[:3] not in dirnames:
        dirnames.append(video[:3])
dirnames
import shutil
test_directory = 'data/k28dtm7tr6-1/test/'
for direc in dirnames:
    try:
        os.mkdir(test_directory+direc)
    except:
        pass
    for video in video_file_list:
        if direc == video[:3]:
            shutil.copy('data/k28dtm7tr6-1/'+video, test_directory+direc+"/"+video)
for video in video_file_list:
    if video[:3] not in dirnames:
        dirnames.append(video[:3])
dirnames = []
for video in video_file_list:
    if video[:3] not in dirnames:
        dirnames.append(video[:3])
import shutil
test_directory = 'data/k28dtm7tr6-1/train/'
for direc in dirnames:
    try:
        os.mkdir(test_directory+direc)
    except:
        pass
    for video in video_file_list:
        if direc == video[:3]:
            shutil.copy('data/k28dtm7tr6-1/'+video, test_directory+direc+"/"+video)
            
    