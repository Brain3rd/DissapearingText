from tkinter import *
from tkinter import messagebox


BTN_COLOR = "#1e2022"
CANVAS_COLOR = "#dddddd"
BG_COLOR = '#52616b'
FONT_COLOR = '#c9d6df'


class App:

    def __init__(self):
        self.timer = None
        self.type_list = []
        self.canvas_list = []

        # Window
        self.window = Tk()
        self.window.title("Disappearing Text")
        self.window.resizable(width=False, height=False)
        self.window.configure(background=BTN_COLOR)
        self.window.geometry("+700+100")

        # Entry
        self.entry = Entry(bg=CANVAS_COLOR)
        self.entry.bind('<Key>', self.key_pressed)
        self.entry.grid(row=2, column=1, sticky="we", pady=(20, 20), padx=(20, 20), ipady=2)

        # Canvas
        self.canvas = Canvas(width=600, height=300, bg=CANVAS_COLOR)
        self.canvas_text = self.canvas.create_text(300, 300, text='', width=550, font=('calibre', 20, 'bold'), anchor=S)
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="we", pady=(20, 20), padx=(20, 20), ipady=2)

        # Timer_label
        self.label = Label(
            text="Click start and begin to write.\nIf you stop for 5-10 seconds, your text will disappear.",
            font=('calibre', 20, 'bold'),
            bg=BTN_COLOR, fg=FONT_COLOR
        )
        self.label.grid(column=1, row=1, sticky="we", pady=(3, 3), padx=(10, 10), ipady=2)

        # Button
        button = Button(text='Start', font=('arial', 12, 'bold'), command=self.start_timer, bg=BG_COLOR, fg=FONT_COLOR)
        button.grid(column=2, row=2, sticky="we", pady=(3, 3), padx=(10, 10), ipady=2)

        # ABOUT POPUP #
        def about_message():
            messagebox.showinfo(
                "Disappearing text", "Need to keep writing or text will disappear.")

        button_about = Button(
            text="About", command=about_message, bg=BG_COLOR, fg=FONT_COLOR, font=('arial', 8, 'bold'))
        button_about.grid(row=2, column=0, sticky="we", ipady=2, pady=(3, 3), padx=(10, 10))

        self.window.mainloop()

    # Countdown timer
    def count_down(self, count):
        # Start counting time
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        # When time is 0
        if count == 0:
            self.entry.delete(0, 'end')
            if len(self.type_list) > 0:
                self.type_list.clear()
                # If you typed enough give you more time
                self.count_down(5)
            else:
                # Clear text from canvas, start timer again
                self.canvas.itemconfig(self.canvas_text, text='')
                self.canvas_list.clear()
                self.count_down(10)

    def start_timer(self):
        self.count_down(10)

    # This function monitor if keyboard get pressed
    def key_pressed(self, event):
        # Current key pressed
        current_type = event.char
        if current_type == '\x08':
            try:
                self.type_list.pop()
                self.canvas_list.pop()
            except IndexError:
                pass
        else:
            self.type_list.append(current_type)
            self.canvas_list.append(current_type)
        text_to_canvas = ''.join(self.canvas_list)
        self.canvas.itemconfig(self.canvas_text, text=text_to_canvas)
        print(self.type_list)


if __name__ == '__main__':
    App()
