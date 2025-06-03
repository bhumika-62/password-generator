from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import random


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("650x445+370+140")

        main_frame = Frame(self.root, bd=5, relief=RIDGE)
        main_frame.place(x=0, y=0, width=650, height=445)

        title_lbl = Label(main_frame, text="PASSWORD GENERATOR",font=("times new roman", 20, "bold"), fg="grey", bg="white")
        title_lbl.place(x=0, y=0, width=650)

        lenthlbl = Label(main_frame, text="Enter Password Length",font=("times new roman", 15, "bold"), fg="blue")
        lenthlbl.place(x=25, y=150)

        self.var_entry = StringVar()
        self.entry_fill = ttk.Entry(main_frame, textvariable=self.var_entry,width=55, font=("times new roman", 15, "bold"))
        self.entry_fill.place(x=25, y=185)

        self.output_label = Label(main_frame, text="", font=("times new roman", 15, "bold"),fg="green", bd=5, relief=RIDGE)
        self.output_label.place(x=25, y=290, width=580)
        
        btn = Button(main_frame, text="GENERATE PASSWORD", font=("times new roman", 15, "bold"),fg="white", bg="red", bd=4, relief=SUNKEN, cursor="hand2",command=self.pass_generator)
        btn.place(x=40, y=235, width=555, height=35)

    def pass_generator(self):
        if self.var_entry.get() == "":
            messagebox.showerror("Error", "Please enter password length")
        else:
            try:
                num = int(self.var_entry.get())
                if num < 4:
                    messagebox.showwarning("Warning", "Password length should be at least 4")
                    return

                s1 = string.ascii_lowercase
                s2 = string.ascii_uppercase
                s3 = string.digits
                s4 = string.punctuation

                s = list(s1 + s2 + s3 + s4)
                random.shuffle(s)

                password = ''.join(random.choices(s, k=num))
                self.output_label.config(text=f"Generated Password: {password}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
