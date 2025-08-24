#Created by Shlomi Kiko
#Goal: This program converts Miles to Kilometers and uses Tkinter for the GUI
#Linkedin: https://www.linkedin.com/in/shlomikiko/

#Plan of action:
#1) Import the required libraries
#2) Create the GUI object
#3) Create 3 labels
#4) Create 2 entry fields, one of them will input it's information in the other Miles to KM
#5) Create a Calculate function that converts Miles to KM
#6) Create a Calculate button, when clicked it should convert the Miles to KM on the relevant field

#Import the relevant libraries
import tkinter as tk

#Function that converts miles to km
def convert_miles_km(val):
    miles2km = round(val * 1.60934, 2)
    return miles2km

#Function responsible for the changes once the button is clicked
def calc_button_used():
    if km_entry is not None: #Reset values after the first use to avoid concatenating values
        km_entry.delete(0, tk.END)

    miles_val = float(miles_entry.get())
    converted_val = convert_miles_km(miles_val)

    if converted_val == 0.0: #Estatic reasons
        converted_val = 0
    
    km_entry.insert(tk.END, string=converted_val)

#Create the GUI object
window = tk.Tk()
window.title('Miles to KM Converter')
window.minsize(200, 100)
window.config(padx=20, pady=20)

#Create 3 Labels
equal_label = tk.Label(text='Equal to', font=('comic sans ms', 12, 'italic'))
equal_label.grid(row=1, column=0)

miles_label = tk.Label(text='Miles', font=('comic sans ms', 12, 'italic'))
miles_label.grid(row=0, column=2)

km_label = tk.Label(text='Km', font=('comic sans ms', 12, 'italic'))
km_label.grid(row=1, column=2)

#Create 2 Entry Fields
miles_entry = tk.Entry()
miles_entry.insert(tk.END, 0)
miles_entry.grid(row=0, column=1)

km_entry = tk.Entry()
km_entry.grid(row=1, column=1)

#Create the Calculate Button
calc_button = tk.Button(text='Calculate', command=calc_button_used)
calc_button.grid(row=2, column=1)

#Mainloop to ensure the program does not close without manual input
window.mainloop()
