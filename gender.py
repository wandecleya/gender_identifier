full_list = open('input.txt', 'r')
unique_names = dict()

for line in full_list:
    first_name = line.split(' ', 1 )[0]

    # Removes Pages 4 lines of Footnote
    if first_name == 'CONSULTE':
        for i in range(4):
            next(full_list)

    if first_name in unique_names:
        unique_names[first_name] += 1
    elif '@' in first_name:
        next(full_list)
    else:
        unique_names[first_name] = 1

full_list.close()

result_file = open("unique_names_list.txt", 'w')

counter = 0
for k, v in unique_names.items():
    result_line = (k + " " + str(v) + "\n")
    result_file.write(result_line);
    counter += 1

total = ("\n Total: " + str(counter))
result_file.write(total)

result_file.close
