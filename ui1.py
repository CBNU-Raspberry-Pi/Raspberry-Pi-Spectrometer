from tkinter import *
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import os
import cv2
import ini

def FileOpen(): 
    file = open("data.txt", 'r', encoding="utf-8")
    data =file.read()
    datalist = data.split(",")
    print(datalist)

def save():
    s=asksaveasfile(mode='w', defaultextension="*.txt")
    if s is None:
        return
    ta=Text()
    textsave=str(ta.get(1.0, END))
    s.write(textsave)
    s.close()

def add():
    file = askopenfilename(title = "파일 열기", filetypes = (("py파일", "*.py"),("모든 파일", "*.*")))
    add.title(os.path.basename(file) + " - 메모장")
    add.delete(1.0, END)
    f = open(file,"r")
    add.insert(1.0,f.read())
    f.close()

def graph():
    ini.making()
    photo=PhotoImage(file='graph.png')
    list_file=Label(root,image=photo , width=630, height=450)
    list_file.grid(row=1, column=0)

root=Tk()
root.title("spectrometer")
root.geometry("640x690")

menu=Menu(root)

menu_file=Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open)
menu_file.add_command(label="저장", command=save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

file_frame=Frame(root)
file_frame.grid(row=0, column=0, ipadx=260, padx=5, pady=3)


#저장하기 버튼
btn_save_file=Button(file_frame, command=save, padx=5, pady=3, width=12, text="저장")
btn_save_file.pack(side="right")


#그래프 띄우기
if os.path.isfile("graph.png"):
    photo=PhotoImage(file='graph.png')
    list_file=Label(root,image=photo , width=630, height=450)
    list_file.grid(row=1, column=0)
else: 
    list_file=Label(root, text = "그래프가 없습니다.", bg="white", width=90, height=30)
    list_file.grid(row=1, column=0)
    
#저장 경로
path_frame=LabelFrame(root, text="불러오기")
path_frame.grid(row=2, column=0, padx=5, pady=3, ipady=3, ipadx=35)

add_list=["1번","2번","3번"]
cmb_add=ttk.Combobox(path_frame, state="readonly", values=add_list , width=60)
cmb_add.current(0)
cmb_add.grid(row=0, column=0, padx= 5)

btn_add_path=Button(path_frame, command=add ,text="찾아보기", width=12)
btn_add_path.grid(row=0, column=1)


#분석 프레임
frame_option=LabelFrame(root, text="분석")
frame_option.grid(row=3, column=0, pady=3, ipady=3, ipadx=50)

#계산1
lbl_width=Label(frame_option, text="파장:", width=8)
lbl_width.grid(row=0, column=0, padx=1, pady=3)

opt_width=["원본유지"]
cmb_width=ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.grid(row=0, column=1, padx=8, pady=3)


#계산2
lbl_space=Label(frame_option, text="최고값:", width=8)
lbl_space.grid(row=0, column=2, padx=1, pady=3)


opt_space=["원본유지"]
cmb_space=ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.grid(row=0, column=3, padx=8, pady=3)

#계산3
lbl_format=Label(frame_option, text="계산3:", width=8)
lbl_format.grid(row=0, column=4, padx=1, pady=3)

opt_format=["원본유지"]
cmb_format=ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.grid(row=0, column=5, padx=8, pady=3)

#실행 프레임
frame_run=Frame(root)
frame_run.grid(row=4, column=0, ipadx=215, pady=3)

btn_close=Button(frame_run, pady=3, text="닫기", width=12, command=quit)
btn_close.pack(side="right")

btn_start=Button(frame_run, pady=3, text="시작", width=12, command=graph)
btn_start.pack(side="right")

root.resizable(False, False)
root.mainloop()

