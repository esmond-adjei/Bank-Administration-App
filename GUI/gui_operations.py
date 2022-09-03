from tkinter import *


def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

def generate_content(content_type, data, current_frame, win_props={}):

    if content_type=='button':
        # buttons setup
        BTN_WIDTH, BTN_HEIGHT = win_props['DEFAULT_FONT_SIZE']+5, 3
        BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
        Mx = place_center(win_props['WIN_WIDTH'], BTN_WIDTH)
        My = place_center(win_props['WIN_HEIGHT'], BTN_HEIGHT)
        no_of_users = len(data['options'])
        GAP = int((win_props['WIN_WIDTH']-BTNx*no_of_users)/(no_of_users+1))
        
        # unpack data
        button_names = data['options']
        button_commands = data['commands']
        frames = data['frames']

        for opt in range(len(button_names)):
            # print(type(data['commands'][opt]))
            Button(current_frame, 
                   text=data['options'][opt], 
                   font=f"{win_props['DEFAULT_FONT']} {win_props['DEFAULT_FONT_SIZE']}", 
                   bd=0, 
                   bg=win_props['THEME_DARK'], 
                   fg=win_props['THEME_LIGHT'], 
                   width=BTN_WIDTH, 
                   height=BTN_HEIGHT,
                   command=lambda: button_commands[0](frames[0])
                   ).place(x=GAP*(opt+1)+BTNx*(opt), y=My)
