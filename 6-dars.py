#math moduli
#import math
#print(math.ceil(8.7))
#print(math.floor(8.7))
#print(math.sqrt(81))

#topshiriq istalgan son kiritib 
#misol uchun 234 soni kirtilsa javobi 2+3+4= "9" 
#javobini ciqaradigan dastur yasaymiz
a = int (input("uchxonali son kiriting: "))
b = a % 10
d = a // 100
c = (a % 100 ) // 10
f = b + d + c
print ("Raqamlar yig'indisi: {} ga teng ".format (f))
