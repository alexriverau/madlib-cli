def welcome():
    print(f'''

******Welcome to Mad Libs!******

- Input the specific type of word asked on each of the prompts.
- Once you're finished read and enjoy!
''')
# welcome()


def game(file):

    user_inputs = []
    content = read_template(file)
    pieces = parse_template(content)




def read_template(str):

    with open(str, 'r') as file:
        try:
            contents = file.read()
            return contents
        except FileNotFoundError as error:
            print(error, "This file does not exist")


def parse_template():
    pass


# with open('test.txt') as file:
#     for word in file:
#         for char in word:
#             print(char)


# new_list = ['sweet', 'juicy', 'orange']
#
# content = 'It was a {} and {} {}.'.format(*new_list)
#
# print(content)








