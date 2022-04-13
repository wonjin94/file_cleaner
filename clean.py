from tkinter import filedialog
import tkinter as tk
import os
import csv
import enchant
import time
import extension_set


# Input files' full path
# retruns file's location, file name
def process_full_file_path(file_path):
    
    splited = os.path.split(file_path)

    return splited[0],splited[1]

# input : full file name
# returns file name,file type  (without .file_type)
def get_file_extension(full_file_name):

    # split returns tuple [file_name, ".extension"]  ".", is included
    # tuple[1] == "" if there's no extension
    split = os.path.splitext(full_file_name)

    if split[1] == "":
        return split[0],"folder"

    return split[0],split[1][1:]

def clean(file_path, delete):

    # separate full file name and file location
    full_file_name = ""
    if not delete:
        full_file_name = file_path
    else:
        file_location, full_file_name = process_full_file_path(file_path)

    # separate file name and extension
    file_name,file_extension = get_file_extension(full_file_name)
    extensions = extension_set.process_file_extension(file_extension.lower())

    file_name_length = len(file_name)

    is_duplicate = is_duplicate_file(file_name)
    num_spaces,separated_file_words = has_spaces(file_name)

    num_real_words = has_real_word(separated_file_words)

    
    return full_file_name, extensions + [file_name_length,num_spaces,num_real_words],is_duplicate




# determine if the file is a duplicate (has (#) form)
# return 1 if True, 0 if False
def is_duplicate_file(file_name):
    
    if file_name[-1] ==")" and file_name[-3] == "(":
        return 1
    else:
        return 0

# input : file name
# output : boolean(file name has separator), list(words between separator if there's one, empty list if false)
# determines if file name has some sort of separator (" ", - or _) in between words
def has_spaces(file_name):
    file_name_separated = []
    num_space = 0

    dict = set(["-","_"," "])
    # previous index that had a space " "
    psi = -1
    for i in range(len(file_name)):
        if file_name[i] in dict:
            num_space += 1
            file_name_separated.append(file_name[psi+1:i])
            psi = i
    file_name_separated.append(file_name[psi+1:])
    return num_space,file_name_separated

# input : List of words
# output: list of booleans (True if word is a real english word)
# Determines if words in the list is a real english word
def has_real_word(words):
    items = enchant._broker.list_languages()

    d = enchant.Dict("en_US")
    results = 0
    for i in range(len(words)):
        w = words[i]

        # check word is alphabet (includes korean)
        if w.isalpha():

            # if word is english check if its a real word
            if w.upper() != w.lower(): 
                if d.check(w):
                    results += 1
            # word is korean, include it as real word
            else:
                results += 1
    return results









