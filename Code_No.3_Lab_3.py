import tkinter as tk

root = tk.Tk()
root.title("Father of Computer")
root.geometry("300x100+10+10")

# Create a frame to hold the text
frame = tk.Frame(root)

# Add the text to the frame with a larger font size
text = tk.Label(frame, text="Charles Babbage", bg="cyan", font=("Times New Roman", 20))

# Pack the frame to center the text
frame.pack(expand=True)
text.pack(side="left", fill="both", expand=True)

root.mainloop()