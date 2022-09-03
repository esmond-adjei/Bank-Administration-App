# TO-D0 
- [] TellerQueue
    - [x] ~~queue has no pointer to connect to next item in queue~~
- [] json database
    - [] we need a convinient way of parsing data
- [x] ~~operational logic for main.py~~
    - [x] ~~check if customer has account before adding to queue (key is for withdraw, deposit and transfer)~~
    - [x] ~~ordering queue order by ticket id or may be time of arrival~~

## GUI (@ 01-09-2022)
- [] window frame transistions. [youtube](youtube.com/?)
- [] windows for each of...
    - [] admin
    - [] teller
    - [] customer
- [] linking gui with backend logic code

---
change to admin/teller/customer frame
---
# WHAT I HAVE LEARNED ABOUT PROGRAMMING STRUCTURE
- Functions are good for dynamic code generation
    - it provides a template of process for code to be generated
- Classes are good for bundling up a set of code that have commonalities. It's some sort of factorization; taking common structures and grouping them together while leaving exceptions.

- There is always a tradeoff between processing and storage. Processing takes time and storage takes space.
A good combination of the 2 makes the program faster.

---
- [x] ~~input/entry fields not showing~~
    ==solution==: wrong placement of btn_width, called before assignment
- [x] ~~back button~~
    ==solution==: transframe function in gui_operations takes two frames, a previous and current for backward operation.
    - pack the previous frame
    - pack_forget the current frame
    ==!!COROLARY PROBLEM==: frames are still in memory and they overlay next frames we enter.
    ==! SOLVED==: destroy current frame. Re-run view function afterwards.
- [] ticket page is created
    - same page will be used for issuing of receipt
- [] When teller logs in, there will not be any account functions coded. The only activity will have to be click 'serve customer', then a **receipt** will be generated
