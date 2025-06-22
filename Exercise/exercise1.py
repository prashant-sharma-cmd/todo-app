import PySimpleGUI as Sg

feet = Sg.Text("Enter feet:")
feet_input = Sg.Input(tooltip="Enter feet")
inches = Sg.Text("Enter inches:")
inches_input = Sg.Input(tooltip="Enter inches")
convert_button = Sg.Button("Convert")

windows = Sg.Window("Convertor", layout=[[feet, feet_input],
                                              [inches, inches_input],
                                              [convert_button]])
windows.read()
windows.close()