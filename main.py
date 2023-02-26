import tkinter as tk
from tkinter import ttk, filedialog
import lex_analyzer as lex
import uuid

class Tooltip:
    active_tip = None

    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip = None
        self.id = None
        self.x = self.y = 0
        
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        if Tooltip.active_tip:
            Tooltip.active_tip.hide_tip()
        self.show_tip(event.x_root + 10, event.y_root + 10)

    def leave(self, event=None):
        self.hide_tip()

    def show_tip(self, x, y):
        if self.tip:
            return
        self.x, self.y = x, y
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tip, text=self.text, justify=tk.LEFT,
                         background="#FFFFFF", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
        Tooltip.active_tip = self

    def hide_tip(self):
        if self.tip:
            self.tip.destroy()
        self.tip = None

class Editor:
    def __init__(self, master):
        self.master = master
        self.master.title("Compilador X")
        #self.master.state('zoomed')
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.minimized_width = int(self.screen_width // 1.4)
        self.minimized_height = int(self.screen_height // 1.4)
        self.master.minsize(self.minimized_width, self.minimized_height)
        
        self.text = tk.Text(self.master, undo=True, maxundo=-1, autoseparators=True)
        self.text.pack(expand=True, fill="both")
        self.scrollbar = tk.Scrollbar(self.text)
        self.scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.toolbar = ttk.Frame(self.master)
        self.toolbar.pack(side="top", fill="x")

        self.open_button = ttk.Button(self.toolbar, text="Open File", command=self.open_file)
        self.open_button.pack(side="left")

        self.parse_button = ttk.Button(self.toolbar, text="Analizador Lexico", command=self.on_button_click)
        self.parse_button.pack(side="left")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.text.delete("1.0", "end")
                self.text.insert("end", file_contents)

    def on_button_click(self):
        tokens = lex.parse(self.text.get("1.0", "end").splitlines())
        for token in tokens:
            self.highlight_token(token, token.attributes.start_pos, token.attributes.end_pos, token.attributes.line)

    def highlight_token(self, token, start_position, end_position, line_number):
        start_index = f"{line_number+1}.{start_position}"
        end_index = f"{line_number+1}.{end_position}"
        uu = uuid.uuid4()

        color_type = {
            "KEYWORD": "#ffb347",
            "ID": "#90ee90",
            "NUMBER": "#87cefa",
            "STRING": "#87cefa",
            "OPERATOR": "#d5a6bd",
            "DELIMITER": "#c9c9c9",
            "UNKNOWN": "#ff9aa2",
        }

        tp_message = f"TYPE:{token.type}\nTOKEN:{token.token}\nLEXEME:{token.lexeme}\nLSE:({token.attributes.line},{token.attributes.start_pos},{token.attributes.end_pos})"

        tip = Tooltip(self.text, tp_message)
        self.text.tag_add(uu, start_index, end_index)
        self.text.tag_configure(uu, background=color_type[token.type])
        self.text.tag_bind(uu, "<Enter>", tip.enter)
        self.text.tag_bind(uu, "<Leave>", tip.leave)

def main():
    root = tk.Tk()
    Editor(root)
    root.mainloop()

if __name__ == '__main__':
    main()