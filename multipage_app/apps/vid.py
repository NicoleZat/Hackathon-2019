# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app


import base64
image_filename = 'static/test.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
filler_image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30,
                'opacity': 0.5,
                'box-shadow': '5px 5px 5px #888888'
            })
filler_list = [filler_image]*6

image_filename = 'static/aiBrain.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
our_thumbnail = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30,
                'box-shadow': '5px 5px 5px #888888'
            })
video_list = [html.A(our_thumbnail, href='/apps/logic')]
    
#     [html.Iframe(src = 'https://www.youtube.com/embed/mY4AmqIRTZI',
# style={
#                 'width':'25%',
#                 'margin': 30
#             })]


#############
# Layout

layout = html.Div(
    id='main-page-content',children= [
        html.Div(
            children=[
                # nav bar
                html.Nav(
                    # inside div
                    html.Div(
                        children=[
                            html.Img(
                                src='https://i.imgur.com/Qp1SMwQ.png',
                                style={
                                    'margin': 10,
                                    'height': '80%',
                                    # 'width': '10%'
                                }
                            ),
                            # ul list components
                            html.Ul(
                                children=[
                                    html.Li(html.A('Home', href='/')),
                                    html.Li(html.A('Tool Lookup', href='/apps/tool')),
                                    html.Li(html.A('Tutorial Videos', href='/apps/vid')),
                                ],
                                id='nav-mobile',
                                className='right hide-off-med-and-down'
                            ),
                        ],
                        className='nav-wrapper'
                    ), style={'background-color': '#66ccff'}),
            ],
            className='navbar-fixed'
        ),
    html.Div(
        html.Center(
            children=[
                html.H1('Video Tutorials'),
                html.H5('Search for the topic area you would like to know more about, or browse available videos:')
            ]
    ),
    ),
        html.Center(
            html.Div([
                dcc.Input(
                    id='search_val',
                    type='text',
                    value = '',
                    placeholder= 'Start typting to search',
                    style={
                        'margin':30,
                        'width': '50%'
                    }
                ),
    ])),
        html.Center(
    html.Div(id='output_container', children=[]))
    ])

################
# Callbacks

@app.callback(
    [Output('output_container', 'children')],
    [Input('search_val', 'value')]
)

def search_option_update(search_val):
    length= len(search_val)
    if search_val == '':
        return [video_list + filler_list]
    if search_val.lower() == 'sepsis'[:length]:
        return video_list
    return [video_list + filler_list]

if __name__ == '__main__':
    app.run_server(debug=True)
