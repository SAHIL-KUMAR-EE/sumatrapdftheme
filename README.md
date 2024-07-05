# SumatraPDF Theme Changer
![main](https://github.com/SAHIL-KUMAR-EE/sumatrapdftheme/assets/121251129/adc8909a-8a36-4d04-9a4a-6c0e95f75f43)

### Simple Python Script to allow the users to change themes in Sumatra PDF reader easily
## Contents
- [Changing Theme](#changing-theme)
- [Script Usage](#script-usage)
- [Custom Themes](#custom-themes)
- [Disclaimer](#disclaimer)

## Changing theme
To change the theme in Sumatra PDF Reader:

1. Click on the Hamburger menu in the top left corner.

![top_menu](https://github.com/SAHIL-KUMAR-EE/sumatrapdftheme/assets/121251129/3c5df68c-0805-485d-b853-5abe0c68b951)

2. Select **Settings**.
3. Click on **Advanced Options**.

![advance_options](https://github.com/SAHIL-KUMAR-EE/sumatrapdftheme/assets/121251129/6c470f4f-d8c0-4d2d-8697-699d5db57285)

A notepad file will open up with content similar to this 
```txt
# For documentation, see https://www.sumatrapdfreader.org/settings/settings3-4-6.html
FixedPageUI [
	TextColor = #000000
	BackgroundColor = #ffffff
	SelectionColor = #f5fc0c
	WindowMargin = 2 4 2 4
	PageSpacing = 4 4
	GradientColors = #f2f2f2
	HideScrollbars = false
]
ComicBookUI [
	WindowMargin = 0 0 0 0
	PageSpacing = 4 4
	CbxMangaMode = false
]
ChmUI [
	UseFixedPageUI = false
]
...
...
...
...
# Settings below are not recognized by the current version
```
*Note: You might not see GradientColors in FixedPageUI - Although it is the default setting you can choose to declare it yourself explicitly*

*Copy the following line*
`GradientColors = #f2f2f2`

To change the theme, you just have to manually change the following settings
```txt
	TextColor = #000000
	BackgroundColor = #ffffff
	GradientColors = #f2f2f2
```

For example, a simple dark theme could be - 
```txt
	TextColor = #ffffff
	BackgroundColor = #1e1e1e
	GradientColors = #1e1e1e
```
However this process can be quite repetitive and cumbersome, hence we can automate this with a simple Python script.

## Script Usage
To use the script, place it in the same folder as the `SumatraPDF-settings.txt`

If you save it elsewhere, you would have to specify the file path by right-clicking the file and opening it with your preferred code editor.

```
FILE_PATH = 'SumatraPDF-settings.txt'
```
to
```
FILE_PATH = 'YOUR_PATH'
```

To use it, simply double-click on it and it will open the Python Tkinter GUI.

## Custom Themes
You could add themes of your choice by modifying the following code
```py
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
    'YOUR_THEME': {
        'TextColor': 'HEX_CODE',
        'BackgroundColor': 'HEX_CODE',
        'GradientColors': 'HEX_CODE'
    },
}
```
Further, you can change other properties at your convenience
For example, we change
```py
# User-configurable settings
FONT_NAME = "Arial"
FONT_SIZE = 16
WINDOW_SIZE = '350x350'
FILE_PATH = 'SumatraPDF-settings.txt'
```
to
```py
# User-configurable settings
FONT_NAME = "Consolas"
FONT_SIZE = 22
WINDOW_SIZE = '500x400'
FILE_PATH = 'SumatraPDF-settings.txt'
```

## Disclaimer

I have made this script to help other readers change themes easily. I am not responsible for any damage caused by this Python script. Use it at your own risk.
