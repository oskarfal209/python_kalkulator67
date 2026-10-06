from tkinter import *
import math  # Potrzebne do obsługi pierwiastka i logarytmu

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        # Zamieniamy znaki graficzne na operatory zrozumiałe dla Pythona
        code_to_eval = equation_text
        code_to_eval = code_to_eval.replace('÷', '/')
        code_to_eval = code_to_eval.replace('x', '*')
        
        # Obsługa potęgowania x² (zamiana liczby przed x² na potęgę **2)
        code_to_eval = code_to_eval.replace('x²', '**2')
        
        # Obsługa pierwiastka (zamiana √5 na math.sqrt(5))
        # Działa dla prostych zapisów typu √liczba
        if '√' in code_to_eval:
            code_to_eval = code_to_eval.replace('√', 'math.sqrt(') + ')'
            
        # Obsługa logarytmu dziesiętnego (zamiana Log100 na math.log10(100))
        if 'Log' in code_to_eval:
            code_to_eval = code_to_eval.replace('Log', 'math.log10(') + ')'

        total = str(eval(code_to_eval))
        equation_label.set(total)
        equation_text = total

    except (SyntaxError, NameError, TypeError):
        equation_label.set("Błąd znaków!")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Błąd dzielenia!")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Kalkulator okienkowy - OF")
window.geometry("750x1160")
window.resizable(False, False)

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="black", fg="white", width=24, height=3)
label.pack()

frame = Frame(window)
frame.pack()

'''Przyciski numeryczne'''
button1 = Button(frame, text=1, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(1))
button1.grid(row=1, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="black", fg="white", command=lambda: button_press(0))
button0.grid(row=4, column=1)

'''Znaki matematyczne'''
button_clear = Button(frame, text="C", height=4, width=9, font=35, bg="darkgrey", fg="red", command=clear)
button_clear.grid(row=0, column=0)

# Poprawione dodawanie funkcji matematycznych do tekstu
pierwiastek = Button(frame, text="√", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('√'))
pierwiastek.grid(row=0, column=1)

potegowanie = Button(frame, text="x²", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('x²'))
potegowanie.grid(row=0, column=2)

dzielenie = Button(frame, text="÷", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('÷'))
dzielenie.grid(row=0, column=3)

mnozenie = Button(frame, text="x", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('x'))
mnozenie.grid(row=1, column=3)

odejmowanie = Button(frame, text="-", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('-'))
odejmowanie.grid(row=2, column=3)

dodawanie = Button(frame, text="+", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('+'))
dodawanie.grid(row=3, column=3)

# POPRAWIONE: Zmiana command na wywołanie funkcji equals bez lambda i bez przekazywania '='
wynik = Button(frame, text="=", height=4, width=9, font=35, bg="darkgrey", fg="black", command=equals)
wynik.grid(row=4, column=3)

kropka = Button(frame, text=".", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('.'))
kropka.grid(row=4, column=2)

logarytm = Button(frame, text="Log", height=4, width=9, font=35, bg="darkgrey", fg="black", command=lambda: button_press('Log'))
logarytm.grid(row=4, column=0)

window.mainloop()