with open('data.txt') as f:
    lines = f.readlines()

with open('col1.txt','w') as f:
    for line in lines:
        if 'local' in line or 'datagrams' in line:
            continue

        index = 0
        index_charC = line.find('c')
        index = line.find('-')
        line = line[index+1:index_charC - 2]
        f.write(line +'\n')

with open('col2.txt','w') as f:
    for line in lines:
        if 'local' in line or 'datagrams' in line:
            continue

        index_charM = 0
        if "KBytes" in line:
            index_charM = line.find('KBytes') + 8
        elif "MBytes" in line: 
            index_charM = line.find('MBytes') + 8
        elif 'Bytes' in line:
            index_charM = line.find('Bytes') + 7

        line = line[index_charM : index_charM + 5]
        f.write(line +'\n')
