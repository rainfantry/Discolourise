# Discord Markdown Color Formatter

Convert markdown to Discord ANSI colored text blocks.

## Supported Syntax

| Markdown | Color Output |
|----------|--------------|
| `# Header` | **Yellow Bold** |
| `## Header` | **Cyan Bold** |
| `### Header` | **Green Bold** |
| `` `code` `` | Red |
| `**bold**` | **White Bold** |
| `*italic*` | Pink |
| `- bullet` | Cyan bullet |

## Usage

### CLI Version
```bash
python discord_color.py
```
Then paste your markdown, type `END` on a new line, get output.

### GUI Version
```bash
python discord_color_gui.py
```

### Build EXE (Windows)
```batch
build_exe.bat
```
or
```batch
build_gui_exe.bat
```

## Direct ANSI Codes

For custom colors, use in Discord:
```
\u001b[0;31m = Red
\u001b[0;32m = Green
\u001b[0;33m = Yellow
\u001b[0;34m = Blue
\u001b[0;35m = Pink
\u001b[0;36m = Cyan
\u001b[0;37m = White
\u001b[1;XXm = Bold version
\u001b[0m = Reset
```

## Example

Input:
```
# Task 1c: Troubleshooting

## Procedure 1
Check if interface is up: `ip link show eth0`

## Procedure 2
- Check IP config
- Check routing
```

Output (paste in Discord):
```ansi
[1;33mTask 1c: Troubleshooting[0m

[1;36mProcedure 1[0m
Check if interface is up: [0;31mip link show eth0[0m

[1;36mProcedure 2[0m
[0;36m•[0m Check IP config
[0;36m•[0m Check routing
```
