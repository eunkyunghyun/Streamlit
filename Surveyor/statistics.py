from glob import glob


def portion(*args):
    global flag
    rule = ""
    if flag == 1:
        rule = "성별: "
    elif flag == 2:
        rule = "학교: "
    elif flag == 3:
        rule = "학년: "
    elif flag == 4:
        rule = "성적: "
    elif flag == 5:
        rule = "과목: "
    elif flag == 6:
        rule = "기분: "
    result = []
    things = []
    for i in range(len(args[0])):
        if flag == 4:
            result.append(int(args[0][i].strip(rule).strip('\n')))
        else:
            result.append(args[0][i].strip(rule).strip('\n'))
    if flag == 4:
        print("성적: {}점".format(sum(result) / len(result)))
    else:
        for item in result:
            if item not in things:
                print("{}: {}%".format(item, result.count(item) / len(result) * 100))
                things.append(item)


files = glob("./people/*.txt", recursive=True)
lines = []

for file in files:
    f = open(file, 'r', encoding='utf8')
    lines.append(f.readlines())

for i in range(1, len(lines[0])):
    items = []
    for j in range(len(lines)):
        items.append(lines[j][i])
    flag = i
    portion(items)
