#creating tuples
fruit = ('banana' ,'apple' ,'strawberry')
#printing tuples
print (fruit)
#accesing items in a tuple
print (fruit[1])
#slicing a tuple
print (fruit[0:2])
#loop through tuple
for i in fruit:
    print (i)
#unpacking a tuple
fruit1,fruit2,fruit3 = fruit
print (fruit1)
#packing a tuple
numbers = (1,2,3,4)
print (numbers)
#mixed tuple
stuff = (12,'red',3.7,True)
print (stuff)
#packing variables into a tuple
name = 'Yusuf'
age = 12
hobbie = 'scratch'
person = (name,age,hobbie)
print (person)