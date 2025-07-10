import tkinter as tk
from tkinter import ttk, messagebox

# Color scheme
BG_COLOR = "#f5f5f5"
PRIMARY_COLOR = "#4a6fa5"
SECONDARY_COLOR = "#166088"
TEXT_COLOR = "#333333"
ENTRY_BG = "#ffffff"
BUTTON_HOVER = "#3a5a8a"

def convert_temperature():
    try:
        value = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32

        # Update result with colored text
        label_result.config(text=f"{result:.2f}° {to_unit}", fg=SECONDARY_COLOR)
        
        # Add to history
        history_text.config(state=tk.NORMAL)
        if history_text.index('end-1c') != '1.0':
            history_text.insert(tk.END, "\n")
        history_text.insert(tk.END, f"{value:.2f}° {from_unit} → {result:.2f}° {to_unit}")
        history_text.config(state=tk.DISABLED)
        history_text.see(tk.END)
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        label_result.config(text="", fg=SECONDARY_COLOR)

def on_enter(e):
    convert_button['background'] = BUTTON_HOVER

def on_leave(e):
    convert_button['background'] = PRIMARY_COLOR

# GUI Window Setup
root = tk.Tk()
root.title("Professional Temperature Converter")
root.geometry("500x600")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Main container
main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Header
header = tk.Label(
    main_frame,
    text="Temperature Converter",
    font=('Arial', 20, 'bold'),
    bg=BG_COLOR,
    fg=PRIMARY_COLOR
)
header.pack(pady=(0, 20))

# Input Frame
input_frame = tk.Frame(main_frame, bg=BG_COLOR)
input_frame.pack(fill=tk.X, pady=(0, 15))

# Temperature Entry
tk.Label(
    input_frame,
    text="Enter Temperature:",
    font=('Arial', 12),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack(anchor='w')

entry_temp = tk.Entry(
    input_frame,
    font=('Arial', 14),
    bg=ENTRY_BG,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightcolor=PRIMARY_COLOR,
    highlightbackground="#cccccc"
)
entry_temp.pack(fill=tk.X, pady=(5, 15), ipady=5)

# Conversion Units Frame
units_frame = tk.Frame(main_frame, bg=BG_COLOR)
units_frame.pack(fill=tk.X, pady=(0, 20))

# From Unit
from_frame = tk.Frame(units_frame, bg=BG_COLOR)
from_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

tk.Label(
    from_frame,
    text="From:",
    font=('Arial', 12),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack(anchor='w')

combo_from = ttk.Combobox(
    from_frame,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    font=('Arial', 12),
    state="readonly"
)
combo_from.current(0)
combo_from.pack(fill=tk.X, pady=(5, 0), ipady=3)

# To Unit
to_frame = tk.Frame(units_frame, bg=BG_COLOR)
to_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(15, 0))

tk.Label(
    to_frame,
    text="To:",
    font=('Arial', 12),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack(anchor='w')

combo_to = ttk.Combobox(
    to_frame,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    font=('Arial', 12),
    state="readonly"
)
combo_to.current(1)
combo_to.pack(fill=tk.X, pady=(5, 0), ipady=3)

# Convert Button
convert_button = tk.Button(
    main_frame,
    text="CONVERT",
    font=('Arial', 12, 'bold'),
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=SECONDARY_COLOR,
    activeforeground="white",
    relief=tk.FLAT,
    command=convert_temperature,
    cursor="hand2"
)
convert_button.pack(fill=tk.X, pady=(10, 20), ipady=8)
convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Result Frame
result_frame = tk.Frame(main_frame, bg=BG_COLOR)
result_frame.pack(fill=tk.X, pady=(0, 20))

tk.Label(
    result_frame,
    text="Result:",
    font=('Arial', 12),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack(anchor='w')

label_result = tk.Label(
    result_frame,
    text="",
    font=('Arial', 16, 'bold'),
    bg=BG_COLOR,
    fg=SECONDARY_COLOR
)
label_result.pack(anchor='w', pady=(5, 0))

# History Frame
history_frame = tk.LabelFrame(
    main_frame,
    text=" Conversion History ",
    font=('Arial', 11),
    bg=BG_COLOR,
    fg=SECONDARY_COLOR,
    relief=tk.FLAT,
    labelanchor='n'
)
history_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

# History Text
history_text = tk.Text(
    history_frame,
    height=6,
    font=('Arial', 11),
    wrap=tk.WORD,
    bg=ENTRY_BG,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightcolor="#cccccc",
    highlightbackground="#cccccc",
    padx=10,
    pady=10,
    state=tk.DISABLED
)
history_text.pack(fill=tk.BOTH, expand=True)

# Clear History Button
clear_button = tk.Button(
    history_frame,
    text="Clear History",
    font=('Arial', 10),
    bg="#e0e0e0",
    fg=TEXT_COLOR,
    activebackground="#d0d0d0",
    relief=tk.FLAT,
    command=lambda: [history_text.config(state=tk.NORMAL), 
                    history_text.delete(1.0, tk.END),
                    history_text.config(state=tk.DISABLED)]
)
clear_button.pack(side=tk.RIGHT, pady=(5, 5))

# Bind Enter key to conversion
root.bind('<Return>', lambda event: convert_temperature())

# Focus on entry when app starts
entry_temp.focus()

root.mainloop()