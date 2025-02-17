# import pickle
#
# Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000}
# Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000}
#
# db = {}
# db['Omkar'] = Omkar
# db['Jagdish'] = Jagdish
#
# b = pickle.dumps(db)
# print(b)
# print(type(b))
#
# print(pickle.loads(b))
# print(type(pickle.loads(b)))


f1 = open('pickle-file.txt', 'rb')
x = f1.read()
print(x)
print(type(x))

y = f1.read(-1)
print(y)
print(type(y))

f1.close()