from tkinter import ttk 
from converter.converter import UnitConverterTools
import tkinter as tk

class UnitConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        #---------------------------------------------------------
        #-----------CONFIGURING ROOT WINDOW-----------------------
        #---------------------------------------------------------
        self.title("Unit Converter")
        self.geometry("600x350")
        self.resizable(False, False)
        self.columnconfigure(index=0, weight=2)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=2)
        self.config(bd=5)

        #---------------------------------------------------------
        self.__build()
        self.mainloop()
    
    def __build(self):

        Combobox = ttk.Combobox
        Entry = ttk.Entry
        Label = ttk.Label
        StringVar = tk.StringVar

        #----------------------------------------------------------
        self.quantity_combobox_var = StringVar()
        self._from_entry_var = StringVar()
        self._to_entry_var = StringVar() 

        #----------------------------------------------------------
        #----------QUANTITY SELECTION COMBOBOX---------------------
        #----------------------------------------------------------
        quantity_combobox = Combobox(
            self, state="readonly", values=("Length", "Mass")
        )
        quantity_combobox.grid(
            row=0, column=0, columnspan=3, sticky="nw", ipadx=225, ipady=10, pady=20
        )
        #----------------------------------------------------------
        #---------------------ENTRY AND LABEL----------------------
        #----------------------------------------------------------
        _from_entry = Entry(
            self, textvariable=self._from_entry_var, font=("Helvetica", 12)
        )
        _from_entry.grid(
            column=0, row=1, sticky="nw", ipadx=50, ipady=6.5
        )

        equals_label = Label(
            self, text="=", font=("Helvetica", 20)
        )
        equals_label.grid(
            column=1, row=1
        )

        _to_entry = Entry(
            self, textvariable=self._to_entry_var, font=("Helvetica", 12)
        )
        _to_entry.grid(
            column=2, row=1, sticky="ne", ipadx=50, ipady=6.5, 
        )

        _from_quantity_combobox = Combobox(
            self, state="readonly"
        )
        _from_quantity_combobox.grid(
            column=0, row=2, sticky="nw", ipadx=72.5, ipady=6.5
        )

        _to_quantity_combobox = Combobox(
            self, state="readonly"
        )
        _to_quantity_combobox.grid(
            column=2, row=2, sticky="ne", ipadx=72.5, ipady=6.5
        )
        

    


if __name__ == "__main__":
    UnitConverter()