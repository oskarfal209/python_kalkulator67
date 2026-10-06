from tkinter import *
import math

window = Tk()
window.title("Kalkulator okienkowy - OF")
window.geometry("750x1160")
window.resizable(False, False)

# --- JEDNO MIEJSCE ZARZĄDZANIA STANEM TEKSTU ---
equation_text = ""
equation_label = StringVar()

def update_equation(new_text):
    global equation_text
    equation_text = str(new_text)
    equation_label.set(equation_text)


# --- LOGIKA PRZYCISKÓW ---
def button_press(num):
    update_equation(equation_text + str(num))

def clear():
    update_equation("")

def equals():
    try:
        code_to_eval = equation_text
        code_to_eval = code_to_eval.replace('÷', '/').replace('x', '*')
        code_to_eval = code_to_eval.replace('x²', '**2')
        
        if '√' in code_to_eval:
            code_to_eval = code_to_eval.replace('√', 'math.sqrt(') + ')'
            
        if 'Log' in code_to_eval:
            code_to_eval = code_to_eval.replace('Log', 'math.log10(') + ')'

        total = str(eval(code_to_eval))
        update_equation(total)

    except (SyntaxError, NameError, TypeError):
        equation_label.set("Błąd znaków!")
        update_equation("")
    except ZeroDivisionError:
        equation_label.set("Błąd dzielenia!")
        update_equation("")


# --- INTERFEJS GRAFICZNY ---
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="black", fg="white", width=24, height=3)
label.pack()

frame = Frame(window)
frame.pack()

# Macierz przycisków: [tekst, akcja, bg, fg]
buttons_layout = [
    [("C", clear, "darkgrey", "red"), ("√", lambda: button_press('√'), "darkgrey", "black"), ("x²", lambda: button_press('x²'), "darkgrey", "black"), ("÷", lambda: button_press('÷'), "darkgrey", "black")],
    [(1, lambda: button_press(1), "black", "white"), (2, lambda: button_press(2), "black", "white"), (3, lambda: button_press(3), "black", "white"), ("x", lambda: button_press('x'), "darkgrey", "black")],
    [(4, lambda: button_press(4), "black", "white"), (5, lambda: button_press(5), "black", "white"), (6, lambda: button_press(6), "black", "white"), ("-", lambda: button_press('-'), "darkgrey", "black")],
    [(7, lambda: button_press(7), "black", "white"), (8, lambda: button_press(8), "black", "white"), (9, lambda: button_press(9), "black", "white"), ("+", lambda: button_press('+'), "darkgrey", "black")],
    [("Log", lambda: button_press('Log'), "darkgrey", "black"), (0, lambda: button_press(0), "black", "white"), (".", lambda: button_press('.'), "darkgrey", "black"), ("=", equals, "darkgrey", "black")]
]

# Generowanie przycisków
for row_idx, row in enumerate(buttons_layout):
    for col_idx, (text, action, bg_color, fg_color) in enumerate(row):
        btn = Button(
            frame,
            text=text,
            height=4,
            width=9,
            font=35,
            bg=bg_color,
            fg=fg_color,
            command=action
        )
        btn.grid(row=row_idx, column=col_idx)

window.mainloop()