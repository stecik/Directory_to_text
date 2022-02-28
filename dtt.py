import os
from datastructures import File, Directory
from constants import EXAMPLES, SWITCHES

class DTT:

    def __init__(self):
        pass

    def dir_to_list(self, path, switches):
        list_of_names = []
        indentation = "---"
        for root, dirs, files in os.walk(path):
            # i - checks whether format is required
            if "i" in switches:
                length = len(root.strip().split(os.sep)) - 1
            # f - files only, directories are ignored
            if "f" not in switches:
                 # i - checks whether format is required
                 if "i" in switches:
                     list_of_names.append(indentation*length)
                 list_of_names.append(Directory(os.path.basename(root)))
            # d - directories only, files are ignored
            if "d" not in switches:
                for file in files:
                    # i - checks whether format is required
                    if "i" in switches:
                        list_of_names.append(indentation * (length + 1))
                    # e - file extensions are required
                    if "e" in switches:
                        list_of_names.append(File(file))
                    else:
                        name, ext = self.separate_file_extension(file)
                        list_of_names.append(File(name))
        # if "u" in switches:
        #     unique_values = list(set(list_of_names))
        #     unique_list = []
        #     for item in list_of_names:
        #         if item in unique_values:
        #             unique_list.append(item)
        #             index = unique_values.index(item)
        #             del unique_values[index]
        #     return unique_list
        return list_of_names

    def list_to_txt(self, filename, l):
        with open(filename, "w", encoding="utf8") as f:
            for item in l:
                if type(item) == type("-"):
                    f.write(item)
                else:
                    f.write(item.name)
                    f.write("\n")

    def separate_file_extension(self, filename):
        name, extension = filename.strip().split(".")
        return name, extension


