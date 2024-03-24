import tkinter as tk
from tkinter import messagebox
from functions import check


class GUISudokuGrid(tk.Frame):
    def __init__(self,gridSize, master):
        super().__init__(master)
        self.sudoku = master
        self.gridSize = gridSize
        self.entries = {}
        self.create_widgets()
        self.import_numbers()
        
    def import_numbers(self):
        list = [
    [5, 3, 0, 6, 7, 8, 9, 1, 2],
    [6, 7, 0, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
        for i in range(9):
            for j in range(9):
                if list[i][j]!=0:
                    self.entries[(i,j)].insert(0,list[i][j])
                    self.entries[(i,j)].config(state="readonly", disabledforeground="blue")
    
    def entries_to_numbers(self):
        self.values = {}
        for i in range(9):
            for j in range(9):
                a = self.entries[(i,j)].get() 
                if a == 0:
                    return False
                self.values[(i,j)] = a
        return self.values

    def submit(self):
        x = self.entries_to_numbers()
        if x is False:
            messagebox.showinfo("Wrong solution", "Wrong solution")
        else:
            if check(x):
                messagebox.showinfo("You Win", "Congratulations! You solved the Sudoku puzzle!")
            else:
                messagebox.showinfo("Wrong solution", "Wrong solution")



    def validate_entry(self, entry_var):
        value = entry_var.get()
        if value and (not value.isdigit() or value=='0'):
            entry_var.set(value[:-1])  # Remove the last character if not a digit
        if len(value) > 1:
            entry_var.set(value[:1])
        
    def create_entry(self,box_frame, row, col):
        entry_var = tk.StringVar()
        entry = tk.Entry(box_frame, width=2, font=("Arial", 50), validate="key", justify="center", textvariable=entry_var)
        entry_var.trace('w', lambda *args: self.validate_entry(entry_var))
        entry.grid(row=row, column=col, padx=1, pady=1)
        return entry
            
        
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                box_frame = tk.Frame(self.sudoku, borderwidth=2, relief="solid")
                box_frame.grid(row=i, column=j)
                for m in range(3):
                    for n in range(3):
                        e = self.create_entry(box_frame,m,n)
                        row, col = i*3+m, j*3+n
                        self.entries[(row,col)] = e
        #tk.Button(self.sudoku, text="Submit", command=self.submit).grid(column=3,row=0, padx=10)
        #tk.Button(self.sudoku, text="Submit", command=self.submit).grid(column=3,row=1)
        #tk.Button(self.sudoku, text="Submit", command=self.submit).grid(column=3,row=2)
        tk.Button(self.sudoku, text="Submit", command=self.submit, width=15, height=3).grid(column=1,row=3)
    
    def solve_sudoku(self):
        # You can implement Sudoku solving algorithm here
        pass
