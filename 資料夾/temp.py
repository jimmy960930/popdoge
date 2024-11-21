# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def greet():
    user_name=entry.get()
    label.config(text=f"Hello {user_name}!")
import tkinter as tk
window = tk.Tk()
window.title("aepougijnseiougbaehygioets")
window.geometry("900x400")
label = tk.Label(window,text="enter name")
label.pack()
entry=tk.Entry(window)
entry.pack()
button = tk.Button(window,text="確認",command=greet)
button.pack()
window.mainloop()




    

    
    
