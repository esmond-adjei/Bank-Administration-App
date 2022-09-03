from tkinter import *
# from views import *


def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

# admin_page
def admin_login(frame, preframe):
    ## FRAME SETUP
    preframe.pack_forget()
    frame.pack(fill='both', expand=1)
    
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "Admin Login"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH = 30
    BTNx = BTN_WIDTH*8

    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*14),y=WIN_HEIGHT*0.2)
    
    PASS_LABEL = 'Enter Password'
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.4)
    
    Entry(frame, show='*', 
         font= f'{DEFAULT_FONT} 14', 
         fg='#666', 
         width=int(BTN_WIDTH*0.65), 
         bd=1).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.5)
    
    Button(frame, text="Submit",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.6)
    
    Button(frame, text="Go Back",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#d4af37', 
           fg=THEME_DARK, 
           width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.8)

# teller_page 
def teller_login(frame,preframe):
    ## FRAME SETUP
    preframe.pack_forget()
    frame.pack(fill='both', expand=1)
    
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "Teller Login"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH = 30
    BTNx = BTN_WIDTH*8

    Label(frame,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.1)
    
    passwordvalue, teller_id = '', IntVar()
    PASS_LABEL, ID_LABLE = 'Enter Password', 'Enter Teller ID'
    Label(frame, text=ID_LABLE, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(ID_LABLE)*10),y=WIN_HEIGHT*0.3)
    
    Entry(frame, textvariable=teller_id, 
          font= f'{DEFAULT_FONT} 14', 
          fg='#666', 
          width=int(BTN_WIDTH*0.65), 
          bd=0).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.4)
    
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.5)
    
    Entry(frame, textvariable=passwordvalue, 
          font= f'{DEFAULT_FONT} 14', 
          fg='#666', 
          width=int(BTN_WIDTH*0.65), 
          bd=0).place(x=place_center(WIN_WIDTH,BTNx),y=WIN_HEIGHT*0.6)
    
    Button(frame, text="Submit",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.7)

    Button(frame, text="<< Go Back",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#d4af37', 
           fg=THEME_DARK, 
           width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.8)
    
# customer_page
def customer_page(frame, preframe):
    ## FRAME SETUP
    prev_frame = preframe
    preframe.pack_forget()
    frame.pack(fill='both', expand=1)
    
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "How May We Help You?"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'


    # BTN_WIDTH, BTN_HEIGHT = window_properties['DEFAULT_FONT_SIZE']+5, 3
    # Mx = place_center(640, 30)
    My = place_center(360, 3)

    ## --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH, BTN_HEIGHT = 15, 3
    BTNx = BTN_WIDTH*8
    BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
    # no_of_users = len(options)
    GAP = int((640-BTNx*3)/(3+1))

    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.2)
    
    Button(frame, text="Deposit", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#975318', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command='').place(x=GAP, y=My)
    Button(frame, text="Withdraw", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#2468ac', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command='').place(x=GAP*2+BTNx, y=My)
    Button(frame, text="Transfer",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#70f', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command='').place(x=GAP*3+BTNx*2, y=My)

    Button(frame, text="<< Go Back",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=lambda: prev_frame.pack()).place(x=place_center(WIN_WIDTH, BTNx), y=WIN_HEIGHT*0.8)


root = Tk()

WIN_WIDTH=640
WIN_HEIGHT=360
DEFAULT_FONT='montserrat'
DEFAULT_FONT_SIZE=10
THEME_DARK='#283A73'
THEME_LIGHT='#ccc'

# WINDOW SETUP
root.title("DIGESJC BANK TICKETING SYSTEM")
root.iconbitmap("./Snip/bankicon.ico")
root.geometry(f"640x360")
# root.configure(bg=THEME_LIGHT)
root.resizable(False,False)
# root.configure(bg='#ff0000')


# HOME PAGE
frame = Frame(root, bg=THEME_LIGHT)
frame.pack(fill='both',expand=1)

## HEADER TEXT
HEADING = "Welcome to DIGESJC Bank"
header_1 = Label(frame,text=HEADING,
        font=f"{DEFAULT_FONT} 18 bold", 
        bg=THEME_LIGHT, 
        fg=THEME_DARK)
header_2 = Label(frame,text='Select a User',
        font=f"{DEFAULT_FONT} 15", 
        bg=THEME_LIGHT, 
        fg=THEME_DARK)  

header_1.place(x=place_center(WIN_WIDTH,len(HEADING)*14),
        y=WIN_HEIGHT*0.2)
header_2.place(x=place_center(WIN_WIDTH,len('Select a User')*10),
        y=WIN_HEIGHT*0.3)

## BUTTONS
options = ['Admin', 'Teller', 'Customer']
newframe = Frame(root, bg=THEME_LIGHT)
# commands = [admin_login, teller_login, customer_page]

BTN_WIDTH, BTN_HEIGHT = DEFAULT_FONT_SIZE+5, 3
BTNx, BTNy = BTN_WIDTH*8, BTN_HEIGHT*8
# Mx = place_center(WIN_WIDTH, BTN_WIDTH)
My = place_center(WIN_HEIGHT, BTN_HEIGHT)
no_of_users = len(options)
GAP = int((WIN_WIDTH-BTNx*no_of_users)/(no_of_users+1))

admin_btn= Button(frame, 
            text=options[0], 
            font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
            bd=0, 
            bg=THEME_DARK, 
            fg=THEME_LIGHT, 
            width=BTN_WIDTH, 
            height=BTN_HEIGHT,
            command=lambda: admin_login(newframe, frame)
            ).place(x=GAP*(0+1)+BTNx*(0), y=My)

teller_btn = Button(frame, 
            text=options[1], 
            font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
            bd=0, 
            bg=THEME_DARK, 
            fg=THEME_LIGHT, 
            width=BTN_WIDTH, 
            height=BTN_HEIGHT,
            command=lambda: teller_login(newframe, frame)
            ).place(x=GAP*(1+1)+BTNx*(1), y=My)

customer_btn = Button(frame, 
            text=options[2], 
            font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
            bd=0, 
            bg=THEME_DARK, 
            fg=THEME_LIGHT, 
            width=BTN_WIDTH, 
            height=BTN_HEIGHT,
            command=lambda: customer_page(newframe, frame)
            ).place(x=GAP*(2+1)+BTNx*(2), y=My)


root.mainloop()

