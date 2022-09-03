from tkinter import *
from turtle import back


def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

def transframe(frame_1, frame_2, back_forward):    
    if back_forward in ('back', 'f'):
        print('going back', frame_2)
        frame_1.pack()
        frame_2.pack_forget(fill='both', expand=1)
    elif back_forward in ('forward', 'b'):
        frame_1.pack_forget()
        frame_2.pack(fill='both', expand=1)

    # frame = Frame()
    # ## back button
    # Button(frame, text="<< Go Back",
    #        font=f'{DEFAULT_FONT} 10', 
    #        bd=0, bg='#d4af37',
    #        fg=THEME_DARK,
    #        width=BTN_WIDTH, 
    #        height=1,
    #        command=lambda:transframe(frame, preframe,'b')
    #        ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.8)


# def generate_content(content_type, data, current_frame, win_props={}):

#     if content_type=='button':
#         # buttons setup
#         BTN_WIDTH, BTN_HEIGHT = win_props['DEFAULT_FONT_SIZE']+5, 3
#         BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
#         Mx = place_center(win_props['WIN_WIDTH'], BTN_WIDTH)
#         My = place_center(win_props['WIN_HEIGHT'], BTN_HEIGHT)
#         no_of_users = len(data['options'])
#         GAP = int((win_props['WIN_WIDTH']-BTNx*no_of_users)/(no_of_users+1))
        
#         # unpack data
#         button_names = data['options']
#         button_commands = data['commands']
#         frames = data['frames']

#         for opt in range(len(button_names)):
#             # print(type(data['commands'][opt]))
#             Button(current_frame, 
#                    text=data['options'][opt], 
#                    font=f"{win_props['DEFAULT_FONT']} {win_props['DEFAULT_FONT_SIZE']}", 
#                    bd=0, 
#                    bg=win_props['THEME_DARK'], 
#                    fg=win_props['THEME_LIGHT'], 
#                    width=BTN_WIDTH, 
#                    height=BTN_HEIGHT,
#                    command=lambda: button_commands[0](frames[0])
#                    ).place(x=GAP*(opt+1)+BTNx*(opt), y=My)

