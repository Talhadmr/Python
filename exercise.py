"""
text = "the goal is turn data into information, and information into insight."

text = text.replace(","," ")
text = text.replace("."," ")
text = text.split()

lst = []
for i in text :
    lst.append(i.upper())

print(lst)
"""

"""
lst = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

len = len(lst)
print(len)

print(lst[0],lst[10])

p = []
for i in range(4):
    p.append(lst[i])
print(p)

lst.pop(8)
print(lst)

lst.append(':')


lst.insert(8, 'N')
print(lst)


dict = {'Christian': ['America', 18],
         'daisy': ['England', 12],
         'Antonio': ['spain', 20],
         'Dante': ['Italy', 22]}
dict.values()
dict.keys()
dict['daisy'] = ['England', 13]
dict.values()
dict.update({'ahmet': ['Turkiye', 24]})

dict.pop('Antonio')
print(dict)

"""

"""
even_list = []
odd_list = []
def func(lst):
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return (even_list, odd_list)

lst = [12, 13, 14, 15]
print(func(lst))

"""

"""
lst = ['Furkan', 'Zeynep', 'Berk', 'Aleyna', 'Tuna', 'Halime']

for index, i in enumerate(lst, 1):
    if index <= 3:
        print(f"{index}. öğrenci {lst[index-1]} Mühendislik fakültesinde okumaktadır")
    else:
        print(f"{index}. öğrenci {lst[index-1]} tıp fakültesinde okumaktadır")

"""