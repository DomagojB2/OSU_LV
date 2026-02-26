rijecnik = {}
fhand = open("song.txt")
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        rijec = word.lower()
        if rijec in rijecnik:
            rijecnik[rijec] +=1
        else:
            rijecnik[rijec] =1
fhand.close()
for rijec in rijecnik:
    if rijecnik[rijec]==1:
        print(rijec)