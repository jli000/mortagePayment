from tkinter import *

root = Tk()
root.title("CIS 403 GUI_Programming")
root.geometry("300x400")


def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get(
    ) and down_entry.get():
        y = int(term_entry.get())
        m = y * 12
        r = float(interest_entry.get())
        loan = int(amount_entry.get())
        down = int(down_entry.get())
        monthly_rate = r / 100 / 12
        mp = (monthly_rate / (1 - (1 + monthly_rate)**(-m))) * (loan - down)
        mp = f"{mp:,.2f}"
        payment_label.config(text=f"Monthly Payment: ${mp}")
    else:
        payment_label.config(text="Error")


my_label_frame = LabelFrame(root)
my_label_frame.pack(pady=20)
my_frame = Frame(my_label_frame)
my_frame.pack(pady=5, padx=10)
name = Label(my_frame, text="Created by Jason Li")
amount_label = Label(my_frame, text="Amount")
amount_entry = Entry(my_frame)
down_label = Label(my_frame, text="Down Payment")
down_entry = Entry(my_frame)
interest_label = Label(my_frame, text="Interest")
interest_entry = Entry(my_frame)
term_label = Label(my_frame, text="Years")
term_entry = Entry(my_frame)
name.grid(row=5, column=5)
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1, pady=10)
down_label.grid(row=1, column=0)
down_entry.grid(row=1, column=1, pady=10)
interest_label.grid(row=2, column=0)
interest_entry.grid(row=2, column=1, pady=10)
term_label.grid(row=3, column=0)
term_entry.grid(row=3, column=1, pady=10)
my_button = Button(my_label_frame, text="Calculate", command=payment)
my_button.pack(pady=20)
payment_label = Label(root, text="")
payment_label.pack(pady=20)
root.mainloop()
