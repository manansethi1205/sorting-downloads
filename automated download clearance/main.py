# to create a python script that reads through the downloads folder and sorts the file on 
# the basis of their types and adds them to the suitable folder 
# once the file has been added to the suitable folder we want to mark them as sorted so that
# no further operation is run on them 


import os
import shutil

# Function to copy file from downloads folder and send it to the desired folder
def copy_file(file, destination):
    try:
        shutil.copy(file, destination)
        dir_list_sorted.append(file)
    except FileNotFoundError as e:
        print(f"File not found: {file}")
    except Exception as e:
        print(f"Error copying file {file}: {e}")

path = "C:/Users/Manan Sethi/Downloads"
dir_list = os.listdir(path)
dir_list_sorted = []

for file in dir_list:  # to loop through each file in the downloads folder
    if file not in dir_list_sorted:
        full_file_path = os.path.join(path, file)

        if file.endswith(('.txt', '.docx', '.pdf')):
            destination_directory = "C:/Users/Manan Sethi/new_docs"
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory) #creates folder if it doesnt exist already
            copy_file(full_file_path, destination_directory)


        elif file.endswith((".jpg", ".png")):
            destination_directory = "C:/Users/Manan Sethi/new_img"
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            copy_file(full_file_path, destination_directory)


        elif file.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')):
            destination_directory = "C:/Users/Manan Sethi/new_vids"
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            copy_file(full_file_path, destination_directory)


