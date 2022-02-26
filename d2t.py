import os
from datastructures import File, Directory

class D2T:

    def __init__(self):
        pass

    def dir_to_list(self, path):
        list_of_names = []
        for root, dirs, files in os.walk(path):
            list_of_names.append(Directory(os.path.basename(root)))
            for file in files:
                list_of_names.append(File(file))
        return list_of_names

    def list_to_txt(self, filename, l, switches=""):
        with open(filename, "w", encoding="utf8") as f:
            if not switches:
                for item in l:
                    f.write(item.name)
                    f.write("\n")

