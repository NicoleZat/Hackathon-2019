# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import base64

font_color1 = '#EEEEEE'
back_color1 = '#2F4894'
back_color2 = '#4EC5E8'


images = ['static/sepsis.png', 'static/i1.png','static/i2.png', 'static/i3.png', 'static/i4.png', 'static/i5.png', 'static/i6.png']
image_list = []

for image in images:
    encoded_image = base64.b64encode(open(image, 'rb').read())
    decoded_image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30
            })
    if image == 'static/sepsis.png':
        decoded_image = html.A(decoded_image, href='/apps/sepsis')
    image_list += [decoded_image]

logo_small = 'static/Blackbox logo-02.png'
encoded_image = base64.b64encode(open(logo_small, 'rb').read())
logo_small_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '80%',
                'margin': 10
            })


#############
# Layout

layout = html.Div(
    id='main-page-content',children= [

        html.Div(
        children=[
            #nav bar
            html.Nav(
                #inside div
                html.Div(
                    children=[
                        html.A(logo_small_thumb, href='/'),
                        # ul list components
                        html.Ul(
                            children=[
                                html.Li(html.A('Home', href='/', style={'color': font_color1})),
                                html.Li(html.A('Tool Lookup', href='/apps/tool', style={'color': font_color1})),
                                html.Li(html.A('Tutorial Videos', href='/apps/vid', style={'color': font_color1})),
                            ],
                            id='nav-mobile',
                            className='right hide-off-med-and-down'
                        ),
                    ],
                    className='nav-wrapper'
                ), style={'background-color': '#151E3D'})
        ],
        className='navbar-fixed'
    ),

    html.Div(children=[
        html.Center(
            children=[
            html.H1(' Tool Lookup'),
            html.H5('Search for AI projects in your field of interest')]
    ),
        html.Center(
    dcc.Input(
            id='search_val2',
            type='text',
            value = '',
            placeholder= 'Start typing to search',
            style={
                'margin':30,
                'width': '50%'
            }
        ))
    ]
        # ,style={'backgroundColor':back_color2}
    ),
html.Center(
    html.Div(id='search_out', children=[]))
    ])

################
# Callbacks

@app.callback(
    [Output('search_out', 'children')],
    [Input('search_val2', 'value')]
)

def search_option_update(search_val):
    length= len(search_val)
    if search_val == '':
        return [image_list]
    if search_val.lower() == 'sepsis'[:length]:
        encoded_image = base64.b64encode(open('static/sepsis.png', 'rb').read())
        decoded_image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30
            })
        return [html.A(decoded_image, href='/apps/sepsis')]
    return [image_list]

if __name__ == '__main__':
    app.run_server(debug=True)