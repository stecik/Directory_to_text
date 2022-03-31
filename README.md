# Directory to Text (DTT)
Simple CLI program which generates .txt file with a list of all files and subdirectories of given directory.

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
### Optional switches
```
-f, --filesonly - Returns only names of files
-d, --dirsonly - Returns only names of directorie
-u, --unique - Duplicit names are included only once (if combined with -e ignores file types)
-e, --extension - Include file extensions in filenames
```
### Mutually exclusive switches
```
-i", --indent - Returns formated list with indentation
-s", --sort - Returns alphanumerically sorted list
```
### Switches that require input
```
-D --directory - Specify target directory
-L, --length - Specify depth of a search
```
### Mutually exclusive switches that require input
```
-E, --exclude - Excludes specified file extensions - separate by ';' [-E jpg;png]
-I, --include - Includes only specified file extensions - separate by ';' [-I jpg;png]
```
### Help
```
-h, --help - Show help message
```

## How to install
### Windows
#### Option 1 (Python 3 required)
1. Download repository
2. Delete folder exe_files (only required for option 2)
3. Open cmd
4. Navigate to folder dtt (cd path)
5. Run command python dtt.py [-h] [-D] [-f] [-d] [-u] [-e] [-L] [-i | -s] [-E EXCLUDE | -I INCLUDE] output_file
#### Option 2 (Python 3 not required)
1. Download repository
2. Delete folder DTT_files (only required for option 1)
3. Navigate to C:\Users\%username%\AppData\Local
4. Create folder DTT and copy dtt.exe (DTT\exe_files\Windows\dtt.exe)
5. If using any antivirus program, add dtt.exe as an exception (might not be necessary)
6. Add C:\Users\%username%\AppData\Local\DTT\dtt.exe to PATH (system environment variable)
7. Open cmd
8. Run command dtt [-h] [-D] [-f] [-d] [-u] [-e] [-L] [-i | -s] [-E EXCLUDE | -I INCLUDE] output_file

### Linux
#### Option 1 (Python 3 required)
1. Download repository
2. Delete folder exe_files
3. Open terminal
4. Navigate to folder dtt (cd path)
5. Run command python dtt.py [-h] [-D] [-f] [-d] [-u] [-e] [-L] [-i | -s] [-E EXCLUDE | -I INCLUDE] output_file
## Licence
Feel free to use/edit my software in any way possible for **_non-commercial_** purposes.
