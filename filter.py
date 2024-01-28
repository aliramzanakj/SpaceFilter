file = open("muslimMatch-withcount.txt",'r')
lines = file.readlines()
word = ""
for line in lines:
    line = line.strip()
    for i in line:
        if i==" ":
            index =line.index(i)
            word =line[index:]
    new_file = open("password.txt",'a+')
    new_file.write(word.strip()+"\n")
    new_file.close()        
