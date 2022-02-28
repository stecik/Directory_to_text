# Directory to Text (D2T)
WORK IN PROGRESS --- Simple CLI program which generates .txt file with a list of all files and subdirectories of given directory.

# Example commands
dtt input_directory(default = current directory) output_file.txt switches(-id) depth(default = 0)",
dtt list.txt -f 3
dtt C:\Users\directory list.txt -id
dtt list.txt

# Default behaviour
Returns unformated .txt file with a list of all filenames and subdirectories including files inside them starting from given directory

# Switches
-g = Ignore files in subdirectories
-d = Return only names of directorie
-f = Return only names of all files
-i = Return formated list
-e = Do not include file extensions in filenames
-u = Duplicit names are included only once (if combined with -e ignores file types)
-a = Ignore specified file extensions
-b = Return only specified file extensions

# Requirements
lorem ipsum

# How to install
lorem ipsum

# Licence
Feel free to use/edit my software in any way possible for non-commercial purposes. No need to include my name.
