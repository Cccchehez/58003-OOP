import tkinter as tk
def convert():
    try:
        cm = float(cm_entry.get())
        m = cm / 100
        km = cm / 100000
        m_entry.delete(0, tk.END)
        km_entry.delete(0, tk.END)
        m_entry.insert(0, str(m))
        km_entry.insert(0, str(km))
        m_entry.config(fg='red')
        km_entry.config(fg='red')
    except ValueError:
        m_entry.delete(0, tk.END)
        km_entry.delete(0, tk.END)
        m_entry.insert(0, "Invalid input")
        km_entry.insert(0, "Invalid input")

root = tk.Tk()
root.title("Metrics of Unit Lengths")
root.geometry("500x300+10+10")


cm_label = tk.Label(root, text="Enter the distance in centimeters (cm):")
cm_label.grid(row=0, column=0, padx=30, pady=30)

cm_entry = tk.Entry(root, width=20)
cm_entry.grid(row=0, column=1, padx=30, pady=30)

m_label = tk.Label(root, text="Conversion into meters (m):")
m_label.grid(row=1, column=0, padx=30, pady=30)

m_entry = tk.Entry(root, width=20)
m_entry.grid(row=1, column=1, padx=30, pady=30)

km_label = tk.Label(root, text="Conversion into kilometers (km):")
km_label.grid(row=2, column=0, padx=30, pady=30)

km_entry = tk.Entry(root, width=20)
km_entry.grid(row=2, column=1, padx=30, pady=30)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()