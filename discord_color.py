#!/usr/bin/env python3
"""
Discord Markdown Color Formatter
Converts markdown-style text to Discord ANSI colored code blocks
"""

import re
import sys
import pyperclip

# Discord ANSI color codes
COLORS = {
    'gray': '30', 'red': '31', 'green': '32', 'yellow': '33',
    'blue': '34', 'pink': '35', 'cyan': '36', 'white': '37'
}

STYLES = {
    'bold': '1', 'underline': '4', 'normal': '0'
}

# Presets for markdown elements
PRESETS = {
    'h1': '\u001b[1;33m',      # Bold Yellow - # Headers
    'h2': '\u001b[1;36m',      # Bold Cyan - ## Headers
    'h3': '\u001b[1;32m',      # Bold Green - ### Headers
    'code': '\u001b[0;31m',    # Red - `code`
    'bold': '\u001b[1;37m',    # Bold White - **bold**
    'italic': '\u001b[0;35m', # Pink - *italic*
    'bullet': '\u001b[0;36m', # Cyan - bullet points
    'reset': '\u001b[0m'
}

def convert_markdown_to_discord(text):
    """Convert markdown to Discord ANSI format"""
    lines = text.split('\n')
    result = []

    for line in lines:
        converted = line

        # Headers
        if line.startswith('### '):
            converted = f"{PRESETS['h3']}{line[4:]}{PRESETS['reset']}"
        elif line.startswith('## '):
            converted = f"{PRESETS['h2']}{line[3:]}{PRESETS['reset']}"
        elif line.startswith('# '):
            converted = f"{PRESETS['h1']}{line[2:]}{PRESETS['reset']}"
        else:
            # Inline code `code`
            converted = re.sub(
                r'`([^`]+)`',
                f"{PRESETS['code']}\\1{PRESETS['reset']}",
                converted
            )
            # Bold **text**
            converted = re.sub(
                r'\*\*([^*]+)\*\*',
                f"{PRESETS['bold']}\\1{PRESETS['reset']}",
                converted
            )
            # Italic *text*
            converted = re.sub(
                r'(?<!\*)\*([^*]+)\*(?!\*)',
                f"{PRESETS['italic']}\\1{PRESETS['reset']}",
                converted
            )
            # Bullet points
            if line.strip().startswith('- '):
                converted = f"{PRESETS['bullet']}•{PRESETS['reset']} {line.strip()[2:]}"

        result.append(converted)

    # Wrap in Discord ansi code block
    output = "```ansi\n" + '\n'.join(result) + "\n```"
    return output


def interactive_mode():
    """Interactive CLI mode"""
    print("=" * 50)
    print("  DISCORD MARKDOWN COLOR FORMATTER")
    print("=" * 50)
    print("\nSupported syntax:")
    print("  # Header 1     → Yellow bold")
    print("  ## Header 2    → Cyan bold")
    print("  ### Header 3   → Green bold")
    print("  `code`         → Red")
    print("  **bold**       → White bold")
    print("  *italic*       → Pink")
    print("  - bullet       → Cyan bullet")
    print("\nCommands: 'quit' to exit, 'help' for colors")
    print("-" * 50)

    while True:
        print("\nPaste your markdown (type 'END' on new line when done):")
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == 'END':
                    break
                if line.strip().lower() == 'quit':
                    print("Goodbye!")
                    return
                if line.strip().lower() == 'help':
                    show_colors()
                    break
                lines.append(line)
            except EOFError:
                break

        if lines:
            text = '\n'.join(lines)
            result = convert_markdown_to_discord(text)
            print("\n" + "=" * 50)
            print("COPY THIS TO DISCORD:")
            print("=" * 50)
            print(result)

            try:
                pyperclip.copy(result)
                print("\n✓ Copied to clipboard!")
            except:
                print("\n(Install pyperclip for auto-copy: pip install pyperclip)")


def show_colors():
    """Show available color codes"""
    print("\nDirect ANSI codes you can use:")
    print("```ansi")
    for name, code in COLORS.items():
        print(f"\\u001b[0;{code}m{name}\\u001b[0m = [0;{code}m")
    print("```")
    print("\nAdd 1; for bold: \\u001b[1;31mBold Red\\u001b[0m")


def main():
    if len(sys.argv) > 1:
        # File mode
        with open(sys.argv[1], 'r') as f:
            text = f.read()
        print(convert_markdown_to_discord(text))
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
