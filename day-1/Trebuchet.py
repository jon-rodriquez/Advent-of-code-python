# read file line by line


# deterine all numbers in a line of text
def getNumbers(s):
    number = []

    for charater in s:
        if charater.isdigit():
            number.append(charater)
    
    num = number[0] + number[len(number)-1]
    return int(num)


def readFile(filename):
    file = open(filename, "r")

    sum = 0

    for line in file:
        sum += getNumbers(line)



    file.close()
    print(sum)


readFile("./input.txt")
