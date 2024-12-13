#-format()
#s=input('Ismingiz nima:')
#print('Salom {}'.format(s.capitalize()))
#-trancate long string

#-.capitalize() bu savol bergan payt bosh xarifni 
#kichik xarif bilan yozsanngizxam javob berayotganda 
#bosh xarifni katta xarif bilan javob beradi. 
#print(s.capitalize())

#Bu .casefold() es maitindagi barcha yozuvlarni kichkina qilib beradi.
#print(s.casefold())

#Bu len esa bita sozda newta soz yoki belhilar va prabel orninixam xisoblab beradgan koddur
#s='salom yaxwmsan tuzumsan  nma gapla'
#print(len(s))
#print(s[1]) # bu owa "salom" sozidagi 2chida turgan "a" xarifini bzga opchiqb korsatib beradi
#print(s[0:5]) #shunday korinishda yozsak "salom yozuvini chiqazinb korsatib beradi"

#bu cod esa kiritilgan soni teskari iqlib korsatib beradi
#s=input('Kiriting:')
#print(s.capitalize()[::-1])

#bu topshiriq karochi kiriting degan sorov otkazamza sorovga SALOM DUNYO deb yozganimizda kod 
#yozib DUNYO SALOM wunqa teskari qiladgasn kod yaratamiza

#a=input('Kiriting:')
#print(a[6:11],a[0:5])