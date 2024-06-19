# deterine all numbers in a line of text
def getNumbers(s):
    number = []

    for i, charater in enumerate(s):
        if charater.isdigit():
            number.append(charater)

        for j, num in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if s[i:].startswith(num):
                number.append(str(j+1))
    
    num = number[0] + number[-1]
    return int(num)


def readFile(filename):
    file = open(filename, "r")

    sum = 0

    for line in file:
        sum += getNumbers(line)

    file.close()
    print(sum)


readFile("./input.txt")

