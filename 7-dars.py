#til=input('Tilni tanlang uz/en?')

#if til=='uz':
#	print("Assalomu aleykom")

#elif til=='en':
#	print("Hello")
#else:
#    print("uz/en lardan birini tanlang")	

#random dastur yaratamiz

#from random import randint

#a=randint(1,500)
#b=randint(1,500)

#c=int(input('{}+{}='.format(a,b)))

#if c == (a + b):
#	print('Togri javob')
#else:
#	print('Xato!')

a = int(input("Yilni kiriting! ==> "))

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Kiritgan yilingiz kabisa yili ")
else:
    print("Kiritgan yilibgiz kabisa yili emas")
