def day1():
    f = open("input.txt", "r")
    input = f.readlines()
    i = 0
    elves = {}
    elves[0] = 0
    max = [0,0,0]
    for line in input:
        if line.strip() != "":
            elves[i] += int(line.strip())
        else:
            if elves[i] > min(max):
                max.pop(max.index(min(max)))
                max.append(elves[i])
            i += 1
            elves[i] = 0
    if elves[i] > min(max):
        max.pop(max.index(min(max)))
        max.append(elves[i])
    print(max(elves))
    print(sum(max))


def day2():
    f = open("input.txt", "r")
    input = f.readlines()
    i = 0
    totalscore = 0
    drawpairs = {"A":"X","B":"Y","C":"Z"}
    winpairs = {"A":"Y","B":"Z","C":"X"}
    losepairs = {"A":"Z","B":"X","C":"Y"}
    pointvalues = {"X":1,"Y":2,"Z":3}
    for line in input:
        '''
        if drawpairs[line[0]] == line.rstrip()[-1]:
            totalscore += 3 + pointvalues[line.rstrip()[-1]]
        elif winpairs[line[0]] == line.rstrip()[-1]:
            totalscore += 6 + pointvalues[line.rstrip()[-1]]
        elif losepairs[line[0]] == line.rstrip()[-1]:
            totalscore += pointvalues[line.rstrip()[-1]]
        else:
            print("somethings wrong")
        '''
        if line.rstrip()[-1] == "X":
            totalscore += pointvalues[losepairs[line[0]]]
        elif line.rstrip()[-1] == "Y":
            totalscore += pointvalues[drawpairs[line[0]]] + 3
        elif line.rstrip()[-1] == "Z":
            totalscore += pointvalues[winpairs[line[0]]] + 6

    print(totalscore)

