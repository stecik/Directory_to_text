from d2t import D2T

if __name__ == "__main__":
    d2t = D2T()
    l = d2t.dir_to_list("test")
    d2t.list_to_txt("test.txt", l, "")
