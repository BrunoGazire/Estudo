planets = ['1 Mercury', '2 Venus', '3 Earth', '4 Mars', '5 Exit the program']
txt = ['mercurio.txt',]
for planet in planets:
    print(planet)
user_input = input("Please enter you option: ")
if user_input == planets[0]:
    info = open('mercurio.txt', 'r')
    print(info.readable())
    print(info.read())
    info.close()
else:
    print("ok")




