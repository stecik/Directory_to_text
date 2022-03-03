import os
from constants import INDENTATION_SYMBOL

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
            # filesonly - files only, directories are ignored
            if not switches.filesonly:
                # Gets directory name
                dir_name = os.path.basename(root)
                list_of_names = self._add_to_list(dir_name, list_of_names, switches, length)
            # dirsonly - directories only, files are ignored
            if not switches.dirsonly:
                for file in files:
                    # Compare depth with required depth
                    if switches.length > 0 and length == switches.length:
                        break
                    filename, ext = self._separate_file_extension(file)
                    if self._check_exclude_include(switches, ext):
                        continue
                    # extension - file extensions are required
                    if switches.extension:
                        # validate included and excluded extensions
                        filename = file
                    list_of_names = self._add_to_list(filename, list_of_names, switches, length+1)

        # sort - list is sorted aphanumerically
        if switches.sort:
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
        if filename.startswith(".") or "." not in filename:
            return filename, None

        extension = ""
        i = 1
        symbol = filename[-i]
        while symbol != ".":
            extension += symbol
            i += 1
            symbol = filename[-i]
        name = filename[:len(filename) - i]
        return name, extension[::-1]


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
        # unique - check whether uniqueness is required
        if switches.unique:
            if name not in l:
                l = self._check_format(name, l, switches, length)
        else:
            l = self._check_format(name, l, switches, length)
        return l


    def _check_format(self, name, l, switches, length):
        # indent - checks whether format is required
        if switches.indent:
            l.append(INDENTATION_SYMBOL * length)
        l.append(name)
        return l


    def _check_exclude_include(self, switches, ext):
        if switches.exclude and ext:
            if ext not in switches.exclude:
                return False
            else:
                return True
        elif switches.include and ext:
            if ext in switches.include:
                return False
            else:
                return True
        return None