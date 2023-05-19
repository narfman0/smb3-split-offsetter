import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

from smb3splitoffsetter.main import main
from smb3splitoffsetter.models import OffsetTypes


class App(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        master.title("Split Offsetter")
        self.grid(padx=5, pady=5)
        self.infile = tk.StringVar()
        self.outfile = tk.StringVar()

        orig_offset_type = ttk.Label(self, text="Original offset type:")
        orig_offset_type.grid(column=0, row=0)
        self.selected_orig_offset_type = tk.StringVar()
        self.selected_orig_offset_type.set(OffsetTypes.MARIO_WAND_GRAB.name.lower())
        orig_offset_type_cb = ttk.Combobox(
            self, textvariable=self.selected_orig_offset_type
        )
        orig_offset_type_cb["values"] = [m.name.lower() for m in OffsetTypes]
        orig_offset_type_cb.grid(column=1, row=0)

        target_offset_type = ttk.Label(self, text="Target offset type:")
        target_offset_type.grid(column=0, row=1)
        self.selected_target_offset_type = tk.StringVar()
        self.selected_target_offset_type.set(OffsetTypes.LETTER.name.lower())
        target_offset_type_cb = ttk.Combobox(
            self, textvariable=self.selected_target_offset_type
        )
        target_offset_type_cb["values"] = [m.name.lower() for m in OffsetTypes]
        target_offset_type_cb.grid(column=1, row=1)

        self.infile_button = tk.Button(
            self,
            text="Select input lss file",
            command=self.infile_button_selected,
        ).grid(column=0, row=2, columnspan=2)
        self.outfile_button = tk.Button(
            self,
            text="Save output lss file...",
            command=self.outfile_button_selected,
        ).grid(column=0, row=3, columnspan=2)

    def infile_button_selected(self):
        self.infile.set(
            askopenfilename(filetypes=(("split files", "*.lss"), ("all files", "*.*")))
        )
        self.outfile.set(self.infile.get())

    def outfile_button_selected(self):
        self.outfile.set(
            asksaveasfilename(
                filetypes=(("split files", "*.lss"), ("all files", "*.*"))
            )
        )
        if self.outfile.get() == self.infile.get():
            showinfo("Failure", f"You may not use write directly to the same file :(")
            return
        main(
            self.infile.get(),
            self.outfile.get(),
            OffsetTypes[self.selected_orig_offset_type.get().upper()],
            OffsetTypes[self.selected_target_offset_type.get().upper()],
        )
        showinfo(
            "Success", f"Successfully wrote new splits file to {self.outfile.get()}"
        )


def ui():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()


if __name__ == "__main__":
    ui()
