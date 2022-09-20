from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from Converting import Converter


class ConverterWindow:
    def __init__(self):
        super().__init__()

        self.converter = Converter()
        self.output_textbox = None
        self.output_window = None

        self.window = Tk()
        self.image = PhotoImage(file="GetLucky.png")
        self.window.iconphoto(True, self.image)
        self.window.title("character converter")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.frame = ttk.Frame(self.window, padding="5 5 5 5")
        self.frame.grid(column=0, row=0, sticky='N E S W')

        self.label_from = ttk.Label(self.frame, text="From")
        self.label_from.grid(column=0, row=0, sticky=W)

        self.from_choices = StringVar()
        self.combobox_from = ttk.Combobox(self.frame, textvariable=self.from_choices)
        self.combobox_from['values'] = ['UTF-8', 'Base64', 'HTML', 'Unicode']
        self.combobox_from.state(["readonly"])
        self.combobox_from.current(0)
        self.combobox_from.grid(column=1, row=0, sticky=W)

        self.combobox_from.current(0)
        self.convert_from_text = scrolledtext.ScrolledText(self.frame, width=80, height=15)
        self.convert_from_text.grid(row=1, column=0, columnspan=5)

        self.label_to = ttk.Label(self.frame, text="To")
        self.label_to.grid(row=0, column=3, sticky=E)

        self.to_choices = StringVar()
        self.combobox_to = ttk.Combobox(self.frame, textvariable=self.to_choices)
        self.combobox_to['values'] = ['UTF-8', 'Base64', 'HTML', 'Unicode']
        self.combobox_to.state(["readonly"])
        self.combobox_to.current(0)
        self.combobox_to.grid(row=0, column=4, sticky=E)

        self.convert_button = ttk.Button(self.frame, text="Convert", command=self.convert_now)
        self.convert_button.grid(row=2, column=4, sticky=E, pady=5)

        # Start mainloop
        self.window.mainloop()

    def convert_now(self):
        from_text = self.from_choices.get()
        to_text = self.to_choices.get()
        converted_text = self.converter.converting_text(from_text, to_text, self.convert_from_text.get('1.0', 'end'))
        self.output_window = Toplevel(self.window)
        self.output_window.configure(pady=10, padx=10)
        self.output_window.title("converted text")
        self.output_textbox = scrolledtext.ScrolledText(self.output_window, width=80, height=15)
        self.output_textbox.grid(row=0, column=0)
        self.output_textbox.insert('1.0', converted_text)
