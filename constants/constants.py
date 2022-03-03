PROGRAM_NAME = "Directory to Text"
PROGRAM_SHORTCUT = "dtt"
DESCRIPTION = "Write directory structure into .txt file"
DEFAULT_BEHAVIOUR = "Returns unformated .txt file with a list of all filenames and subdirectories including files inside them starting from given directory"
EXAMPLES = [r"dtt input_directory(default = current directory) output_file.txt switches(-id) depth(default = 0)",
                    r"dtt list.txt -f 3",
                    r"dtt C:\Users\directory list.txt -id",
                    r"dtt list.txt",
                    "dtt -help"
            ]
SWITCHES = ["-d = Return only names of directorie",
            "-f = Return only names of all files",
            "-i = Return formated list",
            "-e = Do not include file extensions in filenames",
            "-u = Duplicit names are included only once (if combined with -e ignores file types)",
            "-a = Ignore specified file extensions",
            "-b = Return only specified file extensions"]

INDENTATION_SYMBOL = "---"