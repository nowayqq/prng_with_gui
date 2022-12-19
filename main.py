import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pylab import rcParams
from middleSquares import get_values_ms
from middleMult import get_values_mm
from mixing import get_values_mix
from lcm import get_values_lcm


rcParams['figure.figsize'] = 16, 6.5

_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False,
         'dataSize': 100,
         'seed': None,
         'max_value': 100,
         'method': 0,
         'toggle': True}

_METHODS = ['Middle squares', 'Middle multiplications',
            'Mixing', 'Linear congruent']

plt.style.use('Solarize_Light2')


def draw_figure(canvas, figure):

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


AppFont = 'Any 16'
SliderFont = 'Any 14'
sg.theme('black')

layout = [[sg.Canvas(key='figCanvas', background_color='#FDF6E3')],
          [sg.Combo(_METHODS, size=(20, 0),
                    enable_events=True, key='-LIST-',
                    default_value=_METHODS[0],
                    background_color='Grey',
                    text_color='Black',
                    pad=((36, 0), (10, 0)),
                    readonly=True),
           sg.Text(text="Random sample size: ",
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
                     pad=((4, 200), (0, 0)), size=(10, 0))],
          # pad ((left, right), (top, bottom))
          [sg.Button('Toggle', font=AppFont, pad=((58, 0), (0, 0)), size=(10, 0)),
           sg.Input(key='-IN-', pad=((10, 0), (10, 0)), size=(25, 0), text_color='Black', background_color='Grey'),
           sg.Button('Set seed', font=AppFont, pad=((0, 9), (0, 0)), size=(10, 0)),
           sg.Button('Set MaxValue', font=AppFont, pad=((0, 8), (0, 0)), size=(10, 0))],
          [sg.Button('Exit', font=AppFont, pad=((504, 0), (3, 0)), size=(10, 0))]]

_VARS['window'] = sg.Window('PRNG',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(0, 0),
                            element_justification="center",
                            background_color='#FDF6E3')


def chooseMethod(val):

    if val == 0:
        return get_values_ms(seed=_VARS['seed'], size=_VARS['dataSize'], maxvalue=_VARS['max_value'])

    if val == 1:
        return get_values_mm(seed=_VARS['seed'], size=_VARS['dataSize'], maxvalue=_VARS['max_value'])

    if val == 2:
        return get_values_mix(seed=_VARS['seed'], size=_VARS['dataSize'], maxvalue=_VARS['max_value'])

    if val == 3:
        return get_values_lcm(seed=_VARS['seed'], size=_VARS['dataSize'], maxvalue=_VARS['max_value'])


def makeSynthData():

    yData = chooseMethod(_VARS['method'])
    xData = np.linspace(0, _VARS['dataSize'],
                        num=_VARS['dataSize'], dtype=int)

    return (xData, yData)


def drawChart():

    _VARS['pltFig'] = plt.figure()
    dataXY = makeSynthData()
    plt.plot(dataXY[0], dataXY[1], '.k')
    rnd.seed(_VARS['seed'])
    if (_VARS['max_value'] == 1):
        plt.scatter(dataXY[0], [rnd.random() for i in range(_VARS['dataSize'])], color='orange', s=10)
    else:
        plt.scatter(dataXY[0], [rnd.randrange(_VARS['max_value']) for i in range(_VARS['dataSize'])], color='orange', s=10)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


def updateChart():

    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = makeSynthData()
    # plt.cla()
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    rnd.seed(_VARS['seed'])
    if (_VARS['max_value'] == 1) and _VARS['toggle']:
        plt.scatter(dataXY[0], [rnd.random() for i in range(_VARS['dataSize'])], color='orange', s=10)
    elif _VARS['toggle']:
        plt.scatter(dataXY[0], [rnd.randrange(_VARS['max_value']) for i in range(_VARS['dataSize'])], color='orange', s=10)
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


def updateMethod(val):

    if val == _METHODS[0]:
        _VARS['method'] = 0
        updateChart()
    elif val == _METHODS[1]:
        _VARS['method'] = 1
        updateChart()
    elif val == _METHODS[2]:
        _VARS['method'] = 2
        updateChart()
    elif val == _METHODS[3]:
        _VARS['method'] = 3
        updateChart()


def updateToggle():

    if _VARS['toggle']:
        _VARS['toggle'] = False
        updateChart()
    else:
        _VARS['toggle'] = True
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
    elif event == '-LIST-':
        updateMethod(values['-LIST-'])
    elif event == 'Toggle':
        updateToggle()

_VARS['window'].close()
