# print('yo')
# num = input('write ')
# print(type (num))
# print(num)
# for i in num:
#     print(type (i))

# while - цикл

# i = 1

# while(i <= 5):
#     print(i)
#     i += 1


# password = ''

# while(password != '1234'):
#     password = input("write password")
# print('access')
    

# text = 'react'

# print(text[0])
# print(text[-1])
# print(len(text))
# print(text.lower())
# print(text.upper())

# text2 = '12345'
# print(text2.isdigit())

# new_text = text.replace('c','t')
# print(new_text)

# print(text[0:3])

# print('tt' in new_text)

# login = input('write login ')
# if(login.isdigit()):
#     print('login doesnt has to be only with numbers')
# elif(len(login) > 5):
#     print('too long login')
# else:
#     print('norm')

# for i in range(3):
#     for j in range(5):
#         print(i,j)

# for i in range(3):
#     for j in range(5):
#         for k in range(7):
#             print(i,j,k)

# квадрат короч
# for i in range(4):
#     for j in range(6):
#         print('*',end='')
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print('*',end='')
#     print()

# num = ''
# while(num != '0'):
#     num = input('write ')

# stroka = input('write ')
# nums = 0
# words = 0
# for i in stroka:
#     if(i.isdigit()):
#         nums += 1
#     else:
#         words += 1
# print(nums)
# print(words)

# for i in range(1,7):
#     for j in range(i):
#         print('*',end='')
#     print()

# list / array
# array = [1,'nice',3.14,True]

# array.append('dd') # add to end
# array.insert(2,10) # add to index insert(index,add)
# array.pop() # delete from end
# array.remove(3) # delete by index/name/stroke
# print(len(array))
# print(array)

# num = [1,2,3,454,4]
# for numb in num:
#     print(num)

# laun = ['python','c++','java']

# for i in laun:
#     print(i.upper())
#     # for j in i:
#     #     print(j)
# for i in laun:
#     print(len(i))

# upper_lang = []
# for i in laun:
#     print(i.upper())
# print(upper_lang)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[2][1] == matrix[-1][1])

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# counter = 0
# for i in matrix:
#     for j in i:
#         counter += j

# print(counter)

# 1.
# num = input('write ')
# if(num.isalpha()):
#     print('write number')
# else:
#     if(int(num) % 3 == 0):
#         print('делится на 3 без остатка')
#     elif(int(num) % 15 == 0):
#         print('делится на 15 без остатка')
#     elif(int(num) % 5 == 0):
#         print('делится на 5 без остатка')
#     else:
#         print('число не на что не делится')


# 2.
# num = 0
# while(int(num) >= 0):
#     num = input('write ')

# 3.
# text = input('write ')
# num = 0
# word = 0
# space = 0
# for i in text:
#     if(i.isdigit()):
#         num += 1
#     elif(i.isalpha()):
#         word += 1
#     elif(i.isspace()):
#         space += 1

# print(num)
# print(word)
# print(space)

# 4.
# array = [3,7,2,9,4,8,2]
# odd = 0
# sum = 0
# for i in array:
#     sum += i
#     if(i % 2 == 0):
#         odd += 1
    
# print(odd)
# print(sum)

# 5.
matrix = [
    [1,2,3],
    [4,5,6],
    [+8,9]
]
counter = 0


# for i in matrix:
#     for j in i:
#         counter += 1

# for i in matrix:
#     for j in i:
#         col += matrix[j][i]
col = 0
for i in matrix:
    for j in i:
        col += j
    print(col)

# print(counter)