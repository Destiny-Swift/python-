alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


message = input('Enter message: ')
stepper = int(input('Enter Stepper: '))

result = ''

def encoder(message):
    result = ''
    for i in message:
        if i.lower() in list(alphabet_dict.keys()):
            position = alphabet_dict[i.lower()]
            step = stepper + position
            while step > 26:
                step -= 26
            if (i.isupper()):
               result += letters_list[step - 1].upper()
            else:
                result += letters_list[step - 1]
        else:
            result += i  
    print('\t\t', result)
    
     
def decoder(message):
    result = ''''''
    for i in message:
        if i.lower() in list(alphabet_dict.keys()):
            position = alphabet_dict[i.lower()]
            step = position - stepper
            while step < 1:
                step += 26
            if (i.isupper()):
               result += letters_list[step - 1].upper()
            else:
                result += letters_list[step - 1]
        else:
            result += i  
    print('\t\t', result, '\n')

encoder(message)
