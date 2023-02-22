import tkinter as tk
import math
import speech_recognition as sr
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

def main():
    # Creating the main window
    window = tk.Tk()
    window.title("Scientific Calculator")
    global entry
    entry = tk.Entry(window, width=45, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    # Creating the buttons using loops and the calculate function
    button_labels = ['C', 'CE', '(', ')', 'π','2π',
                     'cosθ', 'tanθ', 'sinθ', 'arcsin', 'arccos', 'arctan',
                     'sinh', 'cosh', 'tanh', 'log10','ln', 'deg',
                     '√', '^3', '^2','e', 'rad',
                    'x!', '7', '8', '9', '0', '+', '*',
                      '4', '5', '6','.','-', '/','1',
                     '2', '3',
                      '', '', '=']

    # Creating the buttons with loops
    row_count = 1
    col_count = 0
    for button_label in button_labels:
        button = tk.Button(window, text=button_label, padx=20, pady=10, width = 5, height = 3, command=lambda btn=button_label: calculate(btn))
        button.grid(row=row_count, column=col_count)
        col_count += 1
        if col_count > 5:
            row_count += 1
            col_count = 0
    button = tk.Button(window, text="Microphone", padx=20, pady=10, width = 5, height = 3, command=audio)
    button.grid(row=7, column=3)

    # Running the main loop
    window.mainloop()

def calculate(value):
    ex = entry.get()
    result = ''

    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entry.delete(0, tk.END)
            entry.insert(0, ex)
            return

        elif value == 'CE':
            entry.delete(0, tk.END)

        elif value == '√':
            result = math.sqrt(eval(ex))

        elif value == 'π':
            result = math.pi

        elif value == 'cosθ':
            result = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            result = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            result = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            result = 2 * math.pi

        elif value == 'cosh':
            result = math.cosh(eval(ex))

        elif value == 'tanh':
            result = math.tanh(eval(ex))

        elif value == 'sinh':
            result = math.sinh(eval(ex))

        elif value == chr(8731):
            result = eval(ex) ** (1 / 3)

        elif value == '^2':
            result = eval(ex) ** 2

        elif value == '^3':
            result = eval(ex) ** 3

        elif value == 'ln':
            result = math.log(eval(ex))

        elif value == 'deg':
            result = math.degrees(eval(ex))

        elif value == 'rad':
            result = math.radians(eval(ex))

        elif value == 'e':
            result = math.e

        elif value == 'log10':
            result = math.log10(eval(ex))

        elif value == 'x!':
            result = math.factorial(eval(ex))

        elif value == 'arcsin':
            result = math.asin(eval(ex))

        elif value == 'arccos':
            result = math.acos(eval(ex))

        elif value == 'arctan':
            result = math.atan(eval(ex))

        elif value == 'x!':
            result = math.factorial(eval(ex))

        elif value == '=':
            result = eval(ex)

        else:
            entry.insert(tk.END, value)
            return

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except SyntaxError:
        pass

def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        # Use Google speech recognition to convert speech to text
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Parse and evaluate the math expression
        transformations = (standard_transformations + (implicit_multiplication_application,))
        expr = parse_expr(text, transformations=transformations)
        result = float(expr.evalf())

        # Output the result
        print("Result: ", result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__== "__main__":
    main()