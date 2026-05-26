#File Organizer
import os   #interact with system(files/folders)
import shutil   #move files
path="testing_folder"
files=os.listdir(path)
print(files)

if not os.path.exists(path + "/Images"):
    os.mkdir(path+"/Images")

if not os.path.exists(path+"/Documents"):
    os.mkdir(path+"/Documents")

if not os.path.exists(path+"/Videos"):
    os.mkdir(path+"/Videos")
    
only_files = [f for f in files if not os.path.isdir(path + "/" + f)]
if not only_files:
    print("No files to organize")

for file in files:
    if os.path.isdir(path + "/" + file):
        continue

    ext = os.path.splitext(file)[1]
    print("Processing:", file)

    if ext in [".jpg", ".png"]:
        print("Moving to Images")
        shutil.move(path + "/" + file, path + "/Images/" + file)
    elif ext in [".pdf", ".txt"]:
        print("Moving to Documents")
        shutil.move(path + "/" + file, path + "/Documents/" + file)
    elif ext in [".mp4"]:
        print("Moving to Videos")
        shutil.move(path + "/" + file, path + "/Videos/" + file)
        







#os.path.splitext(file) ----> splits file name into ("image",".jpg")             
    # [1] ---> gives extension
    
