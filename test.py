import math

def check_if_prime(test_number, k=1):
    while True:
        k+=1
        root_number = int(math.sqrt(test_number)) + 1
        
        
        if test_number == 1 or test_number%k==0 and k <= root_number:
            try:
                test_number = int(input(f"\nthe number {test_number} is not prime, enter another number: "))
                break
            except ValueError:
                print("you must enter a valid integer")
                continue
        
        elif k > root_number:
            return test_number        

def check_if_modul(e,fi,p,q):
    while True:
        if math.gcd(e,fi) == 1 and e < fi and e != p and e != q:
            return e
        else:
            try:
                e = int(input(f"\nthe number e:{e} is not coprime with fi:{fi} or is more than fi, and is equal to p or q \nenter another number for e: "))
            except ValueError:
                print("you must enter a valid integer")
                continue

def private_key_formula(e,fi,n,k=0):
    while True:
        k+=1
        d = (fi*k+1) % e
        d_check = (fi*k+1) // e

        if d == 0 and d_check != n:
            print(f"\nthe amount of incrementation was: {k}")
            d = (fi*k+1) // e
            return d
        
        else:
            continue
            
def formula():
    while True:
        try:
            full_number = input(f"enter the numbers for p and q with the divider being \",\": ")
            p,q = full_number.split(",")
            break
        except ValueError:
            print("you must enter two numbers separated by a comma example: 5,7")
            continue
        

    p = int(p)
    q = int(q)
    
    p = check_if_prime(p)
    q = check_if_prime(q)

    n = p*q
    fi = (p-1)*(q-1)

    print(f"\nthe number of fi is: {fi}")
    
    while True:
        try:
            e = int(input(f"enter the numbers of e: "))
            break
        except ValueError:
            print("you must enter a valid integer")
            continue
    

    e = check_if_modul(e,fi,p,q)
    d = private_key_formula(e,fi,n)
    
    return (e,n),(d,n)

def message_verify(n):
    while True:
        try:
            message = int(input(f"\nenter the message to be encrypted: "))
            if message < 0 or message >= n:
                print(f"the message must be a non-negative integer and less than {n}")
                continue
            break
        except ValueError:
            print("the message must be an integer")
            continue
    return message




public_key,private_key = formula()

print (f"\nthe private key is: {private_key}")
print (f"\nthe public key is: {public_key}")

message = message_verify(public_key[1])
encrypted = message ** public_key[0] % public_key[1]
decrypted = encrypted ** private_key[0] % private_key[1]

print(f"\nthe encrypted message is: {encrypted}")

print(f"\nthe decrypted message is: {decrypted}")