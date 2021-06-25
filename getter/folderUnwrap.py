import shutil
import glob
import os

for dir in glob.iglob("./domain/*"):
    if (os.path.isdir(dir)==True):
        for path in glob.iglob(f"{dir}/*"):
            dest = shutil.move(path, "./domain/")
            print(f'moved:{path}')