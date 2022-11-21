'''
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}
'''

#1
set_a.update(set_b, set_c)
print(set_a)

#2
set_a.difference(set_b)

set_b.difference(set_c)

set_a.difference(set_c)

#3
set_a.intersection_update(set_b)
print(set_a)

set_b.intersection_update(set_c)
print(set_b)

set_a.intersection_update(set_c)
print(set_a)

#4
set = {1, 2}
set_a.isdisjoint(set)
False
set_b.isdisjoint(set)
True
set_c.isdisjoint(set)
True

#5
res = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
list_a  = []
for i in res:
    if i %2 != 0:
        list_a.append(i)
res_a = set(list_a)
print(res_a)

res = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
list_b = []
for i in res:
    if i %2 == 0:
        list_b.append(i)
res_2 = set(list_b)
print(res_2)

'''
dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}
dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}
dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}
'''
#1
dict_a.update(dict_b)
print(dict_a)

#2
res = dict(zip(dict_a.keys(), dict_b.values()))

#3
res = dict(zip(dict_b.values(), dict_a.keys()))

#4
'''
res = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5',
       'key_6': 'value_6', 'key_7': 'value_7', 'key_8': 'value_8', 'key_9': 'value_9', 'key_10': 'value_10'}
'''
res_a = {}
for key, value in res.items():
    a = int(key.split('_')[-1])
    if a % 2 != 0:
        res_a.update({key: value})
print(res_a)

#5
set_a = set(dict_a.items())
set_b = set(dict_b.items())
set_c = set(dict_c.items())
res = {
    'dict_a': len(set_a & set_c),
    'dict_b': len(set_b & set_c)
}
print(res)

