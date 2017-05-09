full_list = open('input.txt', 'r')
unique_names = dict()

for line in full_list:
    first_name = line.split(' ', 1 )[0]

    # Removes Pages 4 lines of Footnote
    if first_name == 'CONSULTE':
        for i in range(4):
            next(full_list)

    #Removes emails mistaken by names
    if '@' in first_name:
        next(full_list)
    #Remove names with numbers
    elif any(not(letter.isalpha()) for letter in first_name):
        next(full_list)
    #Remove names with less than 3 letters
    elif len(first_name) < 3:
        next(full_list)

    if first_name in unique_names:
        unique_names[first_name] += 1
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
print total
result_file.write(total)


result_file.close
