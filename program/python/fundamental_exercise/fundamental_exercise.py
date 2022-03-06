'''
list_example = ['apple','banana','cherry']


print(list_example)

list_example.append('orange')
print(list_example)

list2_example = list_example[:]
list2_example.append('watermelon')
print(list_example)
print(list2_example)


set_example = set(list_example)
set2_example = set_example
set_example.remove('apple')
print(len(set_example))
print(len(set_example))
# set_example.remove('bbb')
set_example.discard('aaa')
print(len(set_example))

set_example.update(set2_example)

x = {'a':1,'b':2,'c':3}
print(x)
print(x.values())
for a in x.values():
	print(a)

x['d'] = 4
x.popitem()
print(x)


a = 200
b = 66
print("A") if a > b else print("B")



def myfunc(n):
	return lambda a : a*n;
	
mydoubler = myfunc(2)
print(mydoubler(11))

'''


'''
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	def __init__(self, name, age, level):
		#Person.__init__(self, name, age)
		super().__init__(name, age)
		self.level = level
		
a = Student('Alice', 10, 3)

print(a.name)
print(a.age)
print(a.level)
'''


'''
class Person:
	def __init__(self, name, age):
		self.name = named
		self.age = age
		
class Student(Person):
	def __init__(self, name, age):
		super().__init__(name, age)
'''
'''
class IterTest:
	def __iter__(self):
		self.a = 2
		return self
	
	def __next__(self):
		self.a += 3
		return self.a
		
myIter = IterTest()
it = iter(myIter)

print(next(it))
print(next(it))
print(next(it))
'''
'''
import mymodule

mymodule.moduleFunction('Alice')
'''


'''
import datetime

time = datetime.datetime.now()
print(time)
print(time.year)
print(time.strftime("%A"))
print(time.strftime("%b"))
print(time.strftime("%B"))
'''



'''
import json

x = '{"name":"Bill", "age":12, "city":"London"}'
y = json.loads(x)
print(y["age"])

a = {"name":"Bill", "age":12, "city":"London"}
b = json.dumps(a)
print(b)

print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''


import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent = 4))

