file = open('input.txt', 'r')
unique_names = dict()

for line in file:
    first_name = line.split(' ', 1 )[0]

    # Removes Pages 4 lines of Footnote
    if first_name == 'CONSULTE':
        for i in range(4):
            next(file)
            
    if first_name in unique_names:
        unique_names[first_name] += 1
    elif '@' in first_name:
        next(file)
    else:
        unique_names[first_name] = 1

counter = 0
for k, v in unique_names.items():
    print (k + " " + str(v))
    counter += 1

print ("\n"+  "Total " + str(counter))
