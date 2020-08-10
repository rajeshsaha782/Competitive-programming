from os import listdir
from os.path import isfile, join, isdir

ignore = set(['.git','.idea','venv','__pycache__'])

def get_all_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
    
def get_all_dirs(path):
    onlydirs = [join(path, f) for f in listdir(path) if isdir(join(path, f)) and f not in ignore]
    return onlydirs

def file_count(path,file_type=None,count=0):
    files = get_all_files(path)
    for f in files:
        if file_type is None or f.lower().endswith(file_type):
            print(join(path, f))
            count = count + 1
    
    sub_dirs = get_all_dirs(path)
    for d in sub_dirs:
        # print(count)
        count = file_count(d,file_type,count)
    return count
    
    

if __name__ == '__main__':
    print(file_count('E:\Projects\BitMascot',file_type='.java'))