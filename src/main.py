import tkinter as tk

# Constants for configuration
WINDOW_TITLE = "Calculator"
WINDOW_SIZE = "400x600"
BACKGROUND_COLOR = "lightgray"
DISPLAY_FONT = ("Arial", 24)
BUTTON_FONT = ("Arial", 18)
BUTTON_WIDTH = 5
BUTTON_HEIGHT = 2

# Button layout and properties
BUTTONS = [
    ("C", "#ff6666"),
    ("", ""),
    ("", ""),
    ("", ""),
    ("7", "white"),
    ("8", "white"),
    ("9", "white"),
    ("/", "#6666ff"),
    ("4", "white"),
    ("5", "white"),
    ("6", "white"),
    ("*", "#6666ff"),
    ("1", "white"),
    ("2", "white"),
    ("3", "white"),
    ("-", "#6666ff"),
    ("0", "white"),
    (".", "white"),
    ("=", "#66ff66"),
    ("+", "#6666ff"),
]


class Calculator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.expression = ""
        self.create_widgets()

    def setup_window(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BACKGROUND_COLOR)

    def create_widgets(self):
        self.create_display()
        self.create_buttons()
        self.configure_grid()

    def create_display(self):
        self.display = tk.Entry(
            self.root, font=DISPLAY_FONT, borderwidth=2, relief="solid", justify="right"
        )
        self.display.grid(
            row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew"
        )

    def create_buttons(self):
        row_val = 1
        col_val = 0
        for label, color in BUTTONS:
            if label:
                self.create_button(label, color, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, label, color, row, column):
        action = lambda x=label: self.on_button_click(x)
        button = tk.Button(
            self.root,
            text=label,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            font=BUTTON_FONT,
            command=action,
            bg=color,
            relief="flat",
        )
        button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def configure_grid(self):
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.clear_expression()
        elif char == "=":
            self.calculate_expression()
        else:
            self.update_expression(char)

    def clear_expression(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate_expression(self):
        try:
            result = str(eval(self.expression))
            self.display_result(result)
            self.expression = result
        except:
            self.display_error()
            self.expression = ""

    def update_expression(self, char):
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def display_result(self, result):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)

    def display_error(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
