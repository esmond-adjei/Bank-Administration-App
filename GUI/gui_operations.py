from tkinter import *


def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

def generate_content(content_type, data, win_props={}):
    BTN_WIDTH, BTN_HEIGHT = win_props['DEFAULT_FONT_SIZE']+5, 3

    if content_type=='button':
        # buttons setup
        BTN_WIDTH, BTN_HEIGHT = win_props['DEFAULT_FONT_SIZE']+5, 3
        BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
        Mx, My = place_center(win_props['WIN_WIDTH'], BTN_WIDTH), place_center(win_props['WIN_HEIGHT'], BTN_HEIGHT)
        no_of_users = len(data['options'])
        GAP = int((win_props['WIN_WIDTH']-BTNx*no_of_users)/(no_of_users+1))
        
        for opt in range(len(data['options'])):
            Button(win_props['root'], text=data['options'][opt], font=f"{win_props['DEFAULT_FONT']} {win_props['DEFAULT_FONT_SIZE']}", 
                bd=0, bg=win_props['THEME_DARK'], fg=win_props['THEME_LIGHT'], width=BTN_WIDTH, height=BTN_HEIGHT,
                command=data['command'][opt]).place(x=GAP*(opt+1)+BTNx*(opt), y=My)
