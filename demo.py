full_path = 'demo' + '.txt'
file = open(full_path, encoding='UTF-8')

for i in range(1,101,1):
    output = ("这是第" + str(i) + "行.\n")
    file.write(output)


