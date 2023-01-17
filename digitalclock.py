from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

window.configure(bg="steelblue")
label = Label(window, text="Namaste!!", bg="steelblue")
label.pack(pady=100)

window.mainloop()