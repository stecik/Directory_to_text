import os
from constants import EXAMPLES, SWITCHES, INDENTATION_SYMBOL

class DTT:

    def dir_to_list(self, path, switches):
        list_of_names = []
        root_length = self._get_root_length(path)

        # Walks through every subdirectory and file and adds them to list_of_names
        # if they pass conditions specified in switches
        for root, dirs, files in os.walk(path):
            # Depth of current directory
            # Used for format
            length = len(root.strip().split(os.sep)) - root_length
            # f - files only, directories are ignored
            if "f" not in switches:
                # Gets directory name
                dir_name = os.path.basename(root)
                list_of_names = self._add_to_list(dir_name, list_of_names, switches, length)
            # d - directories only, files are ignored
            if "d" not in switches:
                for file in files:
                    # e - file extensions are required
                    if "e" not in switches:
                        filename, ext = self._separate_file_extension(file)
                    else:
                        filename = file
                    list_of_names = self._add_to_list(filename, list_of_names, switches, length+1)
        # a - list is sorted aphanumerically
        if "a" in switches and "i" not in switches:
            return sorted(list_of_names)
        return list_of_names


    def list_to_txt(self, filename, l):
        # Writes each item of given list to a new line of filename.txt file
        with open(filename, "w", encoding="utf8") as f:
            for item in l:
                f.write(item)
                if self._check_item(item):
                    f.write("\n")


    def _separate_file_extension(self, filename):
        # Returns separated filename and file extension
        extension = ""
        i = 1
        symbol = filename[-i]
        while symbol != ".":
            extension += symbol
            i += 1
            symbol = filename[-i]
        name = filename[:len(filename) - i]
        return name, extension


    def _check_item(self, filename):
        # Checks if item is not INDENTATION_SYMBOL
        for symbol in filename:
            if symbol not in INDENTATION_SYMBOL:
                return True
        return False


    def _get_root_length(self, root):
        base = os.path.basename(root)
        path_split = root.strip().split(os.sep)
        length = 0
        for dir in path_split:
            length += 1
            if base == dir:
                return length


    def _add_to_list(self, name, l, switches, length):
        # u - check whether uniqueness is required
        if "u" in switches:
            if name not in l:
                l = self._check_format(name, l, switches, length)
        else:
            l = self._check_format(name, l, switches, length)
        return l


    def _check_format(self, name, l, switches, length):
        # i - checks whether format is required
        if "i" in switches:
            l.append(INDENTATION_SYMBOL * length)
        l.append(name)
        return l




