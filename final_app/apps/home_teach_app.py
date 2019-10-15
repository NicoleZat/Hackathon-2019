# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app
import base64

font_color1 = '#EEEEEE'
back_color1 = '#2F4894'
back_color2 = '#4EC5E8'

# image_directory = '/Users/Dell/Documents/Hackathon 2019/Hackathon-2019/Hackathon-2019/multipage_app/apps/images'
logo_big = 'static/Blackbox logo big.png'
encoded_image = base64.b64encode(open(logo_big, 'rb').read())
logo_big_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 50,
                'padding-right' : 0
            })

logo_small = 'static/Blackbox logo-02.png'
encoded_image = base64.b64encode(open(logo_small, 'rb').read())
logo_small_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '80%',
                'margin': 10
            })

background_design = 'static/giphy.gif'
encoded_image = base64.b64encode(open(background_design, 'rb').read())
background_design_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding' : 40,
                'border-radius': '100px'
            })

background_stars = 'static/Code_data.jpg'
encoded_image = base64.b64encode(open(background_stars, 'rb').read())
background_stars_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding': 40,
                'border-radius': '100px',
                'opacity': '70%'
            })

button1 = 'static/button-09.png'
encoded_image = base64.b64encode(open(button1, 'rb').read())
button1_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding' : 40,
                'border-radius': '100px'
            })

button2 = 'static/button-10.png'
encoded_image = base64.b64encode(open(button2, 'rb').read())
button2_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding': 40,
                'border-radius': '100px',
                'opacity': '70%'
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
                ) ,style={'background-color':'#151E3D'}),
        ],
        className='navbar-fixed'
    ),

    html.Div(
        html.Center(
            children=[
                logo_big_thumb,
                html.Center(
        html.H1('''Breaking Open the Black Box
    '''), style={'padding-bottom': 100})
             ], style={'padding-bottom': 0,'background-image':'url("/static/17260961.png")'})
    ),
    html.Div(
        children=[
            html.Center(
                html.H3('What is this website?',style={'color':'white'}),style={'padding-top': 50,'text-shadow': '0.5px 0.5px gray'}),
            html.Center(
            html.H5('The healthcare field needs more tech-savvy professionals, like you, to understand and smartly leverage Artificial Intelligence (AI) technology. At the 2019 Mount Sinai Health Hackathon we set about to make AI more accesible to those working in a healthcare setting. This website provides access to explanations of AI tools used in the health care setting today as well as the concepts behind these tools',style={'color':'white'}),style={'padding': 100,'text-shadow': '0.5px 0.5px gray'}
        ,className='slim-paragraph')],style={
        'backgroundColor': back_color2,
        'border': 'grey',
        'padding': '50px 10px 10px',
        'box-shadow': '5px 5px 5px #888888',
        'background-image': 'url("/static/giphy.gif")'}
    ),
    html.Div(
        children=[
            html.Center(
            html.H3('How should you use this website?',style={'color':'white'}),style={'padding-top': 50,'color':font_color1,'text-shadow': '0.5px 0.5px black'}),
            html.Center(
            html.H5('Start with what interests or drives you: Is it existing AI tools and how they aid in medical decision-making? Or do you want to understand the statistical concepts underpinning AI? Go at your own pace - spend 5 seconds getting the quick info, or spend 5 hours diving deeper and deeper. Learn how you want, for as long as you want.',style={'color':'white'}),
            style={'padding': 100,'color':font_color1,'text-shadow': '0.5px 0.5px black'},className='slim-paragraph'
        )],style={
        'backgroundColor':back_color1,
        'border': 'grey',
        'padding': '50px 10px 50px',
        'box-shadow': '5px 5px 5px #888888',
        'background-image': 'url("/static/Code_data.jpg")'
        }
    ),
    html.Center(
        children=[
        html.H3('Choose where you want to start:'),
            html.A(button1_thumb, href='/apps/tool'),
            html.A(button2_thumb, href='/apps/vid')], style={'padding': 100})

    ]
)

# if __name__ == '__main__':
#     app.run_server(debug=True)