import tkinter as tk
from PIL import Image,ImageTk
window = tk.Tk()
window.title("PopDoge")
window.geometry("400x500")
window.resizable(False,False)

def update_count():
    global click_count
    click_count +=1
    count_label.config(text=f"點擊次數:{click_count}")
    
    
def on_click(event):
    doge_label.config(image=closed_image)
    window.after(200,lambda:doge_label.config(image=opened_image))
    update_count()

def reset_count():
    global click_count
    click_count = 0
    count_label.config(text=f"點擊次數:{click_count}")

closed_image = ImageTk.PhotoImage(Image.open("close.jpg").resize((300,300)))
opened_image = ImageTk.PhotoImage(Image.open("open.jpg").resize((300,300)))


doge_label = tk.Label(window,image=opened_image)
doge_label.pack(pady=20)

count_label = tk.Label(window,text="點擊次數:0",font=("Arial",18))
count_label.pack(pady=10)
    
click_count = 0
doge_label.bind("<Button>",on_click)


reset_button = tk.Button(window,text="reset",command=reset_count)
reset_button.pack()

window.mainloop()
    
    
