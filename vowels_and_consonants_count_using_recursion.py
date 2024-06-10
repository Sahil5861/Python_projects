def count_vowels_consonants(str, index=0, vowels_count=0, consonant_count=0):
    vowels = 'aeiou'
    if index == len(str):
        return vowels_count, consonant_count
    
    if str[index] in vowels:
        vowels_count +=1
    else:
        consonant_count +=1
    return count_vowels_consonants(str, index + 1, vowels_count, consonant_count)


string = input('Enter the string : ')
v, c = count_vowels_consonants(string)

print(v,c)


