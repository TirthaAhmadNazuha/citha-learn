# def isVocal(character = str):
#     if
#     return True if character.lower() in 'a i u e o' else False
    
# print(isVocal('A'))

list1 = ['citha', 'ahmad', 'pauzi']
list2 = ['tirtha', 'ahmad', 'nazuha']
list3 = ['hafis', 'ahmad', 'ibrahim']

gabung = list1 + list2 + list3

utama = [
    { 'nama': 'Tirtha' },
    { 'nama': 'Citha' },
    { 'nama': 'Hafiz' },
]

tambahan = [
    { 'nama_panjang': 'Tirtha ahmad nazuha' },
    { 'nama_panjang': 'Citha ahmad pauzi' },
    { 'nama_panjang': 'Hafiz ahmad ibrahim' },
]

result = []

index = 0 
while index < len(utama):
    result.append(dict(utama[index], **tambahan[index]))
    index += 1 

def findUser(keyword):
    for r in result:
        if keyword in r['nama_panjang']: return r

def toCapitalize(text):
    return ' '.join(list(map(lambda word: word.capitalize(), text.split(' '))))

print(toCapitalize('tirtha ahmad nazuha'))
print(toCapitalize('citha ahmad pauzi'))
print(toCapitalize('hafiz ahmad ibrahim'))