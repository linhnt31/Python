with open('text.txt') as f:
    lines = f.readlines()

with open('col1.txt','w') as f:
    for line in lines:
        index = 0
        index_charC = line.index('c')
        for k, v in enumerate(line):
            if v == '-':
                index = k
        line = line[index+1:index_charC - 2]
        f.write(line +'\n')

with open('col2.txt','w') as f:
    for line in lines:
        index_charC = line.index('c') + 15
        index_charM = 0
        ans = line.split(' ')
        line = str(ans[len(ans) - 2])

        f.write(line +'\n')
