from tkinter import *
from views import *
from gui_operations import *

root = Tk()
window_properties = {
    'root':root,
    'WIN_WIDTH':640,
    'WIN_HEIGHT':360,
    'DEFAULT_FONT':'montserrat',
    'DEFAULT_FONT_SIZE':10,
    'THEME_DARK':'#283A73',
    'THEME_LIGHT':'#ccc',
}

# WINDOW SETUP
root.title("DIGESJC BANK TICKETING SYSTEM")
root.geometry(f"{window_properties['WIN_WIDTH']}x{window_properties['WIN_HEIGHT']}")
root.configure(bg=window_properties['THEME_LIGHT'])
root.resizable(False,False)

def user_page(window_properties):
    """commands for the user selection window"""


    program_sequence = {
        'options':['Admin', 'Teller', 'Customer'],
        'command':[admin_login, teller_login, customer_page, '']
    }

    ## MAIN CONTENT
    HEADING = "Welcome to DIGESJC Bank"
    Label(root,text=HEADING,font=f"{window_properties['DEFAULT_FONT']} 18 bold", bg=window_properties['THEME_LIGHT'], 
        fg=window_properties['THEME_DARK']).place(x=place_center(window_properties['WIN_WIDTH'],len(HEADING)*14),y=window_properties['WIN_HEIGHT']*0.2)
    Label(root,text='Select a User',font=f"{window_properties['DEFAULT_FONT']} 15", bg=window_properties['THEME_LIGHT'], 
        fg=window_properties['THEME_DARK']).place(x=place_center(window_properties['WIN_WIDTH'],len('Select a User')*10),y=window_properties['WIN_HEIGHT']*0.3)  
    generate_content('button', program_sequence, window_properties)


    root.mainloop()

user_page(window_properties)