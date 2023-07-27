file = open('files/tes.txt', 'r')
lines = file.readlines()
results = []
for line in lines:
    result = line.split(',')
    for i, data in enumerate(result):
        print(i, data)
        if data.startswith('"') and data.endswith('"'):
            result[i] = data[1:-1]
        else:
            result[i] = int(data)

    results.append(result)

print(results)

file.close()