from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime


GUI = Tk()
GUI.title('บันทึกค่าใช้จ่าย by Gift')
GUI.geometry('700x700+500+50')

########################MENU###################
menubar = Menu(GUI)
GUI.config(menu=menubar)

#file manu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import csv')
filemenu.add_command(label='Export to Googlesheet')

#Help
def About():
    messagebox.showinfo('About','สวัสดี โปรแกรมบันทึกข้อมูลฃ\n สนใจบริจาคเราไหม ขอ 1 BTC ก็พอแล้ว \n')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

#Donate
def Donate():
    messagebox.showinfo('Donate','dogecoin network: DLaoRTEF36VqfUpLrcWKcrNDKH27VsqJ6v\nDogecoin BEP20(BSC):    0x0fd36bbcf3f1010796e748d3c4bd48c7ee61620e')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)



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
#F1.place(x=100,y=50)
F1.pack()
         
days = {'Mon':'จันทร์',
         'Tue':'อังคาร',
         'Wed':'พุธ',
         'Thu':'พฤหัสบดี',
         'Fri':'ศุกร์',
         'Sat':'เสาร์',
         'Sun':'อาทิตย์', }

def save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = quantity.get()

    if expense =='' :
        print('NO Data')
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูลค่าใช้จาย')
        return
    elif price == '':
        messagebox.showwarning('ERORR','กรุณากรอกราคา')
        return
    elif quantity =='':
        quantity = 1
    
    total = float(price)*float(quantity)     
    
    try:
        total = float(price)*float(quantity)
        
        print('รายการ: {} ราคา: {}'.format(expense,price,))
        print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text +'จำนวน: {} รวมทั้งหมด: {}บาท'.format(quantity,total)
        v_resul.set(text)
        #clearข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

        today = datetime.now().strftime('%a')
        print(today)
        dt = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        dt = days[today]+'-'+dt     
        with open ('savedata.csv','a',encoding='utf-8',newline='') as f:
            fw = csv.writer(f)#สร้างฟังชั่นสำหรับเขียนข้อมูล
            data =[dt,expense,price,quantity,total]
            fw.writerow(data)
        
        E1.focus()
        update_table()
        
    except Exception as e:
        print('ERROR:',e)
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
        #messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')


#ทำให้กด enter ได้
GUI.bind('<Return>',save)#ต้องเพิ่มใน def Save(event=None) ด้วย
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
v_quantity = StringVar()
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#---------------------------------

icon_b1 = PhotoImage(file='b_save.png')


B2=ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_resul = StringVar()
v_resul.set('--------ผลลัพธ์----------')
result = ttk.Label(F1,textvariable=v_resul,font=FONT1,foreground='green')
result.pack(pady=20)


#######TAB2###################

def read_csv():
    
    with open('savedata.csv',newline ='',encoding ='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    
    return data
            




#table#
L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['วันเวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable =ttk.Treeview(T2,columns=header,show='headings',height=20)
resulttable.pack()

#for i in range(len(header)):

    #resulttable.heading(header[i],text=header[i])

for h in header:
    resulttable.heading(h,text=h)




#for hd in header:###
    #resulttable.heading(hd,text=hd)#

headerwidth = [150,170,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

#resulttable.insert('',volue=['จันทร์','น้ำดื่ม',30,5,150])
#resulttable.insert('','end'volue=['อังคาร','น้ำดื่ม',30,5,150])

def update_table():
    #for c in resulttable.get_children():
        #resulttable.delete(c)
    resulttable.delete(*resulttable.get_children())
    data = read_csv()
    for d in data:
        resulttable.insert('',0,value=d)

update_table()
print('GET CHILD:',resulttable.get_children())


GUI.bind('<Tab>',lambda x:E2.focus())
GUI.mainloop()


                    

    
    
