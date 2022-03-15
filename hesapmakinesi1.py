import tkinter as tk

form=tk.Tk()
 #form isimli nesne oluşturuldu.
form.config(bg='#63b8ff')
#formun arka plan rengi ayarlandı.

form.title('Hesap Makinesi')
form.geometry('250x320+1300+1')
#kod ekranıma göre formumu bilgisayarımın sağ köşesine sabitliyorum.Aynı zamanda formun boyutunu 250x320 olacak şekilde tanımladım.
form.resizable(False,False) 
#x ve y ekseninde form boyutunun değişmesini engelliyorum.

ifade=""
#boş bir string değişken tanımlandı.

def butona_tıkla(item):
    global ifade
    ifade=ifade+str(item)
    text_giris.set(ifade)  
    

text_giris =tk.StringVar()  
#input almak için nesne yaratıldı.
  
def Sil():
    #silme işlemi için fonksiyon oluşturuldu.
    global ifade
    ifade=""
    text_giris.set("")

def bt_equal():
    global ifade
    result=str(eval(ifade)) 
    #en son gelen ifadeleri toparlamak için eval fonksiyonu kullanıldı.
    text_giris.set(result)
    ifade="" 
    
    


input_frame=tk.Frame(form).pack(side=tk.TOP)    
#giriş için frame oluşuturuldu.

input_field=tk.Frame(form).pack(side=tk.TOP)
#input_frame içindeki değeri alabilmek için bir frame daha oluşturuldu.

input_field=tk.Entry(input_frame,textvariable=text_giris,width=20,font=('bold'))
input_field.place(x=30,y=60)

#son olarak butonlar için bir frame daha oluşturulacak.
buton_frame=tk.Frame(form).place(x=110,y=230)

#BUTTONS
bir=tk.Button(buton_frame,text="1",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(1)).place(x=30,y=220)
iki=tk.Button(buton_frame,text="2",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(2)).place(x=80,y=220)
uç=tk.Button(buton_frame,text="3",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(3)).place(x=130,y=220)
dort=tk.Button(buton_frame,text="4",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(4)).place(x=30,y=190)
bes=tk.Button(buton_frame,text="5",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(5)).place(x=80,y=190)
alti=tk.Button(buton_frame,text="6",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(6)).place(x=130,y=190)
yedi=tk.Button(buton_frame,text="7",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(7)).place(x=30,y=160)
sekiz=tk.Button(buton_frame,text="8",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(8)).place(x=80,y=160)
dokuz=tk.Button(buton_frame,text="9",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(9)).place(x=130,y=160)
carp=tk.Button(buton_frame,text="*",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla("*")).place(x=180,y=190)
bol=tk.Button(buton_frame,text="/",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla("/")).place(x=180,y=160)
cikar=tk.Button(buton_frame,text="-",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla("-")).place(x=180,y=220)
topla=tk.Button(buton_frame,text="+",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla("+")).place(x=180,y=250)
nokta=tk.Button(buton_frame,text=" .",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(".")).place(x=80,y=250)
sifir=tk.Button(buton_frame,text="0",width=1,height=1,bg='#87ceff',command= lambda: butona_tıkla(0)).place(x=30,y=250)
esit=tk.Button(buton_frame,text="=",width=1,height=1,bg='#87ceff',command= lambda: bt_equal()).place(x=130,y=250)
sil=tk.Button(buton_frame,text="C",width=3,height=1,bg='#87ceff',command= lambda: Sil()).place(x=165,y=120)


form.mainloop() #formun açık halde durabilmesi için.



