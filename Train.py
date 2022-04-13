

from tkinter import filedialog
import tkinter as tk
import time
import clean
import shutil
import os

# asks user to choose folder path and return it
def choose_folder():
    # choose folder path
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    return folder_selected
# asks user to choose files to be deleted and return the list of file paths
def choose_files():
    # get list of files in the folder
    root = tk.Tk()
    root.withdraw()

    # full path of the files will be stored in tuples
    raw_file_names = filedialog.askopenfilenames()

    return raw_file_names


# input time
# returns number of days since start time and today
def time_diff (start_time):
    diff = time.time() - start_time
    diff = diff/(60*60*24)
    return round(diff)


# input file path
# returns atime, mtime
def get_file_time(file_path):

    time_created = os.path.getctime(file_path)
    days_since_created = time_diff(time_created)
    return days_since_created

# input array of strings
# combines array elements into single string separated by , and \n at end and returns it
def combine_info (info):

    return ",".join(str(x) for x in info) + "\n"

def get_var (f,folder,YN,check,delete):
    file_name,file_name_info,is_duplicate = clean.clean(f,delete)

    if not delete:
        f = folder + "/" + f
    days_since_created = get_file_time(f)
    file_size = os.path.getsize(f)

    file_info = combine_info([str(check)] + file_name_info + [file_size,days_since_created,is_duplicate,str(YN),file_name])


    return file_info,file_name


# check - 1 do manual check by user, 0 for auto check
# stores files' info into train file
# moves files to be deleted into folder

def train_files_delete (check) :
    files = choose_files()
    trash_folder_location = ""

    if check:
        trash_folder_location =  os.getcwd() + "/trash_manual"
    else:
        trash_folder_location =  os.getcwd() + "/trash_auto"
    
    yn = 1
    train_file = "train_delete.txt"

    with open(train_file,"a", encoding="utf=8") as train_file:
        for f in files:
            info,file_name = get_var(f,"",yn,check,1)
            
            shutil.move(f,trash_folder_location +"/"+ file_name)
            train_file.write(info)



    



def train_files_keep (folder,files):

    # choose folder to train, all files are to be kept
    # choose files to be manually checked

    delete_files_dict = {}
    for f in files:
        delete_files_dict[f] = 1
    

    all_files = os.listdir(folder)
    with open("train_keep.txt","a",encoding = "utf=8") as train_file:
        check = 0
        for f in all_files:

            if f in delete_files_dict:
                check = 1
            else:
                check = 0
            info, file_name = get_var(f,folder,0,check,0)

            train_file.write(info)
    
    
