import os
from datastructures import File, Directory
from constants import EXAMPLES, SWITCHES

class DTT:

    def __init__(self):
        pass

    def dir_to_list(self, path, switches):
        list_of_names = []
        for root, dirs, files in os.walk(path):
            if "f" not in switches:
                list_of_names.append(Directory(os.path.basename(root)))
            if "d" not in switches:
                for file in files:
                    if "e" in switches:
                        list_of_names.append(File(file))
                    else:
                        name, ext = self.separate_file_extension(file)
                        list_of_names.append(File(name))
        return list_of_names

    def list_to_txt(self, filename, l):
        with open(filename, "w", encoding="utf8") as f:
            for item in l:
                f.write(item.name)
                f.write("\n")

    def separate_file_extension(self, filename):
        name, extension = filename.strip().split(".")
        return name, extension


