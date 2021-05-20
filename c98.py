def countwords():
    filename = input("enter the file name: ")
    numberofwords = 0
    file = open(filename, "r")
    for line in file:
        words = line.split()
        numberofwords += len(words)
    print(numberofwords)

countwords()
