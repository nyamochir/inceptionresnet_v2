# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:55:23 2020

@author: nyamochir
"""
import tarfile
import os
import zipfile
print("Use sometimes --above can be useful --> trying to load the rest of the databses")
import shutil

#os.chdir("data/") # this notebook is related to the data directory since it is only going manipulate the data --> 
#os.listdir()
def extract_zipfile():
    zfile = zipfile.ZipFile("k28dtm7tr6-1.zip")
    zfile.extractall()
extract_zipfile()


def extract_zipfile():
    zfile = zipfile.ZipFile("k28dtm7tr6-1.zip")
    zfile.extractall()
extract_zipfile()

def get_tar_files(names):
    tar_files = []
    for name in names:
        if ".tar" in name:
            tar_files.append(name)
    return tar_files
names = os.listdir()
tar_files = get_tar_files(names)
#tar_files
def extract_tarfiles(tar_files):
    print("Starting to extract ...")
    for current_tarfile in tar_files:
        ctar = tarfile.TarFile(current_tarfile)
        ctar.extractall()
    print("Done to extract!")
    
extract_tarfiles(tar_files)
#dirname = tar_files[0]
#dirname =dirname.split(".")[0]
def build_classdir():
    name_init0 = "a0"
    name_init1 = "a"
    classes = []
    for i in range(1, 19):
        if i  < 10:
            print(name_init0+str(i))
            classes.append(name_init0+str(i))
        else:
            print(name_init1+str(i))
            classes.append(name_init1+str(i))
            
    try:
        os.mkdir("kard_data")
    except:
        pass
    for current_class in classes:
        try:
            os.mkdir("kard_data/"+current_class)
        except:
            pass
    print("successfully created!")
    return classes
build_classdir()

def get_video_files(extension):
    mp4_files=  []
    for i in os.listdir():
        #print(i)

        if extension in i:
            mp4_files.append(i)
    return mp4_files

def copy_files(mp4_files):
    print("Starting to copy video files ...")
    for file in mp4_files:
        class_name = file[:3]
        shutil.copy(file, "kard_data/"+class_name)
    print("Done!")
extension = ".mp4"
mp4_files =  get_video_files(extension)
copy_files(mp4_files)# 

def file_system_clean():
    print("Starting to clean the file system ...")

    for i in os.listdir():

        if i in tar_files or i == "kard_data" or i == "k28dtm7tr6-1.zip":
            pass
        else:
            try:
                os.remove(i)
            except:
                shutil.rmtree(i)
    print("Successful file System cleaning")
def prepare_train_test():
    
    shutil.copytree("kard_data/", "training/")
    shutil.copytree("kard_data/", "test/")
    #for i in os.listdir("kard_data"):
    #    shutil.copytree("kard_data/", "training/")
    #for i in os.listdir("kard_data"):
     #   shutil.copytree("kard_data/"+i, "test/")
file_system_clean()    

extension = ".mp4"# this would be different depending on the particular input itis giving it as training or the testing data
mp4_files= get_video_files(extension)
classes = build_classdir()

prepare_train_test()

