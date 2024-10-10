import tkinter as tk

def on_button_click():
    label.config(text='Button clicked')

# Create the main application window
root = tk.Tk()
root.title('Simple tkinter app')

# Create a label widget
label = tk.Label(root, text='Hello Tkinter')
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text='CLICK me', command=on_button_click)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
