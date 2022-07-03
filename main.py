from ntpath import join
import os
import shutil
import time

days = 30
path = ""
seconds = time.time() - (days * 24 * 60 * 60)

def checkIfPathExists(path):
    return os.path.exists(path)

def getItemAge(path):
    return os.stat(path).st_ctime

def removeFolder(folder):
    shutil.rmtree(folder)

def removeFile(file):
    os.remove(file)

path_exists = checkIfPathExists(path)

if path_exists == True:
    for item, folders, files in os.walk(path):
        for file in files:
            joined_file = os.path.join(item, file)
            age = getItemAge(joined_file)

            if seconds >= age:
                removeFile(joined_file)

        for folder in folders:
            joined_file = os.path.join(item, file)
            age = getItemAge(joined_file)

            if seconds >= age:
                removeFolder(joined_file)
else:
    print(path, " Does not exist")