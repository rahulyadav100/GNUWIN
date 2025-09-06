import tkinter as tk
from time import strftime

# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)  # Update every second

# Create window
root = tk.Tk()
root.title("Digital Clock by Rahul")
root.geometry("400x200")
root.resizable(False, False)

# Background color
root.config(bg="black")

# Clock label
label = tk.Label(
    root, 
    font=('Arial', 40, 'bold'), 
    background='black', 
    foreground='cyan'
)
label.pack(anchor='center')

# Run the clock
time()
root.mainloop()
