from dtt_class import DTT
from parser import args

if __name__ == "__main__":
    dtt = DTT()
    # Creates a list of files and subdirectories
    l = dtt.dir_to_list(args.directory, args)
    # Creates a .txt file with the list
    dtt.list_to_txt(args.output_file, l)