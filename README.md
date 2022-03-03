# Directory to Text (D2T)
**_WORK IN PROGRESS_** 
Simple CLI program (Windows only) which generates .txt file with a list of all files and subdirectories of given directory.

## Usage
```
dtt [-h] [-D] [-f] [-d] [-u] [-e] [-L] [-i | -s] [-E EXCLUDE | -I INCLUDE] output_file
```
```
dtt output.txt -D "C:\Users\directory" -fes -I mkv;avi -L 3
```

## Default behaviour

Returns ***unformated*** .txt file with a list of file names (***without file extensions***) and subdirectories including files inside them starting from ***current directory***
```
dtt output.txt
```

## Switches
```
-f, --filesonly - Returns only names of files
-d, --dirsonly - Returns only names of directorie
-u, --unique - Duplicit names are included only once (if combined with -e ignores file types)
-e, --extension - Include file extensions in filenames
```
```
-i", --indent - Returns formated list with indentation
-s", --sort - Returns alphanumerically sorted list
```
```
-D --directory - Specify target directory
-L, --length - Specify depth of a search
```
```
-E, --exclude - Excludes specified file extensions - separate by ';' [-E jpg;png]
-I, --include - Includes only specified file extensions - separate by ';' [-I jpg;png]
```
```
-h, --help - Show help message
```
## Requirements
Python 3

## How to install
lorem ipsum

## Licence
Feel free to use/edit my software in any way possible for **_non-commercial_** purposes.
