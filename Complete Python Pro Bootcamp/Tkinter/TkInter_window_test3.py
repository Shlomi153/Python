#Build the following for practice:
#1) Spinbox V
#2) Radiobuttons V
#3) Checkboxes V
#4) Listbox V
#5) Scale V
#6) Entry field with pre inserted text V
#7) Text Entrybox V
#8) Label V
#9) Button V

#import the required libraries
import tkinter as tk

def button_click():
    input_value = input.get()
    label.config(text=input_value)
    entry_textbox()

def radio_button():
    print(radio_val.get())

def check_button():
    print(checkbutton_val.get())

def scale_value(val):
    print(val)

def spinbox_value():
    print(spinbox.get())

def entry_textbox():
    print(text_entrybox.get('1.0', tk.END)) #1 specifies the first character of the string, end focuses the index
    
def listbox_used(event): #Event listener
    print(listbox.get(listbox.curselection()))


#Create the GUI object
window = tk.Tk()
window.title('Test GUI')
window.minsize(750, 750)

#Create a Label
label = tk.Label(text='Initial value', font=('comic sans ms', 24, 'italic'))
label.pack(side='left')

#Create an Entry field with pre empted text
input = tk.Entry(width=30)
input.insert(tk.END, string='Entry:')
input.pack(side='left')

#Create a Button
button = tk.Button(text='Click me!', command=button_click, font=('comic sans ms', 18, 'bold'))
button.pack()

#Create a Radiobutton
radio_val = tk.IntVar()
radiobutton1 = tk.Radiobutton(text='First one?', value=1, variable=radio_val, command=radio_button)
radiobutton2 = tk.Radiobutton(text='Second one?', value=2, variable=radio_val, command=radio_button)
radiobutton1.pack(side='left', anchor='nw')
radiobutton2.pack(side='left', anchor='nw')

#Create a Checkbutton
checkbutton_val = tk.IntVar()
checkbutton = tk.Checkbutton(text='Is active?', variable=checkbutton_val, command=check_button)
checkbutton.pack()

#Create a Scale
scale = tk.Scale(from_=1, to=5, command=scale_value)
scale.pack(side='left')

#Create a Spinbox
spinbox = tk.Spinbox(from_=0, to=5, command=spinbox_value)
spinbox.pack()

#Create a Text Entrybox
text_entrybox = tk.Text(height=25, width=50)
text_entrybox.insert(tk.END, 'This is an entrybox used as an example...')
text_entrybox.focus() #Puts the mouse cursor on the field here to focus the attention
text_entrybox.pack()

#Create a Listbox
listbox = tk.Listbox(height=4)

car_models = ['Nissan', 'Suzuki', 'Porshe', 'BMW']

for car in car_models:
    listbox.insert(car_models.index(car), car)

listbox.bind("<<ListboxSelect>>", listbox_used) #The text has to be exact for it to work
listbox.pack()

#Ensure the window does not close unless manually done so
window.mainloop()