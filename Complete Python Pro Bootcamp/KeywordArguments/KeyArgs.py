#Created by Shlomi Kiko
#Goal: Practice *args
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import Playground as play

# play.add(1, 2, 3, 4, 5)


# #Pass a list as an example
# l = (1 ,2 ,3 , 4)


# play.test(l)


#Keyword arguments example
play.arithmethic(add=2, multiply=4)

##Class test with keyword arguments
aircraft1 = play.Aircraft(type='Helicopter', name='Apache')
print(f'Name aircraft1: {aircraft1.name}, type: {aircraft1.type}')

aircraft2 = play.Aircraft(type='Plane', name='F16')
print(f'Name aircraft2: {aircraft2.name}, type: {aircraft2.type}')