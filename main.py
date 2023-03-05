from tkinter import *    

   
def flat(array):
       res = "" 
       for item in array:
              res = res + item
       return res      

def len_list(param):
    return len(list(param))

global input;
global symbols;

input = []
symbols = ["+","-","*","/"]
def handle_1():
      if check():
          input.append("1")
          label.config(text=flat(input).replace("*","x")) 
          
def handle_2():
      if check():
          input.append("2")
          label.config(text=flat(input).replace("*","x")) 
          
def handle_3():
      if check():
          input.append("3")
          label.config(text=flat(input).replace("*","x")) 
          
def handle_4():
      if check():
          input.append("4")
          label.config(text=flat(input).replace("*","x")) 
          
def handle_5():
      if check():
          input.append("5")
          label.config(text=flat(input).replace("*","x")) 

def handle_6():
      if check():
          input.append("6")
          label.config(text=flat(input).replace("*","x")) 

def handle_7():
      if check():
          input.append("7")
          label.config(text=flat(input).replace("*","x")) 

def handle_8():
      if check():
          input.append("8")
          label.config(text=flat(input).replace("*","x")) 

def handle_9():
      if check():
          input.append("9")
          label.config(text=flat(input).replace("*","x")) 

def handle_0():
      if check():
          input.append("0")
          label.config(text=flat(input).replace("*","x")) 
          
def handle_plus():
    if check() and not input[len(input)-1] in symbols and not input[len(input)-1] == "(":
        input.append("+")
        label.config(text=flat(input).replace("*","x"))
def handle_minus():
    if check() and not input[len(input)-1] in symbols and not input[len(input)-1] == "(":
        input.append("-")
        label.config(text=flat(input).replace("*","x"))
def handle_multiply():
    if check() and not input[len(input)-1] in symbols and not input[len(input)-1] == "(":
        input.append("*")
        label.config(text=flat(input).replace("*","x"))
def handle_divide():
    if check() and not input[len(input)-1] in symbols and not input[len(input)-1] == "(":
        input.append("/")
        label.config(text=flat(input).replace("*","x"))
def handle_open_paranthesis(): # 3(
    if check():
        if not input[len(input)-1] in ["*","("]:
            input.append("*")
        input.append("(")
        label.config(text=flat(input).replace("*","x"))
def handle_close_paranthesis():
    if check() and len_list(filter(lambda x: x == ")",input)) < len_list(filter(lambda x: x == "(",input)) and not input[len(input)-1] in symbols and not input[len(input)-1] == "(":
        input.append(")")
        label.config(text=flat(input).replace("*","x"))
def handle_equals():
    if len(input) == 0:
        return
    if not len_list(filter(lambda x: x == "(",input)) == len_list(filter(lambda x: x == ")",input)):
        while not len_list(filter(lambda x: x == "(",input)) == len_list(filter(lambda x: x == ")",input)):
            input.append(")")
            label.config(text=flat(input))
       # errorMsg.config(text="AÇIK PARANTEZ SAYILARI İLE KAPALI \nPARANTEZ SAYISI BİRBİRİ İLE UYUŞMUYOR!")
       # errorMsg.grid()
       # errorMsg.after(2000,resetErrorMsg)
        return
    try:
        label.config(text=eval(flat(input)))
        input.clear()
    except:
        label.config(text="Error")
        return
def btn_geri():
       try:
         input.pop()
         label.config(text=flat(input))
       except:
         return;

def btn_sil():
    input.clear()
    label.config(text="")
    
def check():
       def cb():
              resetErrorMsg()
       if(len(input)+1 == 31):
          errorMsg.config(text="MAKSİMUM KARAKTER SAYISINA ERİŞİLDİ (30)",bg="#EA2027")
          errorMsg.grid()
          errorMsg.after(2000,cb)
          return False
       else:
          return True 

def resetErrorMsg():
       errorMsg.config(text="",bg="#EA2027")
       errorMsg.grid_remove()
root = Tk()
root.title("Hesap Makinesi")
root.geometry("300x300")

root.config(bg="#5352ed") ##5352ed

errorMsg = Label(root,relief=FLAT,text="",bg="#EA2027",height=8,width=38)
errorMsg.grid(padx=950,pady=200)
errorMsg.grid_remove()


label = Label(root,bd=10,relief=GROOVE,width=60,text="")
label.place(height=100,width=300,x=500,y=20)


geri = Button(root,relief=FLAT,text="<-- Geri",bg="#5f27cd",activebackground="#5f27cd",command=btn_geri)
geri.place(height=50,width=125,x=800,y=70)

sil = Button(root,relief=FLAT,text="Hepsini Sil",bg="#5f27cd",activebackground="#5f27cd",command=btn_sil)
sil.place(height=50,width=125,x=950,y=70)

button_1 = Button(root,relief=FLAT,bg="white",text="1",command=handle_1)
button_1.place(height=50,width=80,x=500,y=200)

button_2 = Button(root,relief=FLAT,bg="white",text="2",command=handle_2)
button_2.place(height=50,width=80,x=610,y=200)

button_3 = Button(root,relief=FLAT,bg="white",text="3",command=handle_3)
button_3.place(height=50,width=80,x=720,y=200)

button_4 = Button(root,relief=FLAT,bg="white",text="4",command=handle_4)
button_4.place(height=50,width=80,x=500,y=275)

button_5 = Button(root,relief=FLAT,bg="white",text="5",command=handle_5)
button_5.place(height=50,width=80,x=610,y=275)

button_6 = Button(root,relief=FLAT,bg="white",text="6",command=handle_6)
button_6.place(height=50,width=80,x=720,y=275)

button_7 = Button(root,relief=FLAT,bg="white",text="7",command=handle_7)
button_7.place(height=50,width=80,x=500,y=350)

button_8 = Button(root,relief=FLAT,bg="white",text="8",command=handle_8)
button_8.place(height=50,width=80,x=610,y=350)

button_9 = Button(root,relief=FLAT,bg="white",text="9",command=handle_9)
button_9.place(height=50,width=80,x=720,y=350)

button_0 = Button(root,relief=FLAT,bg="white",text="0",command=handle_0)
button_0.place(height=50,width=80,x=610,y=425)

plus = Button(root,relief=FLAT,bg="#d63031",text="+",activebackground="#d63031",command=handle_plus)
plus.place(height=50,width=80,x=500,y=125)

minus = Button(root,relief=FLAT,bg="#d63031",text="-",activebackground="#d63031",command=handle_minus)
minus.place(height=50,width=80,x=610,y=125)

multiply = Button(root,relief=FLAT,bg="#d63031",text="x",activebackground="#d63031",command=handle_multiply)
multiply.place(height=50,width=80,x=720,y=125)

divide = Button(root,relief=FLAT,bg="#d63031",text="/",activebackground="#d63031",command=handle_divide)
divide.place(height=50,width=80,x=830,y=125)

open_paranthesis = Button(root,relief=FLAT,bg="#d63031",text="(",activebackground="#d63031",command=handle_open_paranthesis)
open_paranthesis.place(height=50,width=80,x=830,y=200)

close_paranthesis = Button(root,relief=FLAT,bg="#d63031",text=")",activebackground="#d63031",command=handle_close_paranthesis)
close_paranthesis.place(height=50,width=80,x=830,y=275)

equals = Button(root,relief=FLAT,bg="#EE5A24",text="=",activebackground="#EE5A24",command=handle_equals)
equals.place(height=50,width=80,x=830,y=350)
root.mainloop()
