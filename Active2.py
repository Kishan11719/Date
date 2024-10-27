
my_dict = {}

#dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

#dictionary with mixed keys
my_dict = {'name': 'john' , 1: [2,4,3]}

my_dict = {'name': 'Jack','age': 26}

#Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['address'] = 'Downtown'
print(my_dict)

#remove particular element
my_dict.pop('age')
print(my_dict)