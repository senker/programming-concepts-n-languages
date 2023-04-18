# Function definition

def f(x):
    return 3 * x ** 2 - 2 * x + 5

# Pure function
def pure_fun_sum(x, y):
    # use only the local function inputs
    return x + y

def crazy_function():
    return

what_is_it = crazy_function()

def do_nothing_useful(i, j):
    x = i + j
    x = i - j
result = do_nothing_useful(10, 12)
print(result)
# >>> print(result)
# None

# lambda functions
lambda_add = lambda x, y: x +y

def greet01(name):
    print ('Ciao ', name)
    
greet02 = lambda name: print('Ciao ', name)

# GUI, Callbacks
import sys
from tkinter import Button, mainloop, messagebox, ttk
import tkinter as tk
win = tk.Tk()
win.geometry('400x300')
win.title('Using lambda callbacks')

combo = ttk.Combobox(
    state="readonly",
    values=["imperative", "Object-Oriented", "Functional", "Distributed"]
    )
combo.place(x=50, y=50)

btn = Button (
        win, text='Click Me',
        command=(lambda : messagebox.showinfo(
            'Paradigm', combo.get() + 
            '\nProgramming!'
        )))

# btn.pack()
btn.place(x=50, y=100)
win.mainloop()

# lambda
tpl = (2019, 3480.65)
fst = lambda x: x[0]
snd = lambda x: x[1]


from functools import reduce
vlst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
summed_val = reduce(lambda n, m: n + m, vlst)
first_val = reduce(lambda n, _: n, vlst)

import matplotlib.pyplot as plt
import numpy as np

# Using pandas
# ============
import pandas as pd
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
series3 = pd.DataFrame(array, columns=['Jan_23', 'Feb_23', 'Mar_23'])
series3

