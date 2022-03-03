from dtt import DTT
from parser import args

if __name__ == "__main__":
    dtt = DTT()
    # "D:\Sdílené disky\Filmy a seriály\Filmy"
    # l = dtt.dir_to_list(args.directory, args)
    l = dtt.dir_to_list("D:\Sdílené disky\Filmy a seriály\Filmy", args)
    dtt.list_to_txt("test.txt", l)