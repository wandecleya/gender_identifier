def isValidName(name):
    if '@' in name:
        return False
    elif any(not(letter.isalpha() or "'") for letter in name):
        return False
    elif len(name) < 3:
        return False
    else:
        return True

def removeFootnote(name):
    if name == 'CONSULTE':
        for i in range(4):
            next(full_list)


full_list = open('input.txt', 'r')
unique_names = dict()

for line in full_list:
    first_name = line.split(' ', 1 )[0]

    # Removes Pages 4 lines of Footnote
    removeFootnote(first_name)

    if isValidName(first_name):
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
