import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import figureBackend
import numpy as np
from app import app

font_color1 = '#EEEEEE'
back_color1 = '#2F4894'
back_color2 = '#4EC5E8'

#Initialize all backend interfaces for examples
example1 = figureBackend.Example()
example1.initData("sepsis_mockup_good.csv")
example2 = figureBackend.Example()
example2.initData("sepsis_mockup_bad.csv")
example3 = figureBackend.Example()
example3.initData("sepsis_mockup.csv")

layout = html.Div(children=[
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

    html.H1(children='Logistic Regression'),

    html.Div(children='''
        Use the sliders to move the decision boundary line. A strong predictor completely separates the healthy patients from those with sepsis.
    '''),


    dcc.Graph(
        id='LR-1'
    ),

    html.Label('Change Slope'),
    dcc.Slider(
        id = 'slidem1',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),

    html.Label('Change Intercept'),
    dcc.Slider(
        id = 'slideb1',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),
    html.H3('Accuracy Statistics'),
    html.H6('This pie chart records the number of patients who are correctly and incorrectly identified. A good model will have few false positives and false negatives.'),
    dcc.Graph(
        id = 'pie-chart-1'
    ),
    html.H3('Difficult Prediction'),
    html.H6('In this example, there is less to distinguish septic patients from healthy. You will find it more difficult to accurately segment the population using the decision boundary.'),
    dcc.Graph(
        id='LR-2'
    ),

    html.Label('Change Slope'),
    dcc.Slider(
        id = 'slidem2',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),

    html.Label('Change Intercept'),
    dcc.Slider(
        id = 'slideb2',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),

    
    dcc.Graph(
        id = 'pie-chart-2'
    ),
    html.H3('Worst Case Prediction'),
    html.H6('In the worst case, septic patients are thoroughly mixed with healthy patients. This is indicative of poor model performance, where it will be impossible to draw a decision boundary that effectively segments the population.'),
    
    dcc.Graph(
        id='LR-3'
    ),

    html.Label('Change Slope'),
    dcc.Slider(
        id = 'slidem3',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),

    html.Label('Change Intercept'),
    dcc.Slider(
        id = 'slideb3',
        min=-50,
        max=50,
        # marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=0,
    ),

    dcc.Graph(
        id = 'pie-chart-3'
    ),

])

@app.callback(Output('LR-1', 'figure'), [Input('slidem1', 'value'), Input('slideb1', 'value')])
def update_graph1(slider1, slider2):
    return {
        'data' : [
            go.Scatter(
                x = example1.getHealthyXData(),
                y = example1.getHealthyYData(),
                name = "Healthy",
                showlegend = True,
                mode = "markers",
                marker = {'symbol': "square", 'color' : back_color1}
            ),
            go.Scatter(
                x = example1.getSepsisXData(),
                y = example1.getSepsisYData(),
                name = "Sepsis",
                mode = "markers",
                marker = dict(symbol="square", color= back_color2)
            ),
            go.Scatter(
                x = example1.getDBx(),
                y = example1.getDBy(slider1, slider2),
                name = "Decision Boundary",
                line = dict(color = "#D000CC", width = 3)
            )
        ],
        'layout': go.Layout(
            xaxis={
                'title': "Temperature", #TODO import from data package
            },
            yaxis={
                'title': "Heart Rate", #TODO: similar to above
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('pie-chart-1', 'figure'), [Input('slidem1', 'value'), Input('slideb1', 'value')])
def update_pie1(slider1, slider2):
    #Get the classification vector from the figure back end
    return {
        'data' : [
            go.Pie(
                labels = example1.getPieLabels(),
                values = example1.getPieVector(slider1, slider2),
                marker_colors = ["Red", "Blue", "LightBlue", "Pink"]
            )
        ]
    }

@app.callback(Output('LR-2', 'figure'), [Input('slidem2', 'value'), Input('slideb2', 'value')])
def update_graph2(slider1, slider2):
    return {
        'data' : [
            go.Scatter(
                x = example2.getHealthyXData(),
                y = example2.getHealthyYData(),
                name = "Healthy",
                showlegend = True,
                mode = "markers",
                marker = {'symbol': "square", 'color' : back_color1}
            ),
            go.Scatter(
                x = example2.getSepsisXData(),
                y = example2.getSepsisYData(),
                name = "Sepsis",
                mode = "markers",
                marker = dict(symbol="square", color= back_color2)
            ),
            go.Scatter(
                x = example2.getDBx(),
                y = example2.getDBy(slider1, slider2),
                name = "Decision Boundary",
                line = dict(color = "#D000CC", width = 3)
            )
        ],
        'layout': go.Layout(
            xaxis={
                'title': "Temperature", #TODO import from data package
            },
            yaxis={
                'title': "Heart Rate", #TODO: similar to above
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('pie-chart-2', 'figure'), [Input('slidem2', 'value'), Input('slideb2', 'value')])
def update_pie2(slider1, slider2):
    #Get the classification vector from the figure back end
    return {
        'data' : [
            go.Pie(
                labels = example2.getPieLabels(),
                values = example2.getPieVector(slider1, slider2),
                marker_colors = ["Red", "Blue", "LightBlue", "Pink"]
            )
        ]
    }

@app.callback(Output('LR-3', 'figure'), [Input('slidem3', 'value'), Input('slideb3', 'value')])
def update_graph3(slider1, slider2):
    return {
        'data' : [
            go.Scatter(
                x = example3.getHealthyXData(),
                y = example3.getHealthyYData(),
                name = "Healthy",
                showlegend = True,
                mode = "markers",
                marker = {'symbol': "square", 'color' : back_color1}
            ),
            go.Scatter(
                x = example3.getSepsisXData(),
                y = example3.getSepsisYData(),
                name = "Sepsis",
                mode = "markers",
                marker = dict(symbol="square", color=back_color2)
            ),
            go.Scatter(
                x = example3.getDBx(),
                y = example3.getDBy(slider1, slider2),
                name = "Decision Boundary",
                line = dict(color = "#D000CC", width = 3)
            )
        ],
        'layout': go.Layout(
            xaxis={
                'title': "Temperature", #TODO import from data package
            },
            yaxis={
                'title': "Heart Rate", #TODO: similar to above
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('pie-chart-3', 'figure'), [Input('slidem3', 'value'), Input('slideb3', 'value')])
def update_pie3(slider1, slider2):
        #Get the classification vector from the figure back end
        return {
            'data' : [
                go.Pie(
                    labels = example3.getPieLabels(),
                    values = example3.getPieVector(slider1, slider2),
                    marker_colors = ["Red", "Blue", "LightBlue", "Pink"]
                )
            ]
        }
if __name__ == '__main__':
    app.run_server(debug=True)
