import PySimpleGUI as sg
from nltk.sentiment import SentimentIntensityAnalyzer
model = SentimentIntensityAnalyzer()

# created a function out of model.polarity_scores
def PosOrNeg(n):
    dic = model.polarity_scores(n)
    if dic['compound'] < 0:
        return 'Negative Statement'
    elif dic['compound'] > 0:
        return 'Positive Statement'
    else:
        return 'Neutral Statement'




# # All the stuff inside your window.
layout = [[sg.Text('Enter the text to Analyze'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout, margins=(100, 50))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    lay = [[sg.Text(PosOrNeg(values[0]))]]
    window = sg.Window("State", lay, margins=(100, 50))

window.close()