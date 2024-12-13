#summa=input('Summani kirting:')

#if summa.isdigit() and int(summa)> 0 and int(summa) < 1000000:
#	print('Tashakur!')
#else:
#	print('Limitdan ortiq mumkun emas!')

#ism=input('Ismingizni kiriting:')
#fam=input('Familyangizni kirtirng:')

#@if ism or fam:
#	print('Tashakur!')
#else:
 #   print('Ism yoki Familyangizni kirting:')	

#son = input('1 dan 30 gacha bolgan sonni kirting:')
#if son.isdigit():
 #	son=int(son)
 #	if son > 0 and son < 30:
 #		qoldiq = son % 10
 #		letter =''
 #		if son > 9 and son < 20:
 #			letter='on '
 #		if son > 19 and son < 30:
 #		    letter='yigirma '	
 #		
 #		if qoldiq == 1:
 #		    letter +='bir'
 #		if qoldiq==2:
# 		    letter +='ikki'
 ##		if qoldiq==3:
 #		    letter +='uch'
 #		if qoldiq==4:
 #		    letter +='tor'
 #		if qoldiq==5:
 #		    letter +='besh'
 #		if qoldiq==6:
 #		    letter +='olti'
 #		if qoldiq==7:
 #		    letter +='yetti'
 #		if qoldiq==8:
 #		    letter +='sakkiz'
 #		if qoldiq==9:
 #		    letter +='toqqiz'
 #		if qoldiq==10:
# 		    letter +='on'

 #		print(letter) 
 #	else:
# 		print('1 dan 30 gacha bolgan sonni kirtishungiz kerak!')
#else:
# 	    print('son kiritish kerak')	   

xarif=input('A dan Ng gacha bolgan xarifni kiriting:')
unli1 = 'a'
unli2 = 'o'
unli3 = 'e' 
unli4 = 'i'
unli5 = 'u'
unli6 = 'o`'
if xarif.isalpha():
	if unli1==xarif or unli2==xarif or unli3==xarif or unli4==xarif or unli5==xarif or unli6==xarif:
		print('Kiritilgan {} harfingiz unlidir.'.format(xarif))
	else:
	    print('Kiritilgan {} harfingiz undoshdir!'.format(xarif))
else:
    print('Harif kiriting!!!')    	



























