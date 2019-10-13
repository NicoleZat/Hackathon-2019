# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html

#############
# Layout
from astropy.convolution.tests.test_convolve_kernels import width

layout = html.Div(
    id='main-page-content',children= [
    html.Div(
        children=[
            #nav bar
            html.Nav(
                #inside div
                html.Div(
                    children=[
                        html.A(
                            html.Img(
                                src='https://i.imgur.com/Qp1SMwQ.png',
                                style={
                                    'margin': 10,
                                    'height': '80%',
                                    # 'width': '10%'
                                }
                            ), href='/'),
                        #ul list components
                        html.Ul(
                            children=[
                                html.Li(html.A('Home', href='/')),
                                html.Li(html.A('Search by Specialty', href='/apps/organ')),
                                html.Li(html.A('Tool Lookup', href='/apps/tool')),
                                html.Li(html.A('Tutorial Videos', href='/apps/vid')),
                                html.Li(html.A('Data Sets', href='/apps/data')),
                            ],
                            id='nav-mobile',
                            className='right hide-off-med-and-down'
                        ),
                    ],
                    className='nav-wrapper'
                ),style={'background-color':'#4c586f'}),
        ],
        className='navbar-fixed'
    ),
    html.Div(
        html.Center(
        dcc.Markdown('''
#### AI Medical Tool Lookup
select the tool you would like to know more about:

    ''')
    ),
    ),
    html.Div([
    dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    ),
    html.Div(id='output-container')
],style={'textAlign': 'center'})

    ])

# html.Div(
#     [
#         html.Img(src='data:image/png;base64,{}'.format(encoded_image)),
#         html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
#     ],
#     className="row"
# ),
# html.Div(
#     [
#         html.Div(graph3, className="six columns"),
#         html.Div(graph4, className="six columns")
#     ],
#     className="row"
# ),

if __name__ == '__main__':
    app.run_server(debug=True)