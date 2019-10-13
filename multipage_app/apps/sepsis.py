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

video_list = [html.Iframe(src = 'https://www.youtube.com/embed/mY4AmqIRTZI',
style={
                'width':'25%',
                'margin': 30
            })]

image_filename = 'static/sepsis.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
our_thumbnail = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30
            })

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
                ),style={'background-color':back_color1}),
        ],
        className='navbar-fixed'
    ),



    html.Div([
        # our_thumbnail,
        html.H1('Sepsis',
        style={
            'margin-left':30
        }),
    ], style={'margin-top': 0, 'backgroundColor':back_color2}),
    html.Center(html.Div(children= video_list, style={'size':300})),
    html.H3('Interactive Tools', style={'margin-left': 30}),
    html.A('Sepsis AI', href='/apps/', style={'margin-left': 30}),
    html.H6(' '),
    html.A('Concepts behind Sepsis AI: Linear Regression', href='/apps/logic', style={'margin-left': 30}),
    html.H6(' '),
    html.H3('More about Sepsis', style={'margin-left': 30}),
    html.H5('Development of CARS', style={'margin-left': 30}), 
    dcc.Markdown('''Used scatter plots and box plots to show relationships between patient variables and the outcome of sepsis (e.g. temp & sepsis, AKI score & sepsis)
Developed a logistic regression model (CARS) 
Logistic regression: performs linear regression (modelling the relationship between an outcome and an independent variable) to try and explain the relationship between one or more independent variables 
CARS weights different variables (patient vitals & lab information) to predict how various combinations of patient data can predict a patient’s probability of developing sepsis within hours of an admission/when results are available.
Based on the preliminary modelling, AKI, patient consciousness,and WBCs had greater effect on whether a patient would develop sepsis, however, all variables previously mentioned are taken into account to determine a patient’s propensity for developing sepsis and severe sepsis. 
 ''' ),
    html.H5('How reliable is the prediction?', style={'margin-left': 30}),
    dcc.Markdown('''The model was based on over 26,000 ED admissions.The model has good a c-statistic (coordination statistic) of 0.73  for all sepsis, 0.78 sepsis, & 0.80 for severe sepsis. For c-statistics, 1=perfect prediction and 0.5= a coin flip. The c-statistic explains how well a model can discriminate a sepsis case from a non-sepsis case.
The c-statistic also has a narrow 95% confidence interval, which further demonstrates the strength of the CARS model in predicting patient sepsis. 
The model stikes a balance between sensitivity and specificity as a tool 
Why use it: This model provides an automated estimate of the risk of sepsis in ED admitted patients based on the earliest vitals and lab data collected. It doesn’t require any additional clinical time or data collection for prediction of patient outcome
Aids in effortless early detection of sepsis using information already gathered on patients. 
To consider: model fitted for blood culture data, uses ICD-10 code & consensus definition of sepsis

    ''')
    ])



if __name__ == '__main__':
    app.run_server(debug=True)