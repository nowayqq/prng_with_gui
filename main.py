import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from middleSquares import get_values_ms
from pylab import rcParams

rcParams['figure.figsize'] = 16, 6.5

# VARS CONSTS:
# Upgraded dataSize to global...
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False,
         'dataSize': 100,
         'seed': None,
         'max_value': 100}

plt.style.use('Solarize_Light2')


# Helper Functions


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# \\  -------- PYSIMPLEGUI -------- //

AppFont = 'Any 16'
SliderFont = 'Any 14'
sg.theme('black')

# New layout with slider and padding

layout = [[sg.Canvas(key='figCanvas', background_color='#FDF6E3')],
          [sg.Text(text="Random sample size :",
                   font=SliderFont,
                   background_color='#FDF6E3',
                   pad=((0, 0), (10, 0)),
                   text_color='Black'),
           sg.Slider(range=(10, 10000), orientation='h', size=(34, 20),
                     default_value=_VARS['dataSize'],
                     background_color='#FDF6E3',
                     text_color='Black',
                     key='-Slider-',
                     enable_events=True),
           sg.Button('Resample',
                     font=AppFont,
                     pad=((4, 0), (0, 0)), size=(10, 0))],
          # pad ((left, right), (top, bottom))
          [sg.Input(key='-IN-', pad=((197, 0), (10, 0)), size=(24, 0), text_color='Black', background_color='Grey'),
           sg.Button('Set seed', font=AppFont, pad=((8, 0), (0, 0)), size=(10, 0)),
           sg.Button('Set MaxValue', font=AppFont, pad=((8, 0), (0, 0)), size=(10, 0))],
          [sg.Button('Exit', font=AppFont, pad=((512, 0), (3, 0)), size=(10, 0))]]

_VARS['window'] = sg.Window('Random Samples',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="center",
                            background_color='#FDF6E3')


# \\  -------- PYSIMPLEGUI -------- //


# \\  -------- PYPLOT -------- //


def makeSynthData():
    yData = get_values_ms(seed=_VARS['seed'], size=_VARS['dataSize'], maxValue=_VARS['max_value'])
    xData = np.linspace(0, _VARS['dataSize'],
                        num=_VARS['dataSize'], dtype=int)

    return (xData, yData)


def drawChart():
    _VARS['pltFig'] = plt.figure()
    dataXY = makeSynthData()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


def updateChart():
    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = makeSynthData()
    # plt.cla()
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


def updateData(val):
    _VARS['dataSize'] = val
    updateChart()


def updateMaxValue(val):
    try:
        _VARS['max_value'] = int(val)
        updateChart()
    except ValueError:
        _VARS['max_value'] = 100
        updateChart()


def updateSeed(val):
    try:
        _VARS['seed'] = int(val)
        updateChart()
    except ValueError:
        _VARS['seed'] = None
        updateChart()


drawChart()


while True:
    event, values = _VARS['window'].read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Resample':
        updateChart()
    elif event == '-Slider-':
        updateData(int(values['-Slider-']))
    elif event == 'Set seed':
        updateSeed(values['-IN-'])
    elif event == 'Set MaxValue':
        updateMaxValue(values['-IN-'])

_VARS['window'].close()
