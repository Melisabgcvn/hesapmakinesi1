import tkinter as tk

form=tk.Tk()
 #form isimli nesne oluşturuldu.
form.config(bg='#e0eeee')
#formun arka plan rengi ayarlandı.

form.title('Calculator')
form.geometry('250x320+1300+1')
#kod ekranıma göre formumu bilgisayarımın sağ köşesine sabitliyorum.Aynı zamanda formun boyutunu 250x320 olacak şekilde tanımladım.
form.resizable(False,False) 
#x ve y ekseninde form boyutunun değişmesini engelliyorum.

ifade=""
#boş bir string değişken tanımlandı.

def select_button(item):
    global ifade
    ifade=ifade+str(item)
    text_input.set(str(ifade))  
    

text_input =tk.StringVar()  
#input almak için nesne yaratıldı.
  
def Delete():
    #silme işlemi için fonksiyon oluşturuldu.
    global ifade
    ifade=""
    text_input.set("")


def error():
    try:
        global ifade
        total=str(eval(ifade))
        text_input.set(total)
        ifade=""
        
    except:
        text_input.set("error")
        ifade=""
        print("Error")
        
        
    


input_frame=tk.Frame(form).pack(side=tk.TOP)    
#giriş için frame oluşuturuldu.

input_field=tk.Frame(form).pack(side=tk.TOP)
#input_frame içindeki değeri alabilmek için bir frame daha oluşturuldu.

input_field=tk.Entry(input_frame,textvariable=text_input,width=20,font=('bold'))
input_field.place(x=30,y=60)

#son olarak butonlar için bir frame daha oluşturulacak.
buton_frame=tk.Frame(form).place(x=110,y=230)

#BUTTONS
one=tk.Button(buton_frame,text="1",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(1)).place(x=30,y=220)
two=tk.Button(buton_frame,text="2",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(2)).place(x=80,y=220)
three=tk.Button(buton_frame,text="3",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(3)).place(x=130,y=220)
four=tk.Button(buton_frame,text="4",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(4)).place(x=30,y=190)
five=tk.Button(buton_frame,text="5",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(5)).place(x=80,y=190)
six=tk.Button(buton_frame,text="6",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(6)).place(x=130,y=190)
seven=tk.Button(buton_frame,text="7",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(7)).place(x=30,y=160)
eight=tk.Button(buton_frame,text="8",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(8)).place(x=80,y=160)
nine=tk.Button(buton_frame,text="9",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(9)).place(x=130,y=160)
multiplication=tk.Button(buton_frame,text="*",width=1,height=1,bg='#e6e6fa',command= lambda: select_button("*")).place(x=180,y=190)
division=tk.Button(buton_frame,text="/",width=1,height=1,bg='#e6e6fa',command= lambda: select_button("/")).place(x=180,y=160)
minus=tk.Button(buton_frame,text="-",width=1,height=1,bg='#e6e6fa',command= lambda: select_button("-")).place(x=180,y=220)
plus=tk.Button(buton_frame,text="+",width=1,height=1,bg='#e6e6fa',command= lambda: select_button("+")).place(x=180,y=250)
point=tk.Button(buton_frame,text=" .",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(".")).place(x=80,y=250)
zero=tk.Button(buton_frame,text="0",width=1,height=1,bg='#e6e6fa',command= lambda: select_button(0)).place(x=30,y=250)
equal=tk.Button(buton_frame,text="=",width=1,height=1,bg='#e6e6fa',command= lambda: error()).place(x=130,y=250)
deleted=tk.Button(buton_frame,text="C",width=3,height=1,bg='#e6e6fa',command= lambda: Delete()).place(x=165,y=120)


form.mainloop() #formun açık halde durabilmesi için.



