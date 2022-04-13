import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import simpledialog
import Train
import clean

# functions for interactive menu to train and clean files


# https://pythonguides.com/python-tkinter-messagebox/
# examples for messagebox

# function to make go back button 
def go_back_button(menu):
    menu.destroy()

# function for task completed message box
def task_done_message():
    messagebox.showinfo("Notice","Task Completed")


# train_files menu
def main_menu_b1_train_files():
    global train_files_menu
    train_files_menu = Toplevel(main_menu)
    train_files_menu.geometry("400x400")
    
    train_files_menu_label1 = tk.Label(train_files_menu, text = "Which files to train?")

    train_files_menu_b1 = tk.Button(train_files_menu,text = "Files to delete", command = train_files_menu_delete_files_button)
    train_files_menu_b2 = tk.Button(train_files_menu,text = "Files to keep", command = train_files_menu_keep_files_button)
    train_files_menu_b3 = tk.Button(train_files_menu,text = "Go Back", command = lambda: go_back_button(train_files_menu))

    train_files_menu_label1.pack(pady = 5)
    train_files_menu_b1.pack(pady = 10)
    train_files_menu_b2.pack(pady = 35)
    train_files_menu_b3.pack(pady = 90)


# train files menu for files to keep
def train_files_menu_keep_files_button():
    global keep_files_menu
    keep_files_menu = Toplevel(train_files_menu)
    keep_files_menu.geometry("400x400")

    button1 = tk.Button(keep_files_menu, text = "Choose folder and files to Train", command = choose_folder_file_callfunc)
    button2 = tk.Button(keep_files_menu, text = "Go Back", command = lambda: go_back_button(keep_files_menu))
    button1.pack(pady = 5)
    button2.pack(pady = 90)


# select files and folder to be trained
def choose_folder_file_callfunc():
    
    while True:
        folder = Train.choose_folder()
        files = Train.choose_files()

        
        # get file folder
        files_folder,file_name = clean.process_full_file_path(files[0])

        # check if folder and file's folder is same
        if folder == files_folder:
                break
        else:
            messagebox.showwarning("Error","Selected files are not located in the selected folder.\nSelect correct folder and files")
        

    Train.train_files_keep(folder,files)
    task_done_message()

    keep_files_menu.destroy()

# train menu for files to be deleted
def train_files_menu_delete_files_button():
    global delete_files_menu
    delete_files_menu = Toplevel(train_files_menu)
    delete_files_menu.geometry("400x400")

    button1 = tk.Button(delete_files_menu, text = "Delete files - manual check", command = lambda: delete_files_callfunc(1))
    button2 = tk.Button(delete_files_menu, text = "Delete files - auto check", command = lambda: delete_files_callfunc(0))
    button3 = tk.Button(delete_files_menu, text = "Go Back", command = lambda: go_back_button(delete_files_menu))

    button1.pack(pady = 5)
    button2.pack(pady = 10)
    button3.pack(pady = 90)

def delete_files_callfunc(manually):
    Train.train_files_delete(manually)
    task_done_message()
    delete_files_menu.destroy()



main_menu = tk.Tk()
main_menu.title("File Cleaner")
main_menu.geometry("400x400")

label1 = tk.Label(main_menu, text = "Main Menu")
label1.pack(pady= 5)

button1 = tk.Button(main_menu, text = "Train Files", command = main_menu_b1_train_files)
button2 = tk.Button(main_menu, text = "Exit", command = lambda: go_back_button(main_menu))
button1.pack(pady = 10)
button2.pack(pady = 90)


main_menu.mainloop()