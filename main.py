from dtt import DTT
from parser import args

if __name__ == "__main__":
    dtt = DTT()
    l = dtt.dir_to_list(args.directory, args)
    dtt.list_to_txt(args.output_file, l)