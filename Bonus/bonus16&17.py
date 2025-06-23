from zip_creator import make_archive
import PySimpleGUI as Sg

label1 = Sg.Text("Select files to compress:")
input1 = Sg.Input()
choose_button1 = Sg.FilesBrowse("Choose", key="files")
label2 = Sg.Text("Select destination folder:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

compress_button = Sg.Button("Compress")
output_label = Sg.Text(key="Output")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"]
            files = filepaths.split(";")
            folder = values["folder"]
            make_archive(files, folder)
            window['Output'].update(value="Compression is completed successfully.")
        case Sg.WIN_CLOSED:
                break

window.close()