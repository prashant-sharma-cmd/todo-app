from zip_extractor import extract_archive
import PySimpleGUI as Sg

Sg.theme("DarkGrey")

label1 = Sg.Text("Select archive to extract:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose", key="archive")
label2 = Sg.Text("Select destination folder:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")
output_label = Sg.Text(key="Output", text_color="green")

window = Sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archive = values["archive"]
            folder = values["folder"]
            extract_archive(archive, folder)
            window['Output'].update(value="Compression is completed successfully.")
        case Sg.WIN_CLOSED:
                break

window.close()