from typing import ItemsView


List = []
Tuple = ()
Set = {}
Dictionaries = {"name":"John"}

List
> Mutable collections of Items
> Allow Duplicate Elements
> Element can be of different datatypes


>>> cars = ['Audi','BMW','Merc']
>>> type(cars)
<class 'list'>
>>> cars[0]
'Audi'
>>> cars[1]
'BMW'
>>> cars[-1]
'Merc'
>>> cars.append('Volvo')
>>> cars
['Audi', 'BMW', 'Merc', 'Volvo']
>>> cars.extend(['Sokada','MG'])
>>> cars
['Audi', 'BMW', 'Merc', 'Volvo', 'Sokada', 'MG']
>>> cars.insert(0,'Kia')
>>> cars
['Kia', 'Audi', 'BMW', 'Merc', 'Volvo', 'Sokada', 'MG']
>>> cars[1:2]
['Audi']
>>> cars[1:3]
['Audi', 'BMW']
>>> cars[::2]
['Kia', 'BMW', 'Volvo', 'MG']
>>> cars[:2]
['Kia', 'Audi']
>>> cars[2:]
['BMW', 'Merc', 'Volvo', 'Sokada', 'MG']
>>> cars[::2]
['Kia', 'BMW', 'Volvo', 'MG']
>>> cars[::3]
['Kia', 'Merc', 'MG']
>>> cars.remove('Sokada')
>>> cars
['Kia', 'Audi', 'BMW', 'Merc', 'Volvo', 'MG']
>>> cars.index('Merc')
3
>>> cars.reverse()
>>> cars
['MG', 'Volvo', 'Merc', 'BMW', 'Audi', 'Kia']
>>> cars.sort()
>>> cars
['Audi', 'BMW', 'Kia', 'MG', 'Merc', 'Volvo']
>>> 


Tuple
> immutable
> ordered collaction
> fixeds

fruits = ("Apple","Orange","Mango")
>>> fruits = ("Apple","Orange","Mango")
>>> type(fruits)
<class 'tuple'>
>>> fruits[1]
'Orange'
>>> fruits[1:]
('Orange', 'Mango')
>>> fruits[:1]
('Apple',)
>>> fruits1= ("Banana","KIWI")
>>> fruits + fruits1
('Apple', 'Orange', 'Mango', 'Banana', 'KIWI')
>>> 

Set
>> Mutable
>> Unique


>>> mySet
{1, 2, 3, 4, 5, 6, 7}
>>> mySet.remove(2)
>>> mySet
{1, 3, 4, 5, 6, 7}
>>> mySet.remove(2)
>>> mySet.discard(2)
>>> mySet.pop()
1
>>> mySet.clear()
>>> mySet
set()
>>> set1 = {1,2,3}
>>> set2 = {3,4,5}
>>> print(set1 | set2)
{1, 2, 3, 4, 5}
>>> print(set1 & set2)
{3}
>>> set2 = {1,1,3,4,5}
>>> set2
{1, 3, 4, 5}


Dictionaries
key-value pairs

>>> my_dict = {"name":"Alice","age":25}'
>>> my_dict = {"name":"Alice","age":25}
>>> my_dict['age']
25
>>> my_dict['city']= "Delhi"
>>> my_dict
{'name': 'Alice', 'age': 25, 'city': 'Delhi'}
>>> my_dict={("x","y"):5}
>>> my_dict[("x","y")]
5

user = {
    'name':'John',
    'age':30,
    'address':{
        'city':'Delhi',
        'country':'India'
    }
}


user = {
    'name':'John',
    'age':30,
    'address':{
        'city':'Delhi',
        'country':'India'
    },
    'age':40
}

>>> user['name']
'John'
>>> user['address']['city']
'Delhi'
>>> 