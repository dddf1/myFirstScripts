import hashlib
import os

unique = dict()
path = "c:/test/"

for filename in os.listdir(path):
    full_path = path+filename

    if os.path.isfile(full_path):
        filehash = hashlib.md5(open(full_path, 'rb').read()).hexdigest()

        if filehash not in unique:
            unique[filehash] = filename
        else:
            print("file : " + filename + " is a duplicate of " + unique[filehash])

print("------ and we done ! ---------")