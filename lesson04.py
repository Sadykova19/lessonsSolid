# Файлы чтение и запись

# file = open('text.txt','r')

# content = file.read()
# print(content)

# file.close()





# with open('text.txt', 'r') as file:
#     content = file.read()
    # print(content)


# with open('text.txt', 'a') as file:

#     content = file.write('Hello')

#     print(content)


# with open('text.txt', 'w') as file:
#     lines = ['Строка 1 ', ' Строка 2']
#     content = file.writelines(lines)
#     print(content)



# with open('text.txt', 'a') as file:
#     n = 2*2

#     content = file.write(str(n))

#     print(content)


# with open('text.txt', 'r') as file:

#     for l in file:
#         print(l)


with open('text.txt', 'r') as file:
    with open('copy.txt', 'w') as copy_file:
        copy_file.write(file.read())