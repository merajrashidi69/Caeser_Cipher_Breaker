

#caeser-cipher decryptor

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            #1                       #25

def decrypt(word,key): #function will test every key (25 possible keys)
    result = ''
    for i in word:
        if i.isupper(): #uppercase letters
            index = upper_letters.index(i)
            index -= key
            result += upper_letters[index]

        elif i.islower(): #lowercase letters
            index = lower_letters.index(i)
            index -= key
            result += lower_letters[index]


        if i == ' ':
            result += i


    return result #return final result



caeser_cipher = input('Enter the password: ')

key = 0
for i in range(0,25):
    key += 1
    tested = decrypt(caeser_cipher,key)
    print(f'Key #{key}: {tested}')

        
            
    
    
    
