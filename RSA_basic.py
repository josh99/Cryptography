def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

print("RSA implementation")
p = 9
q = 12
m = p*q
phi = (p-1)*(q-1)
e =coprimes(phi)[-1] #has to be co-prime with m
print("select e ")
print(coprimes(phi))
d = e % m
print("Key generated :"+str(d))

data = int(input("enter data to encrpt: "))

#encr
enc = data^e % m
print("encrypted data :"+str(enc))

#decrypt
print("decrypted data :"+ str(enc^d % m))

























