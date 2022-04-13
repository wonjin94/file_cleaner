import pandas as pd
import os


# concat train data into a single pandas data frame
def get_data():

    data_keep = pd.read_csv("train_keep.txt",sep = ",",header = None)
    data_delete = pd.read_csv("train_delete.txt",sep = ",",header = None)


    data = pd.concat([data_keep,data_delete])
    
    # assign column names
    data.columns = ["do_manual_check",
                "ext_toDelete",
                "is_doc", 
                "is_pic",
                "is_coding_file", 
                "is_vid", 
                "is_mp3", 
                "is_shortcut",
                "is_folder",
                "is_unclassified",
                "name_length",
                "num_spaces",
                "num_real_words",
                "file_size",
                "days_since_created",
                "is_duplicate",
                "delete_file",
                "file_name"]

    return data
