from tkinter import ttk
from tkinter import *

window = Tk()

window.title('Прогнозирование осложнений АКШ')
window.geometry ('450x550')
window.resizable(width=False, height = False)

frame = Frame(window)
frame.place(relwidth=1,relheight=1)

patient = Label(frame,text='Пациент', font='Arial 12',fg='green').place(x=3,y=4)
secondname = Label(frame,text='*Фамилия:', font='Arial 9').place(x=3,y=25)
name = Label(frame,text='*Имя',font='Arial 9').place(x=3,y=65)
thirdname =Label(frame,text='*Отчество', font='Arial 9').place(x=3,y=105)
birthday =Label(frame,text='*Дата рождения:', font='Arial 9').place(x=153,y=25)
ngosp =Label(frame,text='№ госпитализации:', font='Arial 9').place(x=156,y=65)
gospdate =Label(frame,text='Дата госпитализации:', font='Arial 9').place(x=158,y=105)
pokazateli =Label(frame,text='Показатели', font='Arial 12',fg='red').place(x=3,y=150)
age =Label(frame,text='Возраст пациента:', font='Arial 9').place(x=3,y=175)
lg =Label(frame,text='Давление в ЛА (мм.рт.ст):', font='Arial 9').place(x=3,y=215)
ca1=Label(frame,text='Cтепень', font='Arial 9').place(x=45,y=255)
ca2=Label(frame,text='поражения КА (%):', font='Arial 9').place(x=15,y=275)
bleed1 =Label(frame,text='Интраоперационная', font='Arial 9').place(x=10,y=315)
bleed2 =Label(frame,text='кровопотеря (мл.):', font='Arial 9').place(x=20,y=335)
Charlson =Label(frame,text='Charlson Index:', font='Arial 9').place(x=170,y=175)
es =Label(frame,text='Euroscore (%):', font='Arial 9').place(x=170,y=215)
Dindo =Label(frame,text='Clavien-Dindo (1-5):', font='Arial 9').place(x=170,y=255)
Result_label=Label(frame,text='Результат', font='Arial 12',fg='blue').place(x=3,y=420)





vvod1 = Entry(frame)
vvod1.place(relheight=0.03,relwidth=0.3,x=10,y=45)
vvod2 = Entry(frame)
vvod2.place(relheight=0.03,relwidth=0.3,x=10,y=85)
vvod3 = Entry(frame)
vvod3.place(relheight=0.03,relwidth=0.3,x=10,y=125)
vvod4 = Entry(frame)
vvod4.place(relheight=0.03,relwidth=0.3,x=160,y=45)
vvod5 = Entry(frame)
vvod5.place(relheight=0.03,relwidth=0.3,x=160,y=85)
vvod6 = Entry(frame)
vvod6.place(relheight=0.03,relwidth=0.3,x=160,y=125)
vvod7 = Entry(frame)
vvod7.place(relheight=0.03,relwidth=0.3,x=4,y=195)
vvod8 = Entry(frame)
vvod8.place(relheight=0.03,relwidth=0.3,x=4,y=235)
vvod9 = Entry(frame)
vvod9.place(relheight=0.03,relwidth=0.3,x=4,y=295)
vvod10 = Entry(frame)
vvod10.place(relheight=0.03,relwidth=0.3,x=4,y=355)
vvod11 = Entry(frame)
vvod11.place(relheight=0.03,relwidth=0.3,x=170,y=195)
vvod12 = Entry(frame)
vvod12.place(relheight=0.03,relwidth=0.3,x=170,y=235)
vvod13 = Entry(frame)
vvod13.place(relheight=0.03,relwidth=0.3,x=170,y=275)



genderlabel = Label(frame,text='Пол пациента:',font='Arial 9')
genderlabel.place (x=323,y=25)

gender = BooleanVar()
gender.set(False)
gender1=Radiobutton(frame, text="Мужской",font='Arial 9',variable=gender,value="True")
gender2=Radiobutton(frame, text="Женский",font='Arial 9', variable=gender, value="False")
gender1.place(x=323,y=45)
gender2.place(x=323,y=65)

separator=ttk.Separator(frame,orient=HORIZONTAL)
separator.place(relwidth=1.0,y=150)
separator2=ttk.Separator(frame,orient=HORIZONTAL)
separator2.place(relwidth=1.0,y=420)

sq = BooleanVar()
sq.set(False)
Checkbutton(frame, text="Наличие осложнений", font='Arial 9', variable=sq).place(x=165, y=295)

acc = BooleanVar()
acc.set(False)
Checkbutton(frame, text="Несимметричный доступ", font='Arial 9', variable=acc).place(x=165, y=315)

join = BooleanVar()
join.set(False)
Checkbutton(frame, text="Ошибки при наложении швов", font='Arial 9', variable=join).place(x=165, y=335)


def calculate_risk():
    age = int(vvod7.get())
    lg = int(vvod8.get())
    ka = int(vvod9.get())
    bleeding = int(vvod10.get())
    charlsone = int(vvod11.get())
    es = float(vvod12.get())
    sequela = sq.get()
    dindo = int(vvod13.get())
    access = acc.get()
    joint = join.get()

    is_bleeding = bleeding >= 1000
    risk = 0.80806 + 0.04355 * age - 0.07624 * lg + 0.0245 * ka - 1.366 * int(
        is_bleeding) - 1.4601 * charlsone - 0.30636 * es - 1.37319 * int(sequela) - 0.34939 * dindo - 0.94 * int(
        access) - 1.46815 * int(joint)
    if risk > -0.650215:
        result.config(text=f"Риск развития осложнений: {risk}\nОсложнения маловероятны")
    else:
        result.config(text=f"Риск развития осложнений: {risk}\nПрогнозируется наличие осложнений")

result = Label(text='',font=15)
result.place (x=40,y=450)


btn = ttk.Button(text="Рассчитать",width=60, command=calculate_risk)
btn.place(x=40, y=390)

window.mainloop()



