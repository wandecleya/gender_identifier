file = open("input.txt", "r")
unique_names = dict()

for line in file:
    first_name = line.split(' ', 1 )[0]
    if first_name in unique_names:
        unique_names[first_name] += 1
    else:
        unique_names[first_name] = 1

for k, v in unique_names.items():
	print (k + " " + str(v))
