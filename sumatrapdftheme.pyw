import tkinter as tk
from tkinter import messagebox
import re

# User-configurable settings
FONT_NAME = "Arial"
FONT_SIZE = 16
WINDOW_SIZE = '350x350'
FILE_PATH = 'SumatraPDF-settings.txt'

# Themes configuration
THEMES = {
    'default': {
        'TextColor': '#000000',
        'BackgroundColor': '#ffffff',
        'GradientColors': '#f2f2f2'
    },
    'light': {
        'TextColor': '#000000',
        'BackgroundColor': '#ffffff',
        'GradientColors': '#ffffff'
    },
    'dark': {
        'TextColor': '#F8F8F2',
        'BackgroundColor': '#282828',
        'GradientColors': '#282828'
    },
    'sepia': {
        'TextColor': '#000000',
        'BackgroundColor': '#F4ECD8',
        'GradientColors': '#F4ECD8'
    },
    'dark_sepia': {
        'TextColor': '#EBDBB2',
        'BackgroundColor': '#282828',
        'GradientColors': '#282828'
    }
}

# Function to apply theme settings
def apply_theme_settings(theme, file_path=FILE_PATH):
    if theme not in THEMES:
        raise ValueError("Invalid theme specified")

    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "Settings file not found.")
        return

    def replace_setting(match):
        setting_name = match.group(1)
        if setting_name in THEMES[theme]:
            return f'{setting_name} = {THEMES[theme][setting_name]}'
        return match.group(0)

    fixed_page_ui_pattern = re.compile(r'(TextColor|BackgroundColor|GradientColors) = #[0-9a-fA-F]+')
    updated_content = fixed_page_ui_pattern.sub(replace_setting, content)

    if 'GradientColors' not in content:
        fixed_page_ui_start = content.find('FixedPageUI [') + len('FixedPageUI [')
        updated_content = updated_content[:fixed_page_ui_start] + f'\n\tGradientColors = {THEMES[theme].get("GradientColors", "")}' + updated_content[fixed_page_ui_start:]

    with open(file_path, 'w') as file:
        file.write(updated_content)

    messagebox.showinfo("Success", "Theme applied successfully!")

# GUI setup
class ThemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SumatraPDF Theme Changer")
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg='#f0f0f0')

        self.label = tk.Label(root, text="Select Theme:", font=(FONT_NAME, FONT_SIZE, 'bold'), bg='#f0f0f0')
        self.label.pack(pady=20)

        self.theme_var = tk.StringVar(value='default')
        self.themes = THEMES.keys()

        self.radio_buttons = []
        for theme_name in self.themes:
            rb = tk.Radiobutton(root, text=theme_name.capitalize(), variable=self.theme_var, value=theme_name, font=(FONT_NAME, FONT_SIZE), bg='#f0f0f0')
            rb.pack(anchor='w', padx=20)
            self.radio_buttons.append(rb)

        self.apply_button = tk.Button(root, text="Apply", command=self.apply_theme, font=(FONT_NAME, FONT_SIZE, 'bold'), bg='#4caf50', fg='#ffffff', activebackground='#45a049', activeforeground='#ffffff')
        self.apply_button.pack(pady=20)

    def apply_theme(self):
        selected_theme = self.theme_var.get()
        apply_theme_settings(selected_theme)

if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeApp(root)
    root.mainloop()
