#son=1
#while son <=32:
#	print(son)
#	son=son+1

#promokod yasash
#from random import randint
#yangi_kod=randint(130,135)
#print(yangi_kod)


#bu kodimizxam randomli promokod
# bolib faqtgina ozgartirganimiz 135,132,134 shu 
#sonlar chiqmasin  degan dasturdir


#from random import randint
#kodlar=[135,132,134]
#yangi_kod=randint(130,135)

#i=0
#while yangi_kod in kodlar:
#	i+=1
#	yangi_kod=randint(130,135)
#
#print('Takrorlanish soni:', i)
#print(yangi_kod)

#topshiriq 
#a=input('Xoxlagan raqamingizni kiriting:')
#while a:
#	if a.isdigit():
#		print('raxmat')
#		break
#	else:
#		a=input('Qaytadan urinning:')

#from random import choice
#print("Mini O'yinga Xush Kelibsiz\nBitta meva o'ylang/o'yalagandan so'ng xa harfini🤔 yozing")
#a = input("Tayyormisiz: ")

#mevalar = list(("olma","anor","banan","nok"))
#rand = choice(mevalar).capitalize()

#if a == "xa":
#	print("Siz o'yalagan meva {}".format(rand))
#else:
#	print('Ming afsus')

#q = input("To'g'rimi: ha/yoq ")

#if q == "xa":
#	print("Topdim !!!")
#elif q =='yoq':
#    print('Ming afsus')
#else:
#	print("Iltomos ha yoki yoq deb javob bering")


from random import choice

print("Mini O'yinga Xush Kelibsiz\nBitta meva o'ylang/o'yalagandan so'ng 'xa' harfini🤔 yozing")
a = input("Tayyormisiz: ")

# Agar foydalanuvchi 'yoq' deb javob bersa, dastur yakunlanadi
if a == "yoq":
    print("Dastur yakunlandi.")
else:
    mevalar = list(("olma", "anor", "banan", "nok"))
    rand = choice(mevalar).capitalize()

    if a == "xa":
        print("Siz o'yalagan meva {}".format(rand))
    else:
        print('Ming afsus')

    q = input("To'g'rimi: xa/yoq ")

    if q == "xa":
        print("Topdim !!!")
    elif q == "yoq":
        print('Ming afsus')
    else:
        print("Iltimos, 'ha' yoki 'yoq' deb javob bering.")



