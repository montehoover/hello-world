import yaml
import os

# List all files recursively
def get_files(path):
    files = []
    for item in os.listdir(path):
        path_to_item = os.path.join(path, item)
        if os.path.isfile(path_to_item):
            files = files + [path_to_item]
        else:
            files = files + get_files(path_to_item)
    return files

dir = "data"
full_path = os.path.join(os.getcwd(), dir)
# I'm working with a particular directory structure where I know the first level is all
# directories and I want to capture their names.
dirs = os.listdir(full_path)
names = [None] * len(dirs)
for dir in dirs:
    # I expect the name of the dir to be a number and I want to use that number later
    try:
        dir_num = int(dir)
        path_to_dir = os.path.join(full_path, dir)
        if os.path.isdir(path_to_dir):
            for file in os.listdir(path_to_dir):
                path_to_file = os.path.join(path_to_dir, file)
                if os.path.isfile(path_to_file):
                    with open(path_to_file) as f:
                        d = yaml.safe_load(f)
                        names[dir_num] = d['name']
    except(ValueError) as e:
        print("I'm expecting the name of each directory to be a number but instead got: ", e)

with open("names.txt", 'w') as f:
    for name in names:
        print(name, file=f)
