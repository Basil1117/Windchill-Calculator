import PySimpleGUI as sg

sg.theme('DarkPurple4')

# Layout String Variables
title = "Wind Chill Calculator"
description = "A calculator that will help you know how cold it"
description += " feels outside based on the temperature and wind speed"
results = ""

# layout are all the Graphical UI objects row by row
layout = [
  [sg.Text(title, size=(30, 1), font=("Times New Roman", 18))],
  [sg.Text(description, size=(30,3))],
  [sg.Text("Temperature (F): "), sg.Input(size=(3, 1), key='-TEMP-')],
  [sg.Text("Wind Speed (mph): "), sg.Input(size=(3, 1), key='-WIND-')],
  [sg.Button('Get Wind Speed'), sg.Button('Exit')],
  [sg.Text(results, size=(30,3), key ='OUTPUT')]
]

window = sg.Window(title, layout)

# Our program loop
while True:
  event,values = window.read()
  print(event,values)
  if event == sg.WIN_CLOSED or event == 'Exit':
    break
  if event == 'Get Wind Chill':
    temp = values['-TEMP-']
    wind = values['-WIND-']

    # Calculate windchill and produce results

    # Output results
    msg = "You entered {} and {}".format(temp,wind)
    window['-OUTPUT'].update(msg)

# Close the window, very confusing
window.close()