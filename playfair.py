import numpy as np

#generate metrix
key = "playfearcypher"
alpha = "abcdefghijklmnopqrstuvwxyz"
code = []
for element in key +alpha:
       if element == "j" or element == "i":
              element = "i"
       if element not in code:
              code.append(element)
code_arr = np.array(code).reshape((5,5))

print("5x5 Key Metrix :")
print(code_arr)

def loc_(el, in_data):
       if code.index(el) <= 4:
              i = 0
       elif code.index(el) <= 9:
              i = 1
       elif code.index(el) <= 14:
              i = 2
       elif code.index(el) <= 19:
              i = 3
       elif code.index(el) <= 24:
              i = 4
       j = code.index(el) % 5

       return i,j

def cyp(el1, el2):
       ax,ay = loc_(el1,code)
       bx,by = loc_(el2,code)

       if ax == bx:
              #in same row
              return code_arr[ax][int(ay+1) % 5], code_arr[bx][int(by+1) % 5]
       elif ay == by:
              #in same col
              return code_arr[int(ax+1) % 5][ay], code_arr[int(bx+1) % 5 ][by]
       else :
              
              return code_arr[ax][by],code_arr[bx][ay]

                 
text = "hello"
if len(text)%2==1:
       text +="x"

cypherT = ""
k=0
while k < len(text):
       out1 =""
       out2 =""
       out1, out2 = cyp(text[k],text[k+1])
       cypherT += out1+out2
       k+=2

print(cypherT)
       
