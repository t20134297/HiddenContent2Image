import cv2

def getInputContent():
    fp = open("input.txt",'r')
    content_list = fp.readline().split(" ")
    char_num = len(content_list)-1
    fp.close()
    return content_list[0:char_num],char_num

def HiddenSecret2Image(img_path,word_list,length,dst):
    img = cv2.imread(img_path)
    height,width,depth = img.shape
    num_per_row = width/6
    num_all = num_per_row * height - 1
    if num_all < (length+1):
        print ("You input too many words!")
        return 0
    rows_need = (length+1)/num_per_row + 1
    for i in range(rows_need):
        for j in range(width):
            for k in range(3):
                if img[i][j][k] % 2 == 1:
                    img[i][j][k] = img[i][j][k]-1

    length2str = format(length,'b')
    length_str = len(length2str)
    for i in range(length_str):
        img[0][i/3][i%3] = img[0][i/3][i%3] + int(length2str[length_str-1-i])

    for i in range(length):
        if (i+1) < num_per_row:
            numOfChar = len(word_list[i])
            for j in range(numOfChar):
                img[0][(i+1)*6+j/3][j%3] = img[0][(i+1)*6+j/3][j%3] + int(word_list[i][numOfChar-1-j])

        else:
            row = (i+1)/num_per_row
            numOfChar = len(word_list[i])
            for j in range(numOfChar):
                img[row][((i+1)%num_per_row)*6+j/3][j%3] = img[row][((i+1)%num_per_row)*6+j/3][j%3]+int(word_list[i][numOfChar-1-j])
    cv2.imwrite(dst,img)


def getSecretFromImage(img_path):
    fp = open("output.txt",'w')
    img = cv2.imread(img_path)
    height,width,depth = img.shape
    num_per_row = width/6
    binaryOfLength = ""
    for i in range(18):
        binaryOfLength = binaryOfLength + str(img[0][i/3][i%3]%2)
    binaryOfLength = binaryOfLength[::-1]
    numOfWord = int(binaryOfLength,2)

    for i in range(numOfWord):
        word=""
        if (i+1)<num_per_row:
            for j in range(18):
                word = word + str(img[0][(i+1)*6+j/3][j%3]%2)
            word = word[::-1]
            fp.write(word+" ")
        else:
            row = (i+1)/num_per_row
            for j in range(18):
                word = word + str(img[row][((i+1)%num_per_row)*6+j/3][j%3]%2)
            word = word[::-1]
            fp.write(word+" ")
    fp.close()




word_list,length = getInputContent()
print (length)
# HiddenSecret2Image("ManGod.png",word_list,length,"SecretMan.png")
# getSecretFromImage("SecretMan.png")
