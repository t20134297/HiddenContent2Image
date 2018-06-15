def input_content(content):
    fp = open("input.txt",'w')
    for ch in content:
        num = ord(ch)
        bin_num = format(num,'b')
        fp.write(bin_num + " ")
    fp.close()

def get_content():
    fp = open('output.txt','r')
    content_list = fp.readline().split(" ")
    length = len(content_list)
    content=""
    for i in range(length-1):
        num = int(content_list[i],2)
        content = content+chr(num)
    fp.close()
    print (content)
    return content

# input_content("这个人是智障，大家不要理他！")
get_content()
