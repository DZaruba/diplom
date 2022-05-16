#Данный скрипт отвечает за создание графиков о состояннии окружающей среды рабочего
import request_MySQL as req #Обращаемся к выгрузке

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

def cr_image ():

    pmh, alt, temp, time_line = req.query_env()

    fig = go.Figure()
    fig = make_subplots(rows=2, cols=2, subplot_titles = ('График атмосферного давления', 'График высоты над уровнем моря', 'Температура окружающей среды рабочего'))

    fig.add_trace(go.Scatter(x = time_line, y = pmh, name = 'Атмосферное давление'), 1, 1)
    fig.add_trace(go.Scatter(x = time_line, y = alt, name = 'Высота над уровнем моря'), 1, 2)
    fig.add_trace(go.Scatter(x = time_line, y = temp, name = 'Температура'), 2, 1)

    fig.update_layout(title = 'Состояние окружающей среды у рабочего №1')
    fig.update_xaxes(title = 'Время', row = 1, col = 1)
    fig.update_yaxes(title='мм.рт.ст.', row = 1, col = 1)
    fig.update_xaxes(title='Время', row = 1, col = 2)
    fig.update_yaxes(title='м. над уровнем моря', row = 1, col = 2)
    fig.update_xaxes(title='Время', row = 2, col = 1)
    fig.update_yaxes(title='Градусы Цельсия', row = 2, col = 1)

    return fig.to_image(format="png", width=1200, height=700, scale=2)