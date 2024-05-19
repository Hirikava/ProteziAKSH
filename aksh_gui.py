from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from aksh_domain import calculate_risk_of_sequela
from aksh_data import save_result_to_csv
from datetime import *
from dateutil.relativedelta import relativedelta

window = Tk()

window.title('Прогнозирование осложнений АКШ')
window.geometry('450x550')
window.resizable(width=False, height=False)

frame = Frame(window)
frame.place(relwidth=1, relheight=1)

patient = Label(frame, text='Пациент', font='Arial 12', fg='green').place(x=3, y=4)
secondname = Label(frame, text='*Фамилия:', font='Arial 9').place(x=3, y=25)
name = Label(frame, text='*Имя', font='Arial 9').place(x=3, y=65)
thirdname = Label(frame, text='*Отчество', font='Arial 9').place(x=3, y=105)
birthday = Label(frame, text='*Дата рождения:', font='Arial 9').place(x=153, y=25)
ngosp = Label(frame, text='№ госпитализации:', font='Arial 9').place(x=156, y=65)
gospdate = Label(frame, text='Дата госпитализации:', font='Arial 9').place(x=158, y=105)
pokazateli = Label(frame, text='Показатели', font='Arial 12', fg='red').place(x=3, y=150)
age = Label(frame, text='Возраст пациента:', font='Arial 9').place(x=3, y=175)
lg = Label(frame, text='Давление в ЛА (мм.рт.ст):', font='Arial 9').place(x=3, y=215)
ca1 = Label(frame, text='Cтепень', font='Arial 9').place(x=45, y=255)
ca2 = Label(frame, text='поражения КА (%):', font='Arial 9').place(x=15, y=275)
bleed1 = Label(frame, text='Интраоперационная', font='Arial 9').place(x=10, y=315)
bleed2 = Label(frame, text='кровопотеря (мл.):', font='Arial 9').place(x=20, y=335)
Charlson = Label(frame, text='Charlson Index:', font='Arial 9').place(x=170, y=175)
es = Label(frame, text='Euroscore (%):', font='Arial 9').place(x=170, y=215)
Dindo = Label(frame, text='Clavien-Dindo (1-5):', font='Arial 9').place(x=170, y=255)
Result_label = Label(frame, text='Результат', font='Arial 12', fg='blue').place(x=3, y=420)

first_name_entry = Entry(frame)
first_name_entry.place(relheight=0.03, relwidth=0.3, x=10, y=45)
second_name_entry = Entry(frame)
second_name_entry.place(relheight=0.03, relwidth=0.3, x=10, y=85)
surname_entry = Entry(frame)
surname_entry.place(relheight=0.03, relwidth=0.3, x=10, y=125)
birth_date_entry = DateEntry(frame, width=30, bg="darkblue", fg="white", locale='ru_RU', date_pattern='mm/dd/yyyy')
birth_date_entry.place(relheight=0.03, relwidth=0.3, x=160, y=45)

ngosp_entry = Entry(frame)
ngosp_entry.place(relheight=0.03, relwidth=0.3, x=160, y=85)
date_gosp_entry = DateEntry(frame, width=30, bg="darkblue", fg="white")
date_gosp_entry.place(relheight=0.03, relwidth=0.3, x=160, y=125)
age_variable = StringVar()
age_entry = Entry(frame, textvariable=age_variable)
age_entry.place(relheight=0.03, relwidth=0.3, x=4, y=195)
lg_entry = Entry(frame)
lg_entry.place(relheight=0.03, relwidth=0.3, x=4, y=235)
ca_entry = Entry(frame)
ca_entry.place(relheight=0.03, relwidth=0.3, x=4, y=295)
bleeding_entry = Entry(frame)
bleeding_entry.place(relheight=0.03, relwidth=0.3, x=4, y=355)
charlsone_entry = Entry(frame)
charlsone_entry.place(relheight=0.03, relwidth=0.3, x=170, y=195)
es_entry = Entry(frame)
es_entry.place(relheight=0.03, relwidth=0.3, x=170, y=235)
dindo_entry = Entry(frame)
dindo_entry.place(relheight=0.03, relwidth=0.3, x=170, y=275)


def date_entry_selected(event):
    w = event.widget
    date = w.get_date()
    age_variable.set(str(relativedelta(datetime.now(), date).years))


birth_date_entry.bind("<<DateEntrySelected>>", date_entry_selected)

genderlabel = Label(frame, text='Пол пациента:', font='Arial 9')
genderlabel.place(x=323, y=25)

gender = BooleanVar()
gender.set(False)
gender1 = Radiobutton(frame, text="Мужской", font='Arial 9', variable=gender, value="True")
gender2 = Radiobutton(frame, text="Женский", font='Arial 9', variable=gender, value="False")
gender1.place(x=323, y=45)
gender2.place(x=323, y=65)

separator = ttk.Separator(frame, orient=HORIZONTAL)
separator.place(relwidth=1.0, y=150)
separator2 = ttk.Separator(frame, orient=HORIZONTAL)
separator2.place(relwidth=1.0, y=420)

sq = BooleanVar()
sq.set(False)
Checkbutton(frame, text="Наличие осложнений", font='Arial 9', variable=sq).place(x=165, y=295)

acc = BooleanVar()
acc.set(False)
Checkbutton(frame, text="Несимметричный доступ", font='Arial 9', variable=acc).place(x=165, y=315)

join = BooleanVar()
join.set(False)
Checkbutton(frame, text="Ошибки при наложении швов", font='Arial 9', variable=join).place(x=165, y=335)
result = Label(text='', font=15)
result.place(x=40, y=450)


def calculate_action():
    age = int(age_variable.get())
    lg = int(lg_entry.get())
    ka = int(ca_entry.get())
    bleeding = int(bleeding_entry.get())
    charlsone = int(charlsone_entry.get())
    es = float(es_entry.get())
    sequela = sq.get()
    dindo = int(dindo_entry.get())
    access = acc.get()
    joint = join.get()
    risk = calculate_risk_of_sequela(age, lg, ka, bleeding, charlsone, es, sequela, dindo, access, joint)

    if risk > -0.650215:
        result.config(text=f"Риск развития осложнений: {risk}\nОсложнения маловероятны")
    else:
        result.config(text=f"Риск развития осложнений: {risk}\nПрогнозируется наличие осложнений")

    save_result_to_csv("result.csv", [first_name_entry.get(), second_name_entry.get(), surname_entry.get(), birth_date_entry.get_date(), ngosp_entry.get(), date_gosp_entry.get_date(), gender.get(),
                                      age, lg, ka, bleeding, charlsone, es, sequela, dindo, access, joint, risk])


btn = ttk.Button(text="Рассчитать и сохранить", width=60, command=calculate_action)
btn.place(x=40, y=390)

window.mainloop()
