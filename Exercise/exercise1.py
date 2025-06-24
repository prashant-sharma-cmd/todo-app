import PySimpleGUI as Sg
from converter import convert

Sg.theme("Black")

feet = Sg.Text("Enter feet:")
feet_input = Sg.Input(tooltip="Enter feet", key="feet")
inches = Sg.Text("Enter inches:")
inches_input = Sg.Input(tooltip="Enter inches", key="inches")
convert_button = Sg.Button("Convert", key="convert")
exit_button = Sg.Button("Exit", key="exit")
output = Sg.Text("", key="output")

windows = Sg.Window("Convertor", layout=[[feet, feet_input],
                                              [inches, inches_input],
                                              [convert_button, exit_button, output]])

while True:
    event, values = windows.read()
    match event:
        case "convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = convert(feet, inches)
                windows["output"].update(value=result)
            except ValueError:
                Sg.popup("Please provide two numbers.")
                continue

        case "exit":
            break

        case Sg.WIN_CLOSED:
            break

windows.close()