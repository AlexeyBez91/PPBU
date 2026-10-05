from getpass import win_getpass
from tkinter import *
from tkinter import messagebox as mb


def sum():
   s1 = e1.get()
   if not s1.lstrip('-').isdigit():
       mb.showerror(title='Ошибка', message='В первое поле должно быть введено целое число!')
       return
   s2 = e2.get()
   if not s2.lstrip('-').isdigit():
       mb.showerror(title='Ошибка', message='Во второе поле должно быть введено целое число!')
       return
   s3 = e3.get()
   if not s3.lstrip('-').isdigit():
       mb.showerror(title='Ошибка', message='Во второе поле должно быть введено целое число!')
       return
   slag_1 = int(s1)
   slag_2 = int(s2)
   slag_3 = int(s3)
   summa = slag_1 + slag_2 + slag_3
   m1['text'] = f'{s1} + {s2} + {s3} = {summa}'

   answer = mb.askyesno(title='Вопрос', message='Продолжаем?')
   if answer:
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       m1['text'] = ''
   else:
       window.destroy()

def multiply():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror(title='Ошибка', message='В первое поле должно быть введено целое число!')
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror(title='Ошибка', message='Во второе поле должно быть введено целое число!')
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror(title='Ошибка', message='В третье поле должно быть введено целое число!')
        return
    mult_1 = int(s1)
    mult_2 = int(s2)
    mult_3 = int(s3)
    mult = mult_1 * mult_2 * mult_3
    m1['text'] = f'{s1} * {s2} * {s3} = {mult}'

    answer = mb.askyesno(title='Вопрос', message='Продолжаем?')
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ''
    else:
        window.destroy()

window = Tk()
window.title('Калькулятор')
window.geometry('350x250')
window.configure(background='black')

m = Label(text='Введите три числа и нажмите\n на кнопку для вычисления', height=2, width=50, bg='black', fg='green', font='Arial 12')
m.pack()

e1 = Entry()
e1.pack(pady=5)
e2 = Entry()
e2.pack(pady=5)
e3 = Entry()
e3.pack(pady=5)

b = Button(text='Сложить три числа', command=sum, fg='brown', bg='black', font='Arial 10 bold')
b.pack(pady=5)
b1 = Button(text='Умножить три числа', command=multiply, fg='brown', bg='black', font='Arial 10 bold')
b1.pack()

m1 = Label(height=2, bg='black', fg='lime', font='Arial 15 bold')
m1.pack()
m1.pack()

window.mainloop()