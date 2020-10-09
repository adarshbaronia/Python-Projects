
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
    return password

print(password_generator(10))
