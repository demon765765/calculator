import tkinter as tk
from calculator import on_click

def create_calculator_ui():
    """Create and configure the calculator user interface.

    Returns:
        tk.Tk: The main Tkinter window.

    :param entry: Entry widget for displaying and entering values.
    :param expression_var: StringVar for displaying the expression.
    :param result_var: StringVar for displaying the result.
    """

    root = tk.Tk()
    root.title("Calculator")
    root.configure(bg='red')

    # display
    entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
    entry.grid(row=0, column=0, columnspan=4, pady=5)

    expression_var = tk.StringVar()
    result_var = tk.StringVar()

    display_frame = tk.Frame(root, bg='lightblue', borderwidth=2, relief='solid')
    display_frame.grid(row=0, column=0, columnspan=4, sticky='ew', pady=5)

    expression_label = tk.Label(display_frame, textvariable=expression_var, font=('Arial', 12, 'italic'), bg='lightblue')
    expression_label.grid(row=0, column=0, padx=(5, 10), pady=5)

    result_label = tk.Label(display_frame, textvariable=result_var, font=('Arial', 16, 'bold'), bg='lightblue')
    result_label.grid(row=0, column=1, padx=(10, 5), pady=5)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        button_text = button
        if button == "=":
            button_text = "="

        square_button = tk.Canvas(root, width=50, height=50, borderwidth=3, relief='solid', bg='yellow')
        square_button.grid(row=row_val, column=col_val)

        oval_button = tk.Canvas(square_button, width=40, height=40, borderwidth=0, highlightthickness=0)
        oval_button.place(relx=0.5, rely=0.5, anchor='center')

        oval_button.create_oval(5, 5, 35, 35, fill="lightgreen", outline="black", width=3)

        text_id = oval_button.create_text(20, 20, text=button_text, font=('Arial', int(1.3 * 12), 'bold'))

        oval_button.bind("<Button-1>", lambda event, b=button: on_click(entry, expression_var, result_var, b))

        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    fun_label = tk.Label(root, text="Fun with Math", font=('Arial', 18, 'italic'), bg='red')
    fun_label.grid(row=row_val, column=col_val, columnspan=3, sticky='se', padx=10, pady=25)

    return root

if __name__ == "__main__":
    main_window = create_calculator_ui()
    main_window.mainloop()

