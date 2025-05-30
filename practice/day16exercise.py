import FreeSimpleGUI as sg

text1 = sg.Text("Enter feet:")
text2 = sg.Text("Enter inches:")
input1 = sg.Input()
input2 = sg.Input()
convert_btn = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[text1, input1], [text2, input2], [convert_btn]])

window.read()
window.close()