import os
import glob
import random

dir_index = (len(next(os.walk('data/interaction_segmented_set/train'))[1]))
file_index = (len(next(os.walk('data/interaction_segmented_set/train/0'))[0]))
index = 0
class_filename = []

while index < dir_index:
    list = glob.glob("data/interaction_segmented_set/train/" + str(index) + "/*.avi")
    for listname in list:
        fragment = listname.split("/")
        # class_filename.append(fragment[2]+ "/" + fragment[3].split(".")[0])
        class_filename.append(fragment[3].split(".")[0])

    random.shuffle(class_filename)
    train_list_class = class_filename[0:int(len(class_filename)*0.7)]
    print(train_list_class)
    test_list_class = class_filename[int(len(class_filename)*0.7):]

    train_list = open("dataset_list/trainlist_new.txt", "a")

    for listname in train_list_class:
        train_list.write(listname+" "+listname.split("\\")[0]+"\n")

    test_list = open("dataset_list/testlist_new.txt", "a")
    for listname in test_list_class:
        test_list.write(listname+" "+listname.split("\\")[0]+"\n")

    class_filename = []
    train_list.write("\n")
    test_list.write("\n")
    index += 1
