import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from smb3splitoffsetter.main import main
from smb3splitoffsetter.models import OffsetTypes


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.infile = tk.StringVar()
        self.outfile = tk.StringVar()
        self.selected_offset_type = tk.StringVar()
        self.selected_offset_type.set(OffsetTypes.LETTER.name.lower())
        offset_type_cb = ttk.Combobox(self, textvariable=self.selected_offset_type)
        offset_type_cb["values"] = [m.name.lower() for m in OffsetTypes]
        offset_type_cb.pack(fill=tk.X, padx=5, pady=5)

        self.infile_button = tk.Button(
            self,
            text="Select input lss file",
            command=self.infile_button_selected,
        ).pack()
        self.outfile_button = tk.Button(
            self,
            text="Save output lss file as...",
            command=self.outfile_button_selected,
        ).pack()

        tk.Button(self, text="Execute", command=self.execute).pack(
            fill=tk.X, padx=5, pady=5
        )

    def execute(self):
        main(
            self.infile.get(),
            self.outfile.get(),
            OffsetTypes[self.selected_offset_type.get().upper()],
        )

    def infile_button_selected(self):
        self.infile.set(askopenfilename())
        self.outfile.set(self.infile.get())

    def outfile_button_selected(self):
        self.outfile.set(asksaveasfilename())


def ui():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()


if __name__ == "__main__":
    ui()
