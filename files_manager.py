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
home_dir = "data/"
def extract_zipfile():
    zfile = zipfile.ZipFile("k28dtm7tr6-1.zip")
    zfile.extractall(home_dir)
extract_zipfile()

def get_tar_files(names):
    tar_files = []
    for name in names:
        if ".tar" in name:
            tar_files.append(name)
    return tar_files
names = os.listdir(home_dir)
tar_files = get_tar_files(names)
#tar_files
def extract_tarfiles(tar_files):
    print("Starting to extract ...")
    for current_tarfile in tar_files:
        ctar = tarfile.TarFile(home_dir+current_tarfile)
        ctar.extractall(home_dir)
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
        os.mkdir(home_dir+"kard_data")
    except:
        pass
    for current_class in classes:
        try:
            os.mkdir(home_dir+"kard_data/"+current_class)
        except:
            pass
    print("successfully created!")
    return classes
build_classdir()

def get_video_files(extension):
    mp4_files=  []
    for i in os.listdir(home_dir):
        #print(i)

        if extension in i:
            mp4_files.append(i)
    return mp4_files

def copy_files(mp4_files):
    print("Starting to copy video files ...")
    for file in mp4_files:
        class_name = file[:3]
        shutil.copy(home_dir+file, home_dir+"kard_data/"+class_name)
    print("Done!")
extension = ".mp4"
mp4_files =  get_video_files(extension)
copy_files(mp4_files)# 

def file_system_clean():
    print("Starting to clean the file system ...")

    for i in os.listdir(home_dir):

        if i in tar_files or i == "kard_data" or i == "k28dtm7tr6-1.zip":
            pass
        else:
            try:
                os.remove(home_dir+i)
            except:
                shutil.rmtree(home_dir+i)
    print("Successful file System cleaning")
def prepare_train_test():
    
    shutil.copytree(home_dir+"kard_data/", home_dir+"training/")
    shutil.copytree(home_dir+"kard_data/", home_dir+"test/")
    #for i in os.listdir("kard_data"):
    #    shutil.copytree("kard_data/", "training/")
    #for i in os.listdir("kard_data"):
     #   shutil.copytree("kard_data/"+i, "test/")
file_system_clean()    

extension = ".mp4"# this would be different depending on the particular input itis giving it as training or the testing data
mp4_files= get_video_files(extension)
classes = build_classdir()

prepare_train_test()

