import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet:")
label_inches = sg.Text("Enter inches:")
input_feet = sg.Input(key="feet")
input_inches = sg.Input(key="inches")
convert_btn = sg.Button("Convert")
output_meters = sg.Text("", key="output")

window = sg.Window('Convertor',
                   layout=[[label_feet, input_feet], [label_inches, input_inches], [convert_btn, output_meters]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    feet = int(values["feet"])
    inches = int(values["inches"])
    feet_to_meters =  round(feet * 0.3048, 3)
    inches_to_meters = round(inches * 0.0254, 3)
    meters_total = feet_to_meters + inches_to_meters

    window["output"].update(value=f"{meters_total} m")

window.close()