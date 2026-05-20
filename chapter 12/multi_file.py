with (
    open("file1.txt","a+")as f1,        # a+ for file read and write
    open("file2.txt","+a")as f2
):
    f1.write("my name is aaditya\n")
    f1.seek(0)      # This is important
    print(f1.read())

    f2.write("Im in class 11th\n")
    f2.seek(0)
    print(f2.read())