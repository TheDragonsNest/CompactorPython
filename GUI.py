import tkinter as tk


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.panel_amount
        for i in range(panel_amount):
            GUI_Frame.pack()


class GUI_Frame(tk.Frame):
    def __init__(self, text):
        super().__init__()
        self.label = tk.Label(text)
        self.entry = tk.Entry()
        self.button = tk.Button()


if __name__ == '__main__':
    window = tk.Tk()
    label = tk.Label(text="Name")
    entry = tk.Entry()
    label.pack()
    entry.pack()
