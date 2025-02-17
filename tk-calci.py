# import tkinter as tk
#
# # Function to handle button clicks
# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, current + str(number))
#
# # Function to clear the entry field
# def clear():
#     entry.delete(0, tk.END)
#
# # Function to evaluate the expression
# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")
#
# # Create the main application window
# root = tk.Tk()
# root.title("Basic Calculator")
#
# # Entry widget for displaying input and results
# entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=5, justify='right')
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#
# # Button layout
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]
#
# # Create and place buttons on the grid
# for (text, row, col) in buttons:
#     if text == 'C':
#         button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear)
#     elif text == '=':
#         button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate)
#     else:
#         button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
#                            command=lambda t=text: button_click(t))
#     button.grid(row=row, column=col, padx=5, pady=5)
#
# # Run the main event loop
# root.mainloop()

import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    if button_text == "=":
        try:
            entry_var.set(eval(entry_var.get()))
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

# Create main application window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget with StringVar for automatic updates
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 18), justify='right', bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons dynamically
for r, row in enumerate(buttons, 1):
    for c, text in enumerate(row):
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=lambda t=text: on_click(t)).grid(row=r, column=c, padx=5, pady=5)

# Run the application
root.mainloop()
