#shutdown app using python
import tkinter as tk   #we can also write from tkinter import * ( which imports all function of tkinter)
import os

#functions for buttons

def restart():
    os.system("shutdown /r /t 1")  #1 is time
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

# calling of Tk liabrary
st=tk.Tk() 
st.title("Shutdown app")
st.geometry("300x300")
st.config(bg="Blue")

r_button =tk.Button(st,text="Restart",font=("Time New Roman",10,"bold"),cursor="hand2",command=restart)  #font(font,size,style)
r_button.place(x=50,y=50,height=40,width=200)


r_button =tk.Button(st,text="Restart Time",font=("Time New Roman",10,"bold"),cursor="hand2",command=restart_time)  #font(font,size,style)
r_button.place(x=50,y=100,height=40,width=200)   #(outer,inner)

r_button = tk.Button(st,text="Log-Out",font=("Time New Roman",10,"bold"),cursor="hand2",command=logout)  #font(font,size,style)
r_button.place(x=50,y=150,height=40,width=200) 

r_button = tk.Button(st,text="ShutDown",font=("Time New Roman",10,"bold"),cursor="hand2",command=shutdown)  #font(font,size,style)
r_button.place(x=50,y=200,height=40,width=200)

st.mainloop()