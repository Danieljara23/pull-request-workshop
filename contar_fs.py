
def contar_fs(word):
    return word.count('F')

def contar_car(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count


print(contar_fs('FffffffffFC', 'f'))
print(contar_fs('FffffffffFC', 'c'))
print(contar_fs('FffffffffFC', 'F'))