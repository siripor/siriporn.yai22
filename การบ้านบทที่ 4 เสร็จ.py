from tkinter import *
from tkinter import ttk,messagebox


import csv
from datetime import datetime


GUI = Tk()
GUI.title('บันทึกค่าใช้จ่าย by Gift')
GUI.geometry('700x700+500+50')

Tab = ttk.Notebook(GUI)
T1=Frame(Tab)
T2=Frame(Tab) 
Tab.pack(fill=BOTH, expand=1)

icon_t1= PhotoImage(file='t1_expen.png')
icon_t2 = PhotoImage(file='t2_expen.png')

 
Tab.add(T1, text=f'{"ค่าใช้จ่าย": ^{30}}', image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด": ^{30}}', image=icon_t2,compound='top')
#Tab.add(T2, text='Expense List', image=listicon,compound='top')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

F1 = Frame(T1)
F1.place(x=100,y=50)
         
days = {'Mon':'จันทร์',
         'Thu':'พฤ',
         'Fri':'ศุกร์',
         'Sat':'เสาร์',
         'Sun':'อาทิตย์', }

def save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    amout = v_amout.get()
    if expense =='' or price ==''or amout=='':
        print('NO Data')
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูลค่าใช้จาย')
        return
    elif price == '':
        messagebox.showwarning('ERORR','กรุณากรอกราคา')
        return
    elif amout =='':
        amout = 1
    
    total = float(price)*float(amout)     
    try:
        total = float(price)*float(amout)
        
        print('รายการ: {} ราคา: {}'.format(expense,price,))
        print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(amout,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text +'จำนวน: {} รวมทั้งหมด: {}บาท'.format(amout,price)
        v_resul.set(text)
        
        v_expense.set('')
        v_price.set('')
        v_amout.set('')

        today = datetime.now().strftime('%a')
        print(today)
        dt = datetime.now().strftime('%y-%m-%d-%H:%M:%S')
        dt = days[today]+'-'     
        with open ('savedata.csv','a',encoding='utf-8',newline='') as f:
            fw = csv.writer(f)#สร้างฟังชั่นสำหรับเขียนข้อมูล
            data =[expense,price]
            fw.writerow(data)
        E1.focus

    except :
        print('ERROR')
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_amout.set('')
        #messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')



GUI.bind('<Return>',save)
FONT1 = (None,20)

main_icon = PhotoImage(file='icon_money.png')
Mainicon = Label(F1,image=main_icon)
Mainicon.pack()


#--------------text1--------------
L = ttk.Label(F1,text='ชื่อรายการ',font=FONT1).pack()
v_expense = StringVar()
#StringVar()คือ ตัวแปรพิเศษสำหรับเก็ข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#---------------------------------

#--------------text2--------------
L = ttk.Label(F1,text='ราคา  บาท',font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#---------------------------------


#--------------text3--------------
L = ttk.Label(F1,text='จำนวน  ชิ้น',font=FONT1).pack()
v_amout = StringVar()
E3 = ttk.Entry(F1,textvariable=v_amout,font=FONT1)
E3.pack()
#---------------------------------

icon_b1 = PhotoImage(file='b_save.png')


B2=ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=save)
B2.pack(ipadx=50,ipady=20)

v_resul = StringVar()
v_resul.set('--------ผลลัพธ์----------')
result = ttk.Label(F1,textvariable=v_resul,font=FONT1,foreground='green')
result.pack(pady=20)

GUI.bind('<Tab>',lambda x:E2.focus())
GUI.mainloop()


                    

    
    
