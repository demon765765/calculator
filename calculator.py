import tkinter as tk

def on_click(entry, expression_var, result_var, button_value):
    """Handle all the button click events for the calculator.

    :param entry: Entry widget for displaying and entering values.
    :param expression_var: StringVar for displaying the expression.
    :param result_var: StringVar for displaying the result.
    :param button_value: Value of the clicked button.
    """
    current_text = entry.get()

    if button_value == "=":
        if current_text.strip() and any(c.isdigit() or c in "+-*/" for c in current_text):
            try:
                result = eval(current_text)
                result_str = "{:.5f}".format(result).rstrip('0').rstrip('.')
                if '.' not in result_str:
                    result = int(result_str)
                else:
                    result = float(result_str)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result_str))
                expression_var.set(f"{current_text} = {result_str}")
                result_var.set("")
            except (SyntaxError, ZeroDivisionError, TypeError, ValueError) as e:
                entry.delete(0, tk.END)
                expression_var.set("Error")
                result_var.set("")
                print(f"Error: {e}")
    elif button_value == "C":
        entry.delete(0, tk.END)
        expression_var.set("")
        result_var.set("")
    else:
        entry.insert(tk.END, button_value)
        expression_var.set(entry.get())
