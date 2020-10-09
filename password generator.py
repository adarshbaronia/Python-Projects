
def password_generator(n):
    import math
    import random
    small='abcdefghijklmopqrstuvwxyz'
    upper='ABCDEFGHIJKLMOPQRSTUVWXYZ'
    num='0123456789'
    special='$#*!&@'
    
    small_choice=''.join(random.choices(small,k=math.ceil(n/4)))
    upper_choice=''.join(random.choices(upper,k=math.ceil(n/4)))
    num_choice=''.join(random.choices(num,k=math.ceil(n/4)))
    special_choice=''.join(random.choices(special,k=math.ceil(n/4)))
    
    password=''.join(random.sample(small_choice + upper_choice + num_choice + special_choice, k=n)) 
    #print(f"The genrated password of length {n}: ",password)
    return password


#decode

def password_decode():
    password=password_generator(int(input("Please enter password length: ")))
    print(f"The password of length {len(password)} converted in asterick",len(password)*"*")
    import string
    count=0
    decode=''
    for i in range(len(password)):
        if password[i] in string.ascii_letters:
            decode=decode+password[i]
            i+=1
            count+=1
        elif password[i] in string.digits:
            decode=decode+password[i]
            i+=1
            count+=1
        elif password[i] in string.punctuation:
            decode=decode+password[i]
            i+=1
            count+=1
        else:
            count+=1        
    print(f"The decoding of generated password took {count} iterations")
    return decode

print("Decoded password is: ",password_decode())

