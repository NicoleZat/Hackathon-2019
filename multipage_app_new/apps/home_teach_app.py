# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app

font_color1 = '#EEEEEE'
back_color1 = '#2F4894'
back_color2 = '#4EC5E8'

# image_directory = '/Users/Dell/Documents/Hackathon 2019/Hackathon-2019/Hackathon-2019/multipage_app/apps/images'
 
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
                        html.Img(
                            src='https://i.imgur.com/Qp1SMwQ.png',
                            style={
                                'margin':10,
                                'height': '80%',
                                # 'width': '10%'
                                   }
                        ),
                        #ul list components
                        html.Ul(
                            children=[
                               html.Li(html.A('Home', href='/', style={'color': font_color1})),
                               html.Li(html.A('Tool Lookup', href='/apps/tool',style={'color': font_color1})),
                               html.Li(html.A('Tutorial Videos', href='/apps/vid',style={'color': font_color1})),
                            ],
                            id='nav-mobile',
                            className='right hide-off-med-and-down'
                        ),
                    ],
                    className='nav-wrapper'
                ),style={'background-color':back_color1}),
        ],
        className='navbar-fixed'
    ),
    
    html.Div(
        html.Center(
            children=[
            html.Img(
            src='https://i.imgur.com/vBjolrr.png',
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0
            }),
                html.Center(
        html.H1('''Breaking Open the Black Box
    '''), style={'padding-bottom': 100})
             ], style={'padding-bottom': 0})
    ),
    html.Div(
        children=[
            html.Center(
                html.H3('What is this website?'),style={'padding-top': 50,'text-shadow': '0.5px 0.5px gray'}),
            html.Center(
            html.H5('The healthcare field needs more tech-savvy professionals, like you, to understand and smartly leverage Artificial Intelligence (AI) technology. At the 2019 Mount Sinai Health Hackathon we set about to make AI more accesible to those working in a healthcare setting. This website provides access to explanations of AI tools used in the health care setting today as well as the concepts behind these tools'),style={'padding': 100,'text-shadow': '0.5px 0.5px gray'}
        )],style={
        'backgroundColor': back_color2,
        'border': 'grey',
        'padding': '50px 10px 10px',
        'box-shadow': '5px 5px 5px #888888'}
    ),
    html.Div(
        children=[
            html.Center(
            html.H3('How should you use this website?'),style={'padding-top': 50,'color':font_color1,'text-shadow': '0.5px 0.5px black'}),
            html.Center(
            html.H5('Start with what interests or drives you: Is it existing AI tools and how they aid in medical decision-making? Or do you want to understand the statistical concepts underpinning AI? Go at your own pace - spend 5 seconds getting the quick info, or spend 5 hours diving deeper and deeper. Learn how you want, for as long as you want.'),
            style={'padding': 100,'color':font_color1,'text-shadow': '0.5px 0.5px black'}
        )],style={
        'backgroundColor':back_color1,
        'border': 'grey',
        'padding': '50px 10px 50px',
        'box-shadow': '5px 5px 5px #888888'}
    ),
    html.Center(
        children=[
        html.H3('Choose where you want to start:'),
        html.A([
            html.Img(
                    src='https://i.imgur.com/BV0MYj2.png',
                    style={
                        'height' : '35%',
                        'width' : '35%',
                        'float' : 'center',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0,
                        'padding' : 40,
                        'border-radius': '100px'
                    })], href='/apps/tool'),
        html.A([
            html.Img(
                    src='https://i.imgur.com/L4neq6h.png',
                    style={
                        'height' : '35%',
                        'width' : '35%',
                        'float' : 'center',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0,
                        'padding': 40,
                        'border-radius': '100px'
            })], href='/apps/vid')], style={'padding': 100})

    ]
)

# if __name__ == '__main__':
#     app.run_server(debug=True)