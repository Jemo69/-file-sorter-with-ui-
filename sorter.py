import shutil
import os
from list import * 

def sorter( dir_path : str = '.' ):
    print("file sorter has started")
    os.chdir(rf"{dir_path}")
    for file_type in list_of_files_types:
        is_exists = os.path.exists(file_type)
        if not is_exists:
            os.mkdir(file_type)
    list_of_in_dir  : list[str] = os.listdir()
    list_of_files : list[str] = []
    for file in list_of_in_dir:
        if os.path.isfile(file):
            list_of_files.append(file)

    print(list_of_files)
    for file_index in range(len(list_of_files)):

        file = list_of_files[file_index]
        file_type = file.split(".")[-1]
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            shutil.move(file, os.path.join("pictures", file))
        elif file.endswith(".mp4"):
            shutil.move(file, os.path.join("videos", file))
        elif file.endswith(".mp3") or file.endswith(".wav"):
            shutil.move(file, os.path.join("music", file))
        elif file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".docx"):
            shutil.move(file, os.path.join("documents", file))
        elif file.endswith(".rom"):
            shutil.move(file, os.path.join("roms", file))
        elif  file_type in code_type_list:
            shutil.move(file, os.path.join("code", file))
        elif file_type in application_type_list:
            shutil.move(file, os.path.join("applications", file))
        elif file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z"):
            shutil.move(file, os.path.join("archive", file))
        else:
            shutil.move(file, os.path.join("other", file))



if __name__ == "__main__":
   main()
