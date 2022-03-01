import os
from datastructures import File, Directory
from constants import EXAMPLES, SWITCHES

class DTT:

    def __init__(self):
        pass

    def dir_to_list(self, path, switches):
        list_of_names = []
        unique_list = []
        indentation = "---"
        for root, dirs, files in os.walk(path):
            # i - checks whether format is required
            if "i" in switches:
                length = len(root.strip().split(os.sep)) - 1
            # f - files only, directories are ignored
            if "f" not in switches:
                dir_name = os.path.basename(root)
                if "u" in switches:
                    if dir_name not in unique_list:
                        unique_list.append(dir_name)
                        # i - checks whether format is required
                        if "i" in switches:
                            list_of_names.append(indentation * length)
                        list_of_names.append(Directory(dir_name))
                else:
                    # i - checks whether format is required
                    if "i" in switches:
                        list_of_names.append(indentation * length)
                    list_of_names.append(Directory(dir_name))
            # d - directories only, files are ignored
            if "d" not in switches:
                for file in files:
                    # i - checks whether format is required
                    if "i" in switches:
                        list_of_names.append(indentation * (length + 1))
                    # e - file extensions are required
                    if "e" in switches:
                        if "u" in switches:
                            if file not in unique_list:
                                unique_list.append(file)
                                list_of_names.append(File(file))
                        else:
                            list_of_names.append(File(file))
                    else:
                        name, ext = self.separate_file_extension(file)
                        if "u" in switches:
                            if name not in unique_list:
                                unique_list.append(name)
                                list_of_names.append(File(name))
                        else:
                            list_of_names.append(File(name))
        if "a" in switches and "i" not in switches:
            return sorted(list_of_names)
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
        extension = ""
        i = 1
        symbol = filename[-i]
        while symbol != ".":
            extension += symbol
            i += 1
            symbol = filename[-i]
        name = filename[:len(filename) - i]
        return name, extension



