vards = input('Ievadi vārdu: ')

with open('name.txt', 'w') as f:
    f.write(vards + '\n')