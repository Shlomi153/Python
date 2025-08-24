#Created by Shlomi Kiko
#Goal: Basic GUI example
#Linkedin: https://www.linkedin.com/in/shlomikiko/


#Import the Tkinter library
import tkinter as tk

#Function that triggers an action for the button
def button_clicked():
    button.config(text='You picked right!')
    label1.config(text='Did you choose this?')
    #label2.config(text='Or was it this one?')
    #Another option to modify
    label1.config(text=input.get())
    label2['text'] = 'These are not the drones you are looking for'

#Create the window object, define the basic properties
window = tk.Tk()
window.title('Good luck!')
window.minsize(500, 300)

#Create a Label
label1 = tk.Label(text='HP Pro Book G8', font=('comic sans ms', 24, 'italic'))
label1.pack(side='left')

label2 = tk.Label(text='Mysterious Macbook', font=('gothic', 24, 'italic'))
label2.pack(side='right')

#Create a Button
button = tk.Button(text='Click me!', command=button_clicked, width=15)
button.pack()

#Entry field
input = tk.Entry(width=20)
input.pack()

#Ensure the window keeps running until closed manually
window.mainloop()

