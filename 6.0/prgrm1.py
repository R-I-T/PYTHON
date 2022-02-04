def file_read(filename):
    with open(filename) as f:
        content_list=f.readlines()
        print(content_list)
        print(len(content_list))



file_read("text.txt")
