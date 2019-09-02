# -*- coding: utf-8 -*-
#python 3.3
from tkinter import *
from tkinter import messagebox
root = Tk()
def about_Box():
    top = Toplevel()
    top.title("About")
    Label(top,text='Write by 5130379051').pack()
    Label(top,text='This calculator is based on eval()').pack()
    top.resizable(False,False)

def convert(in_hex,out_hex,chose_value):
    out_hex.config(state=NORMAL)
    out_hex.delete(1.0, END)
    try :
        oc_value=int(in_hex,chose_value.get())
        out_hex.insert(END,"Binary:"+bin(oc_value))
        out_hex.insert(END,"\nOctal:"+oct(oc_value))
        out_hex.insert(END,"\nDecimal:"+str(oc_value))
        out_hex.insert(END,"\nHex:"+hex(oc_value))
    except:
        out_hex.insert(END,"Can not be converted")
    out_hex.config(state=DISABLED)

def Hex_converter(win_width,win_height,screen_width,screen_height):
    hex_form = Toplevel()
    hex_form.title("Converter")
    inhex_txt=StringVar()
    input_hex =Entry(hex_form,textvariable=inhex_txt)
    input_hex.pack()
    choseframe=Frame(hex_form)
    choseframe.pack()
    origion_hex=IntVar()
    origion_hex.set(10)
    Radiobutton(choseframe,text="Binary",variable=origion_hex,value=2).pack(side="left")
    Radiobutton(choseframe,text="Octal",variable=origion_hex,value=8).pack(side="left")
    Radiobutton(choseframe,text="Decimal",variable=origion_hex,value=10).pack(side="left")
    Radiobutton(choseframe,text="Hex",variable=origion_hex,value=16).pack(side="left")
    root.geometry('%dx%d+%d+%d' % (win_width,win_height,(screen_width - win_width)/2, (screen_height - win_height)/2) )

    output_hex =Text(hex_form,height=10,width=40,state =DISABLED)
    output_hex.pack()
    input_hex.bind("<KeyRelease>",lambda f:convert(inhex_txt.get(),output_hex,origion_hex))
    hex_form.resizable(False,False)

def support_Box():
    sp_box = Toplevel()
    sp_box.title("Support Operators")
    #got from http://woodpecker.org.cn/abyteofpython_cn/chinese/ch05s02.html
    Label(sp_box,text="""+	加		两个对象相加					3 + 5得到8。
-	减		得到负数或是一个数减去另一个数			-5.2得到一个负数。50 - 24得到26。
*	乘		两个数相乘或是返回一个被重复若干次的字符串		2 * 3得到6。'la' * 3得到'lalala'。
**	幂		返回x的y次幂					3 ** 4得到81（即3 * 3 * 3 * 3）
/	除		x除以y						4/3得到1.3333333333333333
//	取整除		返回商的整数部分					4 // 3.0得到1
%	取模		返回除法的余数					8%3得到2。-25.5%2.25得到1.5
<<	左移		把一个数的比特向左移一定数目			2 << 2得到8。
>>	右移		把一个数的比特向右移一定数目			11 >> 1得到5。
&	按位与		数的按位与					5 & 3得到1。
|	按位或		数的按位或					5 | 3得到7。
^	按位异或		数的按位异或					5 ^ 3得到6
~	按位翻转		x的按位翻转是-(x+1)				~5得到6。
所有比较运算符返回1(True)表示真,返回0(False)表示假。比较可以被任意连接:		1<4>=3!=6返回True
<	小于		返回x是否小于y。					3 < 4 返回True
>	大于		返回x是否大于y					5 > 3 返回True
<=	小于等于		返回x是否小于等于y					3 <=6 返回True
>=	大于等于		返回x是否大于等于y					4 >=3 返回True
==	等于		比较对象是否相等					2 ==2 返回True
!=	不等于		比较两个对象是否不相等				2 !=3 返回True
not	布尔“非”	如果x为True，返回False。如果x为False，它返回True。	not (1 == 1)返回False。
and	布尔“与”	如果x为False，x and y返回False，否则它返回y的计算值。	(1==1) and(1 == 2)返回False
or	布尔“或”	如果x是True，它返回True，否则它返回y的计算值。	(1==1) or (1 == 2)返回True """ ,justify = 'left').pack(side="left")
#    Label(sp_box,text="Support Operators:\nOperators\tExamples\n+\t1+1=2\n-\t2-1=1\n*\t2*3=6\n/\t5/2=2.5\n**\t2**3=8\n( )\t(1+1)*2=4\n|\t6 | 3=7\n&\t6 & 3=2\n^\t6 ^ 3=5\nand\t 1 and 123=123\nor\t 0 or 456=456").pack(side="left")
    sp_box.resizable(False,False)

def calculate(do_calc,input_txt,output_string):
    if(not do_calc):
        return
    output_string.config(state=NORMAL)
    output_string.delete(1.0, END)
    output_string.insert(END,input_txt.get())
    try:
        output_string.insert(END,'\n='+str(eval(input_txt.get())))
    except:        
        output_string.insert(END,'\nWrong expression.')
    output_string.config(state=DISABLED)

def add_widgets(win_width,win_height,screen_width,screen_height):
    m = Menu(root)
    root.config(menu=m)
    toolmenu=Menu(m)
    helpmenu=Menu(m)
    m.add_cascade(label="Tool",menu=toolmenu)
    m.add_cascade(label="Help",menu=helpmenu)
    toolmenu.add_command(label="Hex converter",command=lambda :Hex_converter(win_width,win_height,screen_width,screen_height))
    helpmenu.add_command(label="About",command=about_Box)
    helpmenu.add_command(label="Support Operators",command=support_Box)
    
    rtcomp = IntVar()
    rtcomp.set(1)
    output_string =Text(root,state = DISABLED)
    input_txt=StringVar()
    input_string =Entry(root,textvariable=input_txt,width = win_width-50)
    input_string.bind("<KeyRelease>",lambda f:calculate(rtcomp.get(),input_txt,output_string))
    input_string.bind("<Return>",lambda f:calculate(True,input_txt,output_string))
    input_string.pack()
    input_string.focus_set()
    output_string.pack()
    Checkbutton(root,text="Real-time computing",variable=rtcomp).pack()
    

def init_windows():
    win_width=250
    win_height=350
    root.withdraw()                                        #hide window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 100        #under windows, taskbar may lie under the screen
    root.resizable(False,False)
    root.title("My calculator")

    add_widgets(win_width,win_height,screen_width,screen_height)

    root.update_idletasks()
    root.deiconify()                                    #now window size was calculated
    root.withdraw()                                        #hide window again
    root.geometry('%dx%d+%d+%d' % (win_width,win_height,(screen_width - win_width)/2, (screen_height - win_height)/2) )    #center window on desktop
    root.deiconify()

def quit_ask():
    if messagebox.askokcancel("Quit","Do you really wish to quit?"):
        root.destroy()

def main():
    init_windows()
    root.protocol("WM_DELETE_WINDOW",quit_ask)            #when close window
    root.mainloop()

main()
