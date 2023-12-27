from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current= result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def calculate_percentage():
    global first_number
    percentage = int(result_label['text'])
    result = first_number * (percentage / 100)
    result_label.config(text=str(result))

def get_operator(op):
    global  first_number,operator

    first_number=int(result_label['text'])
    operator=op

    if operator == '%':
        calculate_percentage()
    else:
        result_label.config(text='')

    result_label.config(text='')


def get_result():
    global first_number,second_number,operator

    second_number=int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == 'X':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number ==0:
            result_label.config(text='Error')

        else:
            result_label.config(text=str(round(first_number / second_number,2)))




root=Tk()

# create title of gui
root.title('Calculator')

#Adjust size
root.geometry('280x400')

# fixed the width and height
root.resizable(0,0)

#add background color
root.configure(background='black')



# build result area
result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(30,10),sticky='e')
result_label.config(font=('verdana',25,'bold'))


# Build buttons
btnac=Button(root,text='AC',bg='purple',fg='white',width=5,height=2,command=lambda :clear())
btnac.grid(row=1,column=0)
btnac.config(font=('verdana',14))

btnbrac=Button(root,text='( )',bg='orange',fg='white',width=5,height=2)
btnbrac.grid(row=1,column=1)
btnbrac.config(font=('verdana',14))

btnperc=Button(root,text='%',bg='orange',fg='white',width=5,height=2,command=lambda :get_operator('%'))
btnperc.grid(row=1,column=2)
btnperc.config(font=('verdana',14))

btndiv=Button(root,text='/',bg='orange',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btndiv.grid(row=1,column=3)
btndiv.config(font=('verdana',14))


btn7=Button(root,text='7',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=2,column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=2,column=2)
btn9.config(font=('verdana',14))

btnmul=Button(root,text='X',bg='orange',fg='white',width=5,height=2,command=lambda :get_operator('X'))
btnmul.grid(row=2,column=3)
btnmul.config(font=('verdana',14))


btn4=Button(root,text='4',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=3,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=3,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=3,column=2)
btn6.config(font=('verdana',14))

btnmin=Button(root,text='-',bg='orange',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btnmin.grid(row=3,column=3)
btnmin.config(font=('verdana',14))


btn1=Button(root,text='1',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=4,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=4,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='grey',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=4,column=2)
btn3.config(font=('verdana',14))

btnadd=Button(root,text='+',bg='orange',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btnadd.grid(row=4,column=3)
btnadd.config(font=('verdana',14))


#btn0=Button(root,text='0',bg='grey',fg='white',width=5,height=2)
#btn0.grid(row=5,column=0)
#btn0.config(font=('verdana',14))
btn0 = Button(root, text='0', bg='grey', fg='white', width=11, height=2,command=lambda :get_digit(0))  # Width is set to 11 to span 2 columns
btn0.grid(row=5, column=0, columnspan=2)  # Use columnspan to span two columns
btn0.config(font=('verdana', 14))

btndot=Button(root,text='.',bg='grey',fg='white',width=5,height=2)
btndot.grid(row=5,column=2)
btndot.config(font=('verdana',14))

btnequal=Button(root,text='=',bg='purple',fg='white',width=5,height=2,command=get_result)
btnequal.grid(row=5,column=3)
btnequal.config(font=('verdana',14))

root.mainloop()