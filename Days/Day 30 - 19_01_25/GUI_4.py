import tkinter as tk

root = tk.Tk()  # Create the main window

def volume_up():
	print(f"Volume Increased +1")
def volume_down():
	print(f"Volume decreased -1")

# Create the volume up button
vol_up = tk.Button(root, text="+", command=volume_up)
vol_up.pack()

vol_down = tk.Button(root, text="-", command=volume_down)
vol_down.pack()

root.mainloop()