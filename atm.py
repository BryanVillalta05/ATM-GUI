import tkinter
import time

#generalities
window= tkinter.Tk()
window.title('ATM')
window.geometry("300x400")
window.resizable(0, 0)
window.config(bg="#ADA7A7")

#Function of the first page
def page1():
    #Destroy the others frame and buttons
    frm.destroy()
    start_button.destroy()
    
    global credentials, name_frm, name_entry, password_frm, password_entry, advice_frm, next_btn

    #Input of the needed data
    credentials= tkinter.Label(window, text="Enter your credentials, please", font="Arial 14 bold", 
    bg="#ADA7A7")
    credentials.place(x= 10, y= 30)

    #name
    name_frm=tkinter.Label(window, text="Name:", font="Arial", bg="#ADA7A7")
    name_frm.place(x=10, y=70)
    name_entry= tkinter.Entry(window, width=20, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
    name_entry.place(x=65, y=70)

    #password
    password_frm=tkinter.Label(window, text="Password:", font="Arial", bg="#ADA7A7")
    password_frm.place(x=10, y=100)
    password_entry= tkinter.Entry(window, width=20, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", show="*", bg="#ADA7A7")
    password_entry.place(x=90, y=100)

    #important message
    advice_frm=tkinter.Label(window, text="Note: Fill all the field is imortant to go to\nthe next page",
    font="Arial", justify= tkinter.LEFT, highlightthickness=4, 
    highlightbackground="#FC2323", bg="#ADA7A7")
    advice_frm.place(x=8, y=150)

    next_btn= tkinter.Button(window, text="next page", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= page2, bg="#ADA7A7")
    next_btn.place(x=200, y=220)

#Second page, the options' page
def page2():
#destroy the previous things and have things bc the program need that data to continue other process
    credentials.destroy()
    name_frm.destroy()
    name_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
    password_frm.destroy()
    password_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
    advice_frm.destroy()
    next_btn.destroy()

    global warning, back_button, welcome, qu, btn1, btn2, btn3, btn4

    #checking if all the fields are completed
    if name_entry.get() == "" or password_entry.get() == "":
        warning= tkinter.Label(window, text="You need to fill the fields to\ncontinue with the next page",
        font="Arial 14 bold", justify=tkinter.LEFT, bg="#ADA7A7")
        warning.place(x= 10, y= 30)

        back_button= tkinter.Button(window,text = "Back", font="Arial 20 bold", 
        relief= tkinter.SOLID, border=3, command=lambda:[page1(), back_page1()], 
        activebackground='#345', bg="#ADA7A7")
        back_button.place(x=10, y=100)

        #A little trick
        print("User: ", name_entry.get(), " Password: ", password_entry.get())


    #Draw the options' buttons
    if name_entry.get() != "" and password_entry.get() != "":
        welcome= tkinter.Label(window, text="Hello " + name_entry.get(), 
        font="Arial 15 bold", bg="#ADA7A7")
        welcome.place(x= 10, y= 30)

        qu= tkinter.Label(window, text="What you want to do?",
        font="Arial 12",bg="#ADA7A7")
        qu.place(x= 10, y= 65)

        btn1=tkinter.Button(window, text="check balance", relief= tkinter.SOLID,border=3, 
        font="Arial 12 bold", activebackground='#345', bg="#ADA7A7", command=balance)
        btn1.place(x=30, y=100)

        btn2=tkinter.Button(window, text="make a transfer", relief= tkinter.SOLID,border=3,
        font="Arial 12 bold", activebackground='#345',bg="#ADA7A7", command=transfer)
        btn2.place(x=30, y=140)

        btn3=tkinter.Button(window, text="make a deposit", relief= tkinter.SOLID, border=3, 
        font="Arial 12 bold", activebackground='#345', bg="#ADA7A7", command=deposit)
        btn3.place(x=30, y=180)

        btn4=tkinter.Button(window, text="make a withdrawal", relief= tkinter.SOLID, border=3, 
        font="Arial 12 bold", activebackground='#345', bg="#ADA7A7", command=withdrawal)
        btn4.place(x=30, y=220)

        #A little trick
        print("User: ", name_entry.get(), " Password: ", password_entry.get())

        
#page of the first option
def balance():
    #clearing the previous page
    welcome.destroy()
    qu.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    global balance_output , back

    #Drawing the balance output, more future features in the end of the code
    money=100.00

    balance_output = tkinter.Label(window,text=f'Your current balance is\n{money}$',
    font= "Arial 18 bold", bg="#ADA7A7") 
    balance_output.place(x=10, y=30)

    back= tkinter.Button(window,text = "Back", font="Arial 15 bold", 
    relief= tkinter.SOLID, border=3, command=lambda:[page2(), back_page2()], 
    activebackground='#345', bg="#ADA7A7")
    back.place(x=10, y=100)
    

#page for the second option
def transfer():
    #clearing the previous page
    welcome.destroy()
    qu.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    global sent_to, person_name, person_entry, amount, amount_entry, done_btn, get_back

    #Drawing the widgets of th second option
    sent_to= tkinter.Label(window, text="Enter the name of the\nperson who will recieve\nthe money",
    bg="#ADA7A7", font="Arial 18 bold")
    sent_to.place(x=10, y=30)

    person_name=tkinter.Label(window, text="Name", bg="#ADA7A7", font="Arial")
    person_name.place(x=90, y=120)

    person_entry=tkinter.Entry(window, width=18, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
    person_entry.place(x=90, y=150)

    amount= tkinter.Label(window, text="Amount", bg="#ADA7A7", font="Arial")
    amount.place(x=90, y=180)

    amount_entry=tkinter.Entry(window, width=18, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
    amount_entry.place(x=90, y=210)

    #Function for the done page after the transfer or the warning page
    def done_page():
        #clearing for the messages
        sent_to.destroy()
        person_name.destroy()
        person_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
        amount.destroy()
        amount_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
        done_btn.destroy()
        get_back.destroy()
        
        global done_frm, back_transfer, warning_transfer, back_transfer

        #if nothing was enter
        if person_entry.get() == "" or amount_entry.get()=="":
            warning_transfer= tkinter.Label(window, text="No name has been entered",
            font="Arial 14 bold", justify=tkinter.LEFT, bg="#ADA7A7")
            warning_transfer.place(x= 10, y= 30)

            back_transfer= tkinter.Button(window,text = "Back", font="Arial", 
            relief= tkinter.SOLID, border=3, command=lambda:[transfer(), back_page2()], 
            activebackground='#345', bg="#ADA7A7")
            back_transfer.place(x=10, y=100)

        #succes message
        if person_entry.get() != "" and amount_entry != "":
            done_frm=tkinter.Label(text=amount_entry.get() + " was sent to " + person_entry.get(),
            bg="#ADA7A7", font="Arial 18 bold")
            done_frm.place(x=10, y=30)

            back_transfer= tkinter.Button(window,text = "Back", font="Arial", 
            relief= tkinter.SOLID, border=3, command=lambda:[transfer(), back_page2()], 
            activebackground='#345', bg="#ADA7A7")
            back_transfer.place(x=10, y=100)

    #the button is after the function otherwise it will raise an error 
    done_btn= tkinter.Button(window, text="next page", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= done_page, bg="#ADA7A7")
    done_btn.place(x=200, y=250)

    get_back=tkinter.Button(window, text="Back", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= lambda:[page2(), back_totransfer()], bg="#ADA7A7")
    get_back.place(x=10, y=250)

#the third option of the second page
def deposit():
    #clearing the previous page
    welcome.destroy()
    qu.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

    #start the new page
    global inst, inst_desc, varR, checkR_btn, varC, checkC_btn, dp2, back_page_2

    inst= tkinter.Label(window, text="Instructions", bg="#ADA7A7", font="Arial 35 bold")
    inst.place(x=10, y=30)

    inst_desc= tkinter.Label(window, text="Mark if the money came from a\nremittance or if you will send money from\nyour cebit card.",
    bg="#ADA7A7", font="Arial 12", justify=tkinter.LEFT)
    inst_desc.place(x=10, y=100)

    varR = tkinter.StringVar()
    checkR_btn=tkinter.Checkbutton(window, text="Remittance", bg="#ADA7A7", font="Arial 12 bold", 
    onvalue="R", offvalue="nR", activebackground='#345', border=3, variable=varR)
    checkR_btn.deselect()
    checkR_btn.place(x=40, y=180)

    varC=tkinter.StringVar()
    checkC_btn=tkinter.Checkbutton(window, text="Credit card", bg="#ADA7A7", font="Arial 12 bold", 
    onvalue="C", offvalue="nC", activebackground='#345', border=3, variable=varC)
    checkC_btn.deselect()
    checkC_btn.place(x=40, y=210)

    dp2= tkinter.Button(window, text="next page", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= lambda:[deposit_p2(), clr_dp1()], bg="#ADA7A7")
    dp2.place(x=200, y=250)

    back_page_2=tkinter.Button(window,text = "Back", font="Arial 12 bold", 
        relief= tkinter.SOLID, border=3, command=lambda:[clr_dp1(), page2()], 
        activebackground='#345', bg="#ADA7A7")
    back_page_2.place(x=10, y=250)

#This two functions to clar are here because if they weren´t here this will be a mess
def clr_dp1():
    try:
        inst.destroy()
        inst_desc.destroy()
        checkR_btn.place(anchor="nw", x=0, y=0, width=0, height=0)
        checkC_btn.place(anchor="nw", x=0, y=0, width=0, height=0)
        dp2.destroy()
        back_page_2.destroy()
    except NameError:
        pass

def deposit_p2():
    #Clearing the previous page
    inst.destroy()
    inst_desc.destroy()
    checkR_btn.place(anchor="nw", x=0, y=0, width=0, height=0)
    checkC_btn.place(anchor="nw", x=0, y=0, width=0, height=0)
    dp2.destroy()

    """
    The succesful page of the deposit is here before the page that is for entering the Remittance code 
    Because tho assing this fuction to the "Next page" button it need to be created before
    """

    def deposit_donep():

        advice_frm.destroy()
        to_donep.destroy()
        back_todeposit.destroy()
        r_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
        r_frm.destroy()
        r_inst.destroy()
        
        global back_deposit2, happy_f, dep_don

        dep_don= tkinter.Label(text="Please wait", justify=tkinter.CENTER,
        font="Arial 27 bold", bg="#ADA7A7")

        time.sleep(1)

        dep_don.config(text="The deposit was\nsuccessful")

        print("Codigo: " + r_entry.get())


        dep_don.place(x=10, y=20)
        happy_f=tkinter.Label(text="☺", justify=tkinter.CENTER, font="Arial 100 bold", bg="#ADA7A7")
        happy_f.place(x=80, y=100)

        back_deposit2= tkinter.Button(window,text = "Back", font="Arial 12 bold", 
        relief= tkinter.SOLID, border=3, command=lambda:[deposit_p2(), deposit_clear()], 
        activebackground='#345', bg="#ADA7A7")
        back_deposit2.place(x=10, y=230)

    global warning_d, back_deposit, r_frm, r_inst, r_entry, advice_frm, to_donep, back_todeposit

    #If staments to control the decisitions
    if varR.get() == checkR_btn["onvalue"] and varC.get() == checkC_btn["onvalue"]:
        warning_d= tkinter.Label(window, text="You can't have both options",
        font="Arial 14 bold", bg="#ADA7A7")
        warning_d.place(x= 10, y= 30)

        back_deposit= tkinter.Button(window,text = "Back", font="Arial 12 bold", 
        relief= tkinter.SOLID, border=3, command=lambda:[deposit(), back_page2()], 
        activebackground='#345', bg="#ADA7A7")
        back_deposit.place(x=10, y=100)

    elif varR.get() == checkR_btn["offvalue"] and varC.get() == checkC_btn["offvalue"]:
        warning_d= tkinter.Label(window, text="You need at least one option\nselected",
        font="Arial 14 bold", bg="#ADA7A7", justify=tkinter.LEFT)
        warning_d.place(x= 10, y= 30)

        back_deposit= tkinter.Button(window,text = "Back", font="Arial 12 bold", 
        relief= tkinter.SOLID, border=3, command=lambda:[deposit(), back_page2()], 
        activebackground='#345', bg="#ADA7A7")
        back_deposit.place(x=10, y=100)

    #Remitance  
    elif varR.get() == checkR_btn["onvalue"]:
        r_frm=tkinter.Label(window, text="You choose remmitance", font= "Arial 18 bold", bg="#ADA7A7")
        r_frm.place(x=10, y=20)

        r_inst=tkinter.Label(window, text="Enter the code", font="Arial 12", bg="#ADA7A7")
        r_inst.place(x=10, y=60)

        r_entry=tkinter.Entry(window, width=18, highlightthickness=2,
        highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
        r_entry.place(x=90, y=90)

        advice_frm=tkinter.Label(window, text="Remember to enter the correct amount\nof numbers in the remmitance code",
        font="Arial", justify= tkinter.LEFT, highlightthickness=4, 
        highlightbackground="#FC2323", bg="#ADA7A7")
        advice_frm.place(x=8, y=130)

        back_todeposit= tkinter.Button(window,text = "Back", font="Arial", 
        relief= tkinter.SOLID, border=3, command=lambda:[clear_deposit(), deposit()], 
        activebackground='#345', bg="#ADA7A7")
        back_todeposit.place(x=10, y=190)

        to_donep= tkinter.Button(window, text="Done", font="Arial",relief= tkinter.SOLID, 
        activebackground='#345', border=3, command= deposit_donep, bg="#ADA7A7")
        to_donep.place(x=227, y=190)

        #Credit card
    elif varC.get() == checkC_btn["onvalue"]:
        r_frm=tkinter.Label(window, text="You choose Credit Card", font= "Arial 18 bold", bg="#ADA7A7")
        r_frm.place(x=10, y=20)

        r_inst=tkinter.Label(window, text="Enter the Numbers of your credit card", font="Arial 12", bg="#ADA7A7")
        r_inst.place(x=10, y=60)

        r_entry=tkinter.Entry(window, width=18, highlightthickness=2,
        highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
        r_entry.place(x=90, y=90)

        advice_frm=tkinter.Label(window, text="You just need to enter the numbers that \nare behind of your credit card",
        font="Arial", justify= tkinter.LEFT, highlightthickness=4, 
        highlightbackground="#FC2323", bg="#ADA7A7")
        advice_frm.place(x=8, y=130)

        back_todeposit= tkinter.Button(window,text = "Back", font="Arial", 
        relief= tkinter.SOLID, border=3, command=lambda:[clear_deposit(), deposit()], 
        activebackground='#345', bg="#ADA7A7")
        back_todeposit.place(x=10, y=190)

        to_donep= tkinter.Button(window, text="Done", font="Arial",relief= tkinter.SOLID, 
        activebackground='#345', border=3, command= deposit_donep, bg="#ADA7A7")
        to_donep.place(x=227, y=190)

#The clear function for the withdrawal is here because it raise an error if it placed after the withdrawal function
def withdrawal_clear():
    msg.destroy()
    pin.destroy()
    pin_space.place(anchor="nw", x=0, y=0, width=0, height=0)
    amount.destroy()
    amount_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
    done_btn.destroy()
    get_back.destroy()
    twenty.destroy()
    fifty.destroy()
    hundred.destroy()
    dollars.destroy()

#The withdrawal window
def withdrawal():
    #clearing the previous page
    welcome.destroy()
    qu.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    
    #Starting the page

    global msg, pin, dollars, twenty, fifty, hundred, pin_space, amount, amount_entry, done_btn, get_back

    msg= tkinter.Label(window, text="Enter your card PIN",
    bg="#ADA7A7", font="Arial 18 bold")
    msg.place(x=10, y=30)

    pin=tkinter.Label(window, text="Enter your pin below", bg="#ADA7A7", font="Arial")
    pin.place(x=90, y=70)

    pin_space=tkinter.Entry(window, width=18, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
    pin_space.place(x=90, y=100)

    amount= tkinter.Label(window, text="Amount", bg="#ADA7A7", font="Arial")
    amount.place(x=90, y=140)

    amount_entry=tkinter.Entry(window, width=18, highlightthickness=2,
    highlightcolor= "black", highlightbackground = "black", bg="#ADA7A7")
    amount_entry.place(x=90, y=170)

    #Function for the done page after the transfer or the warning page
    def done_page():
        #clearing for the messages
        msg.destroy()
        pin.destroy()
        pin_space.place(anchor="nw", x=0, y=0, width=0, height=0)
        amount.destroy()
        amount_entry.place(anchor="nw", x=0, y=0, width=0, height=0)
        done_btn.destroy()
        get_back.destroy()
        twenty.destroy()
        fifty.destroy()
        hundred.destroy()
        dollars.destroy()
        
        global done_frm, back_transfer, warning_transfer

        #if nothing was enter
        if pin_space.get() == "" or amount_entry.get()=="":
            warning_transfer= tkinter.Label(window, text="No pin has been entered",
            font="Arial 14 bold", justify=tkinter.LEFT, bg="#ADA7A7")
            warning_transfer.place(x= 10, y= 30)

            back_transfer= tkinter.Button(window,text = "Back", font="Arial", 
            relief= tkinter.SOLID, border=3, command=lambda:[withdrawal_clear_dep(),withdrawal()], 
            activebackground='#345', bg="#ADA7A7")
            back_transfer.place(x=10, y=100)

        #succes message
        elif pin_space.get() != "" and amount_entry != "":
            done_frm=tkinter.Label(text=amount_entry.get() + " was retired ",
            bg="#ADA7A7", font="Arial 18 bold")
            done_frm.place(x=10, y=30)

            back_transfer= tkinter.Button(window,text = "Back", font="Arial", 
            relief= tkinter.SOLID, border=3, command=lambda:[withdrawal_clear_dep(),withdrawal()], 
            activebackground='#345', bg="#ADA7A7")
            back_transfer.place(x=10, y=100)
    
    #Ask the type
    dollars= tkinter.Label(window, text="Which type of dollars you want?", bg="#ADA7A7", font="Arial")
    dollars.place(x=20, y=200)

    #Type of dollars
    varT=tkinter.StringVar()
    twenty=tkinter.Checkbutton(window, text="Twenty", bg="#ADA7A7", font="Arial 12 bold", 
    onvalue="T", offvalue="nT", activebackground='#345', border=3, variable=varT)
    twenty.deselect()
    twenty.place(x=10, y=230)

    varF=tkinter.StringVar()
    fifty=tkinter.Checkbutton(window, text="Fifty", bg="#ADA7A7", font="Arial 12 bold", 
    onvalue="F", offvalue="nF", activebackground='#345', border=3, variable=varF)
    fifty.deselect()
    fifty.place(x=110, y=230)

    varH=tkinter.StringVar()
    hundred=tkinter.Checkbutton(window, text="Hundred", bg="#ADA7A7", font="Arial 12 bold", 
    onvalue="H", offvalue="nH", activebackground='#345', border=3, variable=varH)
    hundred.deselect()
    hundred.place(x=190, y=230)
    
    #the button is after the function otherwise it will raise an error 
    done_btn= tkinter.Button(window, text="next page", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= done_page, bg="#ADA7A7")
    done_btn.place(x=200, y=280)

    get_back=tkinter.Button(window, text="Back", font="Arial",relief= tkinter.SOLID, 
    activebackground='#345', border=3, command= lambda:[ withdrawal_clear(), page2()], bg="#ADA7A7")
    get_back.place(x=10, y=280)
    
"""
The next section is for the functions that have the duty of try to clear the previos pages for the buttons
that make you return to the page

the names of the functions are not acurrated for the page that they are but I was running out of names
"""
def withdrawal_clear_dep():
    back_transfer.destroy()
    try:
        done_frm.destroy()
    except NameError:
        pass   
    try:
        warning_transfer.destroy()
    except NameError:
        pass


def deposit_clear():
    try:
        happy_f.destroy()
        back_deposit2.destroy()
        dep_don.destroy()
    except NameError:
        pass

def back_page2():
    #a try statement to clear the first option and half of the secondd option
    try:
        balance_output.destroy()
        back.destroy()
    except NameError:
        pass
    try:
        done_frm.destroy()
        back_transfer.destroy()
    except NameError:
        pass
    try:
        warning_transfer.destroy()
        back_transfer.destroy()
    except NameError:
        pass
    try:
        warning_d.destroy()
        back_deposit.destroy()

    except NameError:
        pass    

def back_totransfer():
    sent_to.destroy()
    person_name.destroy()
    person_entry.destroy()
    amount.destroy()
    amount_entry.destroy()
    done_btn.destroy()
    get_back.destroy()


def back_page1():
    warning.destroy()
    back_button.destroy()
    
#Yes another function to clear a page
def clear_deposit():
    r_frm.destroy()
    r_inst.destroy()
    r_entry.destroy()
    advice_frm.destroy()
    to_donep.destroy()
    back_todeposit.destroy()

#I don't know for what this function was
def dp2c():
    pass
#welcome frame
frm = tkinter.Label(window, text="Welcome!", font="Arial 44 bold",bg="#ADA7A7") 
frm.place(x= 10, y= 20)

#button to go to the next page
start_button = tkinter.Button(window,text = "Next", font="Arial 30 bold", 
relief= tkinter.SOLID, border=3, command=page1, activebackground='#345', bg="#ADA7A7")
start_button.place(x=90, y=150)

window.mainloop()

"""
name_entry.place(anchor="nw", x=0, y=0, width=0, height=0) is for hide the widget because if we destroy 
it or use "place_forget the text will no concatenate the text Hi with the name so for the UI and UX is 
better that way

Conected to a database the balance can change matchng the name with the data in the data base, and also
doing that the balance will be more responsive
"""
