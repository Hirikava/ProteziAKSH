from tkinter import *

window = Tk()


window.title('Прогнозирование осложнений АКШ')
window.geometry ('450x550')
window.resizable(width=False, height = False)

frame = Frame(window)
frame.place(relwidth=1,relheight=0.33)

patient = Label(frame,text='Пациент', font='Arial 10',fg='green')
secondname = Label(frame,text='*Фамилия:', font='Arial 8')
name = Label(frame,text='*Имя',font='Arial 8')
thirdname =Label(frame,text='*Отчество', font='Arial 8')
birthday =Label(frame,text='*Дата рождения', font='Arial 8')
ngosp =Label(frame,text='№ госпитализации', font='Arial 8')
gospdate =Label(frame,text='Дата госпитализации', font='Arial 8')
patient.place(x=3,y=4)
secondname.place(x=3,y=25)
name.place(x=3,y=65)
thirdname.place(x=3,y=105)


vvod1 = Entry(frame)
vvod1.place(relheight=0.08,relwidth=0.25,x=10,y=45)
vvod2 = Entry(frame)
vvod2.place(relheight=0.08,relwidth=0.25,x=10,y=85)
vvod3 = Entry(frame)
vvod3.place(relheight=0.08,relwidth=0.25,x=10,y=125)
window.mainloop()