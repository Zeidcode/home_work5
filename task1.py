#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = "Some абв text абв text абв text some words"
my_list = text.split()
minus = "абв"   
for i in my_list:
    for j in range(len(i)):
        print(type(j))
        if i[j] == 'а' and i[j+1] == 'б' and i[j+2] == 'в':
            my_list.remove(i)
print(my_list) 