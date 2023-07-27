# # belajar class

# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         self.engine = False
    
#     def start(self):
#         self.engine = True
#         print('brom broom')
    
#     def shutDown(self):
#         self.engine = False

# myCar = Car('avanza', 'silver')
# print(f'myCar is {myCar.name} and \ncolor is {myCar.color}')

# myCar.start()
# print('Car engine is running' if myCar.engine else 'car engine is stop')

# myCar.shutDown()
# print('Car engine is running' if myCar.engine else 'car engine is stop')

class Motor:
    def __init__(self, name, color, merk, madeIn):
        self.name = name
        self.color = color 
        self.merk = merk 
        self.madeIn = madeIn
        self.engine = False

    def on(self):
        self.engine = True 
        print('emberrrrr berrr')

    def off(self):
        self.engine = False

motor1 = Motor('Scoopy', 'black', 'Honda', 'Japan')
print(f'motor citha is {motor1.name}\ncolor {motor1.color}\nmerk {motor1.merk}\nmade in {motor1.madeIn}')

motor1.on()
print('Motor Citha sedang berjalan' if motor1.engine else 'motor citha sedang berhenti')

motor1.off()
print('Motor Citha sedang berjalan' if motor1.engine else 'motor citha sedang berhenti')
print(10*"="+"PEMBATAS"+10*"=")


class Motor2T(Motor):
    def on(self):
        self.engine = True 
        print('tang tang tang tang')


motor1 = Motor2T('vespa', 'blue', 'Piagio', 'Italy')
print(f'motor Nazu is {motor1.name}\ncolor {motor1.color}\nmerk {motor1.merk}\nmade in {motor1.madeIn}')

motor1.on()
print('Motor Nazu sedang berjalan' if motor1.engine else 'motor Nazu sedang berhenti')

motor1.off()
print('Motor Nazu sedang berjalan' if motor1.engine else 'motor Nazu sedang berhenti')
print(10*"="+"PEMBATAS"+10*"=")
