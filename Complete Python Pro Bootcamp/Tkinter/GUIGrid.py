#Created by Shlomi Kiko
#Goal: This program shows how to use a grid for a GUI
#Linkedin: https://www.linkedin.com/in/shlomikiko/


#Note: can also use Place for absolute positioning and Pack for relative(Pack is not as efficient as Grid and cannot work together with it)

#Import the libraries
import tkinter as tk

def button1_used():
    print('Button1 clicked!')

def button2_used():
    print('Button2 clicked!')

def entry_used():
    print(entry.get())

#Create a GUI object
window = tk.Tk()
window.title('Placement practice')
window.minsize(250, 125)
window.config(padx=15, pady=15)#Padding to give space between elements

#Create a Label:
label = tk.Label(text='Label', font=('comic sans ms', 24, 'italic'))
label.grid(row=0, column=0)

#Create a Button
button1 = tk.Button(text='Button1', command=button1_used)
button1.grid(row=1, column=2)#Rows, columns
#button1.config(padx=10, pady=10)#Can also just give padding to a specific element

#Create a second Button
button2 = tk.Button(text='Button2', command=button2_used)
button2.grid(row=0, column=3)

#Create an Entry field
entry = tk.Entry()
entry.grid(row=3, column=4)

#Mainloop
window.mainloop()