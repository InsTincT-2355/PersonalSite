import tkinter as tk
from tkinter import ttk



def click_calc():
    root.title("you clicked calculate")
    
    
def click_exit():
    root.destroy()    


root = tk.Tk()
root.title("Days until your birthday")
root.geometry("500x300")

frame = ttk.Frame(root, padding ="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)


date_label = ttk.Label(frame, text = "Birth Date (dd/mm/yy): ").grid(row=0, column=0)
date_entry = ttk.Entry(frame, width=25, textvariable=date_label).grid(column=1, row=0)



day_label = ttk.Label(frame, text = "Days Left: ").grid(row=1, column=0)
day_entry = ttk.Entry(frame, width=25, textvariable=day_label).grid(column=1, row=1)

calc = ttk.Button(frame, text = "Calculate" , command=click_calc).grid(row=2,column=0)
exit = ttk.Button(frame, text = "Exit" , command=click_exit).grid(row=2,column=1)




root.mainloop()