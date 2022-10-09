print(f'''

******Welcome to our Mad Libs game!******

- Input the specific type of word asked on each of the prompts.
- Once you're finished read and enjoy!
''')

# with open('test.txt') as file:
#     for word in file:
#         for char in word:
#             print(char)


new_list = ['sweet', 'juicy', 'orange']

content = 'It was a {} and {} {}.'.format(*new_list)

print(content)








