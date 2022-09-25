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
        #-----------------CONVERTER TOOL--------------------------
        #---------------------------------------------------------
        self.converter = UnitConverterTools()
        self._quantities = self.converter.quantities
        self.quantities = [ ]

        for quantity in self._quantities:
            if ("_" in quantity):
                quantity = quantity.replace("_", " ")
            self.quantities.append(quantity.capitalize())

        #---------------------------------------------------------
        self.__build()
        self.__bind_events()
        self.mainloop()
    
    def __build(self):

        Combobox = ttk.Combobox
        Entry = ttk.Entry
        Frame = ttk.Frame
        Label = ttk.Label
        StringVar = tk.StringVar

        #----------------------------------------------------------
        self.quantity_combobox_var = StringVar()
        self._from_combobox_var = StringVar()
        self._to_combobox_var = StringVar()
        self._from_entry_var = StringVar()
        self._to_entry_var = StringVar() 

        #----------------------------------------------------------
        #----------QUANTITY SELECTION COMBOBOX---------------------
        #----------------------------------------------------------
        self.quantity_combobox = Combobox(
            self, state="readonly", values=self.quantities, textvariable=self.quantity_combobox_var, font=("Helvetica")
        )
        self.quantity_combobox.grid(
            row=0, column=0, columnspan=3, sticky="nw", ipadx=225, ipady=10, pady=20
        )
        #----------------------------------------------------------
        #---------------`FROM` SECTION CONFIG----------------------
        #----------------------------------------------------------
        frame_1 = Frame(
            self, 
        )
        frame_1.grid(
            column=0, row=1, rowspan=2, sticky="nw"
        )
        # ENTRY
        self._from_entry = Entry(
            frame_1, textvariable=self._from_entry_var, font=("Helvetica", 13)
        )
        self._from_entry.pack(
            fill="x", ipady=7.5, ipadx=52.5
        )
        # COMBOBOX
        self._from_combobox = Combobox(
            frame_1, textvariable=self._from_combobox_var, state="readonly", font=("Helvetica")
        )
        self._from_combobox.pack(
            fill="x", ipady=7.5
        )

        #--------------------------------------------------------
        #--------------`=` label section-------------------------
        #--------------------------------------------------------
        equals_label = Label(
            self, text="=", font=("Helvetica", 25)
        )
        equals_label.grid(
            column=1, row=1
        )

        #----------------------------------------------------------
        #-----------------`TO` SECTION CONFIG----------------------
        #----------------------------------------------------------
        frame_2 = Frame(
            self, 
        )
        frame_2.grid(
            column=2, row=1, rowspan=2, sticky="ne"
        )
        # ENTRY
        self._to_entry = Entry(
            frame_2, textvariable=self._to_entry_var, font=("Helvetica", 13)
        )
        self._to_entry.pack(
            fill="x", ipady=7.5, ipadx=52.5
        )
        # COMBOBOX
        self._to_combobox = Combobox(
            frame_2, textvariable=self._to_combobox_var, state="readonly", font=("Helvetica")
        )
        self._to_combobox.pack(
            fill="x", ipady=7.5
        )
    
    def __quantity_selected(self):

        selected_quantity = self.quantity_combobox_var.get().lower()

        if (" " in selected_quantity):
            selected_quantity = selected_quantity.replace(" ", "_")

        #--------------------------------------------------------------------------------
        #------CONFIGURING _from and _to COMBOBOX VALUES BASED ON SELECTED QUANTITY------
        #--------------------------------------------------------------------------------
        _quantity_units = self.converter.quantity_units[selected_quantity]
        quantity_units = []

        for quantity_unit in _quantity_units:
            if ("_" in quantity_unit):
                quantity_unit = quantity_unit.replace("_", " ")
            quantity_units.append(quantity_unit.capitalize())

        self._from_combobox.config(values=quantity_units)
        self._to_combobox.config(values=quantity_units)

        self._from_combobox_var.set(quantity_units[0])
        self._to_combobox_var.set(quantity_units[0])

    def __bind_events(self):

        self.quantity_combobox.bind(
            "<<ComboboxSelected>>", lambda event=None: self.__quantity_selected()
        )

        self.bind(
            "<Control-w>", lambda event=None: self.destroy()
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy()
        )
        
        
    
        

    


if __name__ == "__main__":
    UnitConverter()