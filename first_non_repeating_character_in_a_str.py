# first non repeating character in a str:

string = input('Enter a string !!')

def first_char(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    
    for char in char_count:
        if char_count[char] == 1:
            return char

result = first_char(string)
if result:
    print(f'The character is : {result}')
else:
    print(f'There is no any character !!')

