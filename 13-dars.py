#davlat = {'davlat':'Ozbekiston','poytaxt':'Toshkent','til':'uzbek'}
#print(davlat)
#print(type(davlat))

#print(davlat['davlat'], '-', davlat['poytaxt'])

#davlat2 = dict()
#davlat2['davlat']='AQSH'
#davlat2['poytaxt']='Vashington'
#print(davlat2['poytaxt'])

#davlat2.update({'davlat': '*','poytaxt':'Toshkent'})
#print(davlat2)

#dv=input('Davlat kodini kiriting:')
#davlatlar={
#	'UZ':{
#	     "name":"Uzbekistan",
#	     "capital": "Tashkent",
#	     "language":[
#	            'uz',
#	            'ru',
#	            'en'
#	            ]
#	},
#	'RU':{
#	     "name":"Russia",
#	     "capital":"Moscow",
#	     "language":[
#	            'ru',
#	            'en',
#	            'ur'
#	            ]
#	}
#}

#natija = davlatlar.get(dv,False)
#if natija:
#    print('Poytaxt:',natija['capital'])
#else:
#	print('Bunday malumot yoq!')


hh=input('Qaysi davlatda, qanday til borligini bilmoqchimisiz?Unda til kodini kiriting:')
davlatlar={
	'UZ':{
	     "name":"Uzbekistan",
	     "capital": "Tashkent",
	     "language":[
	            'uz',
	            'ru',
	            'en'
	            ]
	},
	'RU':{
	     "name":"Russia",
	     "capital":"Moscow",
	     "language":[
	            'ru',
	            'en',
	            'ur'
	            ]
	}

}

hh = davlatlar.items()

for key, val, in hh:
	if dv in val['languages'] :
		print(val["name"])








































