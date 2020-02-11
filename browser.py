import PySimpleGUI as sg

sg.theme('LightGreen3')

from test import te,mod,cre,trm,md,size,direc

tasks=[]
#read(tasks)

layout = [
    [sg.Text('File Browser')],
    [sg.Text('Browse file',size=(8, 1)), sg.Input("", key="in"), sg.FileBrowse()],

    [sg.Checkbox(' show Directory', size=(25, 1))],
    [sg.Button(button_text="Submit", key="sub")],

    [sg.Text('Your File Properties are')],
    [sg.Listbox(values=tasks, size=(40, 10), key="items")],



]

window = sg.Window('File Browser', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event =="sub":
        input=values['in']
        #window.FindElement('items').Update(values=tasks)
        #tasks.append(values[0])
        tasks= te(input)
        window.FindElement('items').Update(values=tasks)
        tasks=mod(input)
        window.FindElement('items').Update(values=tasks)
        tasks=cre(input)
        window.FindElement('items').Update(values=tasks)
        tasks=trm(input)
        window.FindElement('items').Update(values=tasks)
        tasks=md(input)
        window.FindElement('items').Update(values=tasks)
        tasks=size(input)
        window.FindElement('items').Update(values=tasks)
        tasks=direc(input)
        window.FindElement('items').Update(values=tasks)


    elif event == None:
        break




window.Close()



