#!/usr/bin/env python3
"""
Discord Markdown Color Formatter - GUI Version
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import re

# Discord ANSI color codes
PRESETS = {
    'h1': '\u001b[1;33m',      # Bold Yellow
    'h2': '\u001b[1;36m',      # Bold Cyan
    'h3': '\u001b[1;32m',      # Bold Green
    'code': '\u001b[0;31m',    # Red
    'bold': '\u001b[1;37m',    # Bold White
    'italic': '\u001b[0;35m',  # Pink
    'bullet': '\u001b[0;36m',  # Cyan
    'reset': '\u001b[0m'
}

COLORS = {
    'Gray': '30', 'Red': '31', 'Green': '32', 'Yellow': '33',
    'Blue': '34', 'Pink': '35', 'Cyan': '36', 'White': '37'
}


def convert_markdown_to_discord(text):
    lines = text.split('\n')
    result = []

    for line in lines:
        converted = line

        if line.startswith('### '):
            converted = f"{PRESETS['h3']}{line[4:]}{PRESETS['reset']}"
        elif line.startswith('## '):
            converted = f"{PRESETS['h2']}{line[3:]}{PRESETS['reset']}"
        elif line.startswith('# '):
            converted = f"{PRESETS['h1']}{line[2:]}{PRESETS['reset']}"
        else:
            converted = re.sub(r'`([^`]+)`', f"{PRESETS['code']}\\1{PRESETS['reset']}", converted)
            converted = re.sub(r'\*\*([^*]+)\*\*', f"{PRESETS['bold']}\\1{PRESETS['reset']}", converted)
            converted = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', f"{PRESETS['italic']}\\1{PRESETS['reset']}", converted)
            if line.strip().startswith('- '):
                converted = f"{PRESETS['bullet']}•{PRESETS['reset']} {line.strip()[2:]}"

        result.append(converted)

    return "```ansi\n" + '\n'.join(result) + "\n```"


class App:
    def __init__(self, root):
        self.root = root
        root.title("Discord Markdown Color Formatter")
        root.geometry("800x600")
        root.configure(bg='#36393f')

        style = ttk.Style()
        style.configure('TLabel', background='#36393f', foreground='white')
        style.configure('TButton', padding=5)

        # Input
        ttk.Label(root, text="INPUT (Markdown):").pack(pady=(10,5))
        self.input_text = scrolledtext.ScrolledText(root, height=12, bg='#40444b', fg='white',
                                                      insertbackground='white', font=('Consolas', 10))
        self.input_text.pack(fill='x', padx=10)

        # Buttons
        btn_frame = tk.Frame(root, bg='#36393f')
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Convert", command=self.convert).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Copy Output", command=self.copy_output).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear).pack(side='left', padx=5)

        # Color insert buttons
        color_frame = tk.Frame(root, bg='#36393f')
        color_frame.pack(pady=5)
        ttk.Label(color_frame, text="Insert Color:").pack(side='left', padx=5)
        for color, code in COLORS.items():
            btn = tk.Button(color_frame, text=color, width=6,
                           command=lambda c=code: self.insert_color(c))
            btn.pack(side='left', padx=2)

        # Output
        ttk.Label(root, text="OUTPUT (Copy to Discord):").pack(pady=(10,5))
        self.output_text = scrolledtext.ScrolledText(root, height=12, bg='#2f3136', fg='#7289da',
                                                       font=('Consolas', 10))
        self.output_text.pack(fill='x', padx=10, pady=(0,10))

        # Syntax help
        help_text = "Syntax: # H1 | ## H2 | ### H3 | `code` | **bold** | *italic* | - bullet"
        ttk.Label(root, text=help_text).pack()

    def convert(self):
        text = self.input_text.get("1.0", tk.END).strip()
        result = convert_markdown_to_discord(text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", result)

    def copy_output(self):
        text = self.output_text.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def insert_color(self, code):
        color_code = f"\\u001b[0;{code}m"
        reset_code = "\\u001b[0m"
        self.input_text.insert(tk.INSERT, f"{color_code}TEXT{reset_code}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
