def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b, a%b) 

p = int(input("Enter a Prime Number: "))
q = int(input("Enter a Second Prime Number: "))
while (p==q):
    print("Invalid number, Enter again (p!=q): ")
    q = int(input("Enter a Second Prime Number: "))
n = p*q
m = (p-1)*(q-1)

for e in range(2,m): 
    if gcd(e,m) == 1: 
        gcd(e,m)
        break
d = (e**(-1) % m)


print("Public Key: {" + str(e) + ", " + str(n) + "}")
print("Private Key: {" + str(d) + ", " + str(n) + "}")

message = int(input("Enter Text to Encrypt: "))
encrypted = (message**e % n)
print("Encrypted Message:",encrypted)

print(d,e,n)
decrypted = (encrypted**d % n)
print("Decrypted Message:",decrypted)