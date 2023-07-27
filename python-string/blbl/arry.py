coffees = [
    {
        'name': 'Arabica',
        'taste': 'Nutty Flavours',
        'temp': '15-24°C',
        'local': 'Gayo, Flores, Banjawa'
    },
    {
        'name': 'Robusta',
        'taste': 'Whiskey',
        'temp': '21-24°C',
        'local': 'Lampung, Malang, Jawa'
    },
    {
        'name': 'Liberica',
        'taste': 'Chocolatey',
        'temp': ' 18-28°C',
        'local': 'Africa, Gana, Kongo'
    }
] 
target = 'Robustas'
for coffe in coffees:
    if target in coffe['name']:
        print(coffe)
    elif target[:5] in coffe['name']:
        print(coffe)