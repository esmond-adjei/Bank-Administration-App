from tkinter import *
from tkinter.ttk import *
from gui_operations import *


def home_view(win_prop={}, frame=''):
    """layout for the home window.
      home_view is created directly in the main window. No frame is used.
      The structure is laid out here.
            - H1 heading
            - H2 heading
            - Option buttons
      NOTE: home_view create it's own frame, and the next frame for
            the next page.
    """
    
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT, DEFAULT_FONT_SIZE = win_prop['DEFAULT_FONT'], win_prop['DEFAULT_FONT_SIZE']
    
    ## FRAME SETUP
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both',expand=1)

    # HEADER TEXT (H1 & H2): Structure and placement
    HEADING = "Welcome to DIGESJC Bank"
    Label(frame,text=HEADING,
            font=f"{DEFAULT_FONT} 18 bold", 
            bg=THEME_LIGHT, 
            fg=THEME_DARK
            ).place(x=place_center(WIN_WIDTH,len(HEADING)*14),
                    y=WIN_HEIGHT*0.2)
    Label(frame,text='Select a User',
            font=f"{DEFAULT_FONT} 15", 
            bg=THEME_LIGHT, 
            fg=THEME_DARK
            ).place(x=place_center(WIN_WIDTH,len('Select a User')*10),
            y=WIN_HEIGHT*0.3)

    # BUTTONS
    ## Button varaibles
    options = ['Admin', 'Teller', 'Customer']
    commands = [admin_login, teller_login, customer_page]
    ## Button design variables
    no_of_users = len(options)
    BTN_WIDTH, BTN_HEIGHT = DEFAULT_FONT_SIZE+5, 3
    GAP = int((WIN_WIDTH-BTN_WIDTH*8*no_of_users)/(no_of_users+1))
    My = place_center(WIN_HEIGHT, BTN_HEIGHT)
    
    ## Button creation: using data and design varibles
    # Admin Button
    Button(frame, 
      text=options[0], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: commands[0](win_prop,frame)
      ).place(x=GAP*(0+1)+BTN_WIDTH*8*(0), y=My) 
    
    Button(frame, 
      text=options[1], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: commands[1](win_prop,frame)
      ).place(x=GAP*(1+1)+BTN_WIDTH*8*(1), y=My)

    Button(frame, 
      text=options[2], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: commands[2](win_prop,frame)
      ).place(x=GAP*(2+1)+BTN_WIDTH*8*(2), y=My)


def admin_login(win_prop,preframe):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 30

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Admin Login"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*12),y=WIN_HEIGHT*0.2)
    # password label
    PASS_LABEL = 'Enter Password'
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*9),y=WIN_HEIGHT*0.4)
    # password entry/input field
    Entry(frame, show='*', 
         font= f'{DEFAULT_FONT} 10', 
         fg='#666', 
         width=BTN_WIDTH, 
         bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.5)
    
    # submit button
    Button(frame, text="Login",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.6)
    ## back button
    BTN_WIDTH = BTN_WIDTH-15
    Button(frame, text="<<👈 Go Back",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37',
           fg=THEME_DARK,
           width=BTN_WIDTH, 
           height=1,
           command=lambda:go_back(frame,home_view, win_prop)
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.8)
    
def teller_login(win_prop,preframe):
    '''Teller frame is made up of:
      - H1 (teller login)
      - ID entry/input
      - Password entry/input
    '''
    ## FRAME SETUP
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 30

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Teller Login"
    Label(frame,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*11),y=WIN_HEIGHT*0.1)
    
    passwordvalue, teller_id = '', 'T-'
    PASS_LABEL, ID_LABLE = 'Enter Password', 'Enter Teller ID'
    ## ID field
    Label(frame, text=ID_LABLE, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(ID_LABLE)*8),y=WIN_HEIGHT*0.3)   
    teller_id = Entry(frame, textvariable=teller_id, 
          font= f'{DEFAULT_FONT} 10', 
          fg='#666', 
          width=BTN_WIDTH, 
          bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.4)
    ## password field
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.5)    
    Entry(frame, textvariable=passwordvalue, show='*',
          font= f'{DEFAULT_FONT} 10', 
          fg='#666', 
          width=BTN_WIDTH, 
          bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.6)
      
    ## submit button
    Button(frame, text="Login",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, width=BTN_WIDTH, 
           height=1,
           command='').place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.7)
    ## back button
    Button(frame, text="<<👈 Go Back",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37', 
           fg=THEME_DARK, 
           width=15, 
           height=1,
           command=lambda:go_back(frame,home_view, win_prop)
           ).place(x=place_center(WIN_WIDTH, 15*8), y=WIN_HEIGHT*0.8)
    
def customer_page(win_prop,preframe):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH, BTN_HEIGHT = 15, 3
    GAP = int((640-BTN_WIDTH*8*3)/(3+1))
    My = place_center(WIN_HEIGHT, 3)

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    HEADING = "How May We Help You?"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK
          ).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.2)
    
    # INPUT BUTTONS
    ## Deposit Button
    Button(frame, text="Deposit", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#975318', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Deposit')
           ).place(x=GAP, y=My)
    ## Withdraw button
    Button(frame, text="Withdraw", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#2468ac', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Withdraw')
           ).place(x=GAP*2+BTN_WIDTH*8, y=My)
    ## Transfer button
    Button(frame, text="Transfer",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#70f', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Transfer')
           ).place(x=GAP*3+BTN_WIDTH*8*2, y=My)
    ## back button
    Button(frame, text="<<👈 Go Back",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=15, 
          height=1,
          command=lambda:go_back(frame,home_view, win_prop)
          ).place(x=place_center(WIN_WIDTH, 15*8), y=WIN_HEIGHT*0.8)

# ==================3rd View============== #
def ticket_page(win_prop,preframe,service=''):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 15
    GAP = int((640-BTN_WIDTH*8*2)/(2+1))

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1
    HEADING = "Print Ticket"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.1)

    Label(frame,text=service+'  Ticket',
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.25)

    label_content = [
      'Name: ...............................',
      'Ticket ID: ..........................',
      'Service: .............................',
      'Date: ................................',
    ]
    for l in range(len(label_content)):
      Label(frame,text=label_content[l],
          font=f'{DEFAULT_FONT} 10', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*(0.4+l/10))
    
    Button(frame, text="<<👈 Go Back",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=lambda:go_back(frame,customer_page, win_prop, frame)
          ).place(x=GAP, y=WIN_HEIGHT*0.8)

    Button(frame, text="🖨️ Print Ticket",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg="#90e210", 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=''
          ).place(x=GAP*2+BTN_WIDTH*8, y=WIN_HEIGHT*0.8)
