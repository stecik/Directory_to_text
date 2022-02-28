from dtt import DTT

if __name__ == "__main__":
    dtt = DTT()
    l = dtt.dir_to_list("test", "ie")
    dtt.list_to_txt("test.txt", l)
