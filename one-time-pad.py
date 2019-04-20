import numpy as np

alpha = "abcdefghijklmnopqrstuvwxyz"
ran_key = "jklmnhipqroabcgstuvdwxyzef"

def rand_key(data):
       new_key = ""
       for el in data:
              new_key += ran_key[alpha.index(el)]
       return new_key

text = input("enter the text Message >>" )

print("key :",rand_key(text))

a = list(text)
b = list(rand_key(text))
c = ""

#encypt

for i in range(0,len(a)):
       val_i = alpha.index(a[i])
       val_k = alpha.index(b[i])
       c +=alpha[int(val_i + val_k) % 26]
print("cypher text : ",c)

#decrypt
d=""
for i in range(0,len(c)):
       val_i = alpha.index(c[i])
       val_k = alpha.index(b[i])
       d +=alpha[int(val_i - val_k) % 26]
print("decode text : ",d)
