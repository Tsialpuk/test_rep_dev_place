"""
1)	Есть список состоящий из слов и чисел,
нужно записать в файл сначала слова в порядке их длины, а после слов цифры в порядке возрастания.
"""
list1 = [10, 2, 3, 7, 'a', 'world', 'cat']
list2 = []
list3 = []
for i in list1:
    if type(i) == int:
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)
list2.sort()
list3.sort()
print(list2)
print(list3)
list4 = list3 + list2
print(list4)
string1 = str(list4)
with open('text_1.txt', 'w') as file:
    for element in string1:
        file.write(element)







