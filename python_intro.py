print('Hello, Django girls!')
if 3 > 2:
    print('It works')
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('is not greater than 2')
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else: 
    print('Hey anonymous!')
volume = 57
if volume < 20:
    print('It´s kind quiet.')
elif 20 <= volume < 40:
    print('It´s nice for background music')
elif 40 <= volume < 60:
    print('Perfect, I can hear all the details')
elif 60 <= volume <80:
    print('Nice for parties')
elif 80 <= volume <100:
    print('A bit loud!')
else:
    print('Me duelen las orejas!:(')

# Cambiar el volumen si está muy alto o bajo

if volume < 20 or volume > 80:
    volume = 50
    print('Mucho mejor!')

def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi2 (name):
    if name == 'Ola':
        print('Hi Ola')
    elif name == 'Sonja':
        print('Hi Sonja') 
    else:
        print('Hi anonymous!')
hi2('linda')

def hi3(name):
    print('Hi' + name + '!')
hi3('Rachel')

# Lista de chicas

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi3(name)
    print('Next girl')

for i in range(1, 6):
    print(i)




    



