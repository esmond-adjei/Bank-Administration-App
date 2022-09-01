from tkinter import *
from gui_operations import *

def admin_login():
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "Admin Login"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH = 30
    BTNx = BTN_WIDTH*8

    # WINDOW SETUP
    root = Tk()
    root.title("DIGESJC BANK TICKETING SYSTEM")
    root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    root.resizable(False,False)
    root.configure(bg=THEME_LIGHT)

    Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*14),y=WIN_HEIGHT*0.2)
    
    passwordvalue = ''
    PASS_LABEL = 'Enter Password'
    Label(root, text=PASS_LABEL, font=f'{DEFAULT_FONT} 14', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.4)
    Entry(root, textvariable=passwordvalue, font= f'{DEFAULT_FONT} 14', fg='#666', width=int(BTN_WIDTH*0.65), bd=0).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.5)
    Button(root, text="Submit",font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=1,command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.6)

    root.mainloop()

def teller_login():
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "Teller Login"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH = 30
    BTNx = BTN_WIDTH*8

    # WINDOW SETUP
    root = Tk()
    root.title("DIGESJC BANK TICKETING SYSTEM")
    root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    root.resizable(False,False)
    root.configure(bg=THEME_LIGHT)

    Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.1)
    
    passwordvalue, teller_id = '', IntVar()
    PASS_LABEL, ID_LABLE = 'Enter Password', 'Enter Teller ID'
    Label(root, text=ID_LABLE, font=f'{DEFAULT_FONT} 14', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(ID_LABLE)*10),y=WIN_HEIGHT*0.3)
    Entry(root, textvariable=teller_id, font= f'{DEFAULT_FONT} 14', fg='#666', width=int(BTN_WIDTH*0.65), bd=0).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.4)
    Label(root, text=PASS_LABEL, font=f'{DEFAULT_FONT} 14', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.5)
    Entry(root, textvariable=passwordvalue, font= f'{DEFAULT_FONT} 14', fg='#666', width=int(BTN_WIDTH*0.65), bd=0).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.6)
    Button(root, text="Submit",font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=1,command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.7)

    root.mainloop()
    
def customer_page():
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "How May We Help You?"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH, BTN_HEIGHT = 15, 3
    BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
    Mx, My = place_center(WIN_WIDTH, BTN_WIDTH), place_center(WIN_HEIGHT, BTN_HEIGHT)
    GAP = int((WIN_WIDTH-BTNx*3)/4)

    # WINDOW SETUP
    root = Tk()
    root.title("DIGESJC BANK TICKETING SYSTEM")
    root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    root.resizable(False,False)
    root.configure(bg=THEME_LIGHT)

    Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.2)
    
    Button(root, text="Deposit", font=f'{DEFAULT_FONT} 10', bd=0, bg='#975318', fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP, y=My)
    Button(root, text="Withdraw", font=f'{DEFAULT_FONT} 10', bd=0, bg='#2468ac', fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*2+BTNx, y=My)
    Button(root, text="Transfer",font=f'{DEFAULT_FONT} 10', bd=0, bg='#70f', fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*3+BTNx*2, y=My)


    root.mainloop()