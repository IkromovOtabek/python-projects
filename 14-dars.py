from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title('My project')
oyna.geometry('300x300')

# Foydalanuvchidan yil kiritishni so'raymiz
yil_label = Label(oyna, text="Tug'ilgan yilingiz:")
yil_label.place(x=75, y=20, width=150, height=20)

yil = Entry(oyna)
yil.place(x=75, y=50, width=150, height=30)

# Natijani ko'rsatish uchun Label yaratish
natija = Label(oyna, text="Natija", bg="white")
natija.place(x=90, y=135, width=120, height=40)

def farq():
    try:
        # Yilni olish
        yil_kiritilgan = int(yil.get())  # Entrydan foydalanuvchi kiritgan yilni olish
        bugun = datetime.today()
        # Natijani hisoblash va natija Labelda ko'rsatish
        natija.config(text=f"Yosh: {bugun.year - yil_kiritilgan}")
    except ValueError:
        # Agar foydalanuvchi raqam kiritmasa yoki noto'g'ri yil kiritsa, xato xabari
        natija.config(text="Noto'g'ri yil!")

# Tugma yaratish va "Hisoblash" tugmasi bosilganda farq() funksiyasini chaqirish
tugma = Button(oyna, text="Hisoblash", command=farq)
tugma.place(x=90, y=90, width=120, height=40)

oyna.mainloop()
