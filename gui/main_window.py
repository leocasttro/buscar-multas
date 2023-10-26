from tkinter import *
from tkinter import ttk

class MinhaAplicacao:
    def __init__(self, root):

        def calculate(*args):
            try:
                value = float(self.feet.get())
                self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
            except ValueError:
                pass
        
        self.root = root
        self.root.title("Consulta multas")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(self.mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(self.mainframe, text="Pés").grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text="o equivalente em").grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text="metros").grid(column=3, row=2, sticky=W)

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.feet_entry.focus()
        root.bind("<Return>", calculate)

        root.mainloop()
