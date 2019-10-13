import copy
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import math
from app import app
import base64

font_color1 = '#EEEEEE'
back_color1 = '#2F4894'
back_color2 = '#4EC5E8'

image_filename = 'static/sep1.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
sep1_thumbnail = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30
            })
image_filename = 'static/sep2.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
sep2_thumbnail = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'width':'25%',
                'margin': 30
            })

class Case:
    def __init__(self, Age, sex, oxygenSupp, haemoglobin, potassium, sodium, whiteCellCount, urea):
        self.Age = Age
        self.sex = sex
        self.oxygenSupp = oxygenSupp
        self.haemoglobin = haemoglobin
        self.potassium = potassium
        self.sodium = sodium
        self.whiteCellCount = whiteCellCount
        self.urea = urea

#NOTE: Globals might be a problem
healthyPatient = Case(66.7, "Male", 0, 125.7, 4.3, 136.7, 9.9, 7.8)
sickPatient = Case(74.5, "Female", 1, 120.6, 4.2, 135.8, 12.1, 8.2)

def computeLRModel(Age, sex, oxygenSupp, haemoglobin, potassium, sodium, whiteCellCount, urea):
    if(sex == "Male"):
         Male = 1
    else:
         Male = 0
    return 5.5-0.027*Male + 0.020*Age + 0.266*oxygenSupp - 0.016*haemoglobin - 0.182*math.log(potassium) - 0.012*sodium - 1.389*math.log(whiteCellCount)+ 0.078 * math.log(urea)

def computeLRModelFromCase(p):
    return computeLRModel(p.Age,p.sex,p.oxygenSupp,p.haemoglobin,p.potassium, p.sodium, p.whiteCellCount, p.urea)

def processCase(p):
    unprocessed = computeLRModelFromCase(p)
    return math.exp(unprocessed)/(1+math.exp(unprocessed))


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

    html.H1(children='CARS: Computer Aided Risk Score for Sepsis'),

    html.Div(id='result'),

    html.Div(id='patientbox'),

    dcc.Graph(
        id='example-graph',
    ),

    html.Label('Patient Examples'),
    dcc.Dropdown(
        id = 'examples',
        options=[
            {'label': 'Patient with Klebsella Liver Abscess', 'value': 'Patient 2'},
            {'label': 'Healthy Eldery Male with Dog Bite', 'value': 'Patient 1'},
            # {'label': 'Questionable Patient', 'value': 'Patient 3'}
        ],
        value='Patient 1'
    ),

    html.Label('Sex'),
    dcc.RadioItems(
        id = 'sex',
        options=[
            {'label': 'Male', 'value': 'm'},
            {'label': 'Female', 'value': 'f'},
        ],
        value='m'
    ),

    html.Label('Oxygen Supplementation'),
    dcc.RadioItems(
        id='oxy',
        options=[
            {'label': 'Yes', 'value': 'y'},
            {'label': 'No', 'value': 'n'},
        ],
        value='n'
    ),
    #TODO: Beautify
    #NOTE: Box values don't change with loading a different patient
    html.Label('Age'),
    dcc.Input(id='age',value=healthyPatient.Age, type='number'),

    html.Label('Haemoglobin'),
    dcc.Input(id='haemoglobin',value=healthyPatient.haemoglobin, type='number'),

    html.Label('Potassium'),
    dcc.Input(id='potassium',value=healthyPatient.potassium, type='number'),

    html.Label('Sodium'),
    dcc.Input(id='sodium',value=healthyPatient.sodium, type='number'),

    html.Label('White Cell Count'),
    dcc.Input(id='white',value=healthyPatient.whiteCellCount, type='number'),

    html.Label('Urea'),
    dcc.Input(id='urea',value=healthyPatient.urea, type='number'),

    html.H2('Logistic Regression in Sepsis', style={'margin': 30} ),

    html.H4('Why is this sepsis Logistic Regression model useful?', style={'margin': 30} ),
    html.H6('This model provides an automated estimate of the risk of sepsis in Emergency Department (ED) admitted patients based on the earliest vitals and lab data collected and resulted into a patient’s  Electronic-Health Record (EHR). This tool removes the need for additional clinical time in data collection and manual score calculation by predicting a patient’s propensity for sepsis fairly shortly after hospital admission with existing data. ', style={'margin': 30} ),
    
    html.H4('What is Logistic Regression?', style={'margin': 30} ),
    html.H6('Logistic regression is a mathematical modelling tool which classifies entities into groups based on the available data. ', style={'margin': 30} ),
    html.H6('In the healthcare setting, the entities are often patients, and the classes we aim to predict are diseases or conditions.  ', style={'margin': 30} ),
    html.H6('Logistic regression works by identifying linear relationships between predictor variables and the outcome variable. Then, it combines these contributions and transforms the data into a probability. In this example, the output is the probability that a patient will become septic.', style={'margin': 30} ),

    html.H4('How is Logistic Regression used in the CARS Sepsis predictive model?', style={'margin': 30} ),
    html.H6('For development of the CARS (Computed Aided RIsk of Sepsis) model, data from 26,000 patient ED admissions was analyzed using scatter and box plots to examine the relationship between patient variables and the outcome of sepsis. The variables analyzed comprise of age, sex, respiration rate, oxygen staturation, any supplemental oxygen, temperature, systolic blood pressure, heart rate, level of consciousness (alert, voice, pain, unrepsonsive), diastolic blood pressure, albumin, creatinine, hemoglobin, potassium, sodium, urea, white blood cell count (WBC), Acute Kidney Injury (AKI) score (0, 1, 2, 3), kidney function, and ICD-10 codes. ', style={'margin': 30} ),
    html.H6('The CARS model weights some variables with a closer correlation to an outcome of sepsis higher because those variables are stronger predictors for developing sepsis (Figure 1). Those variables were AKI, patient consciousness, and WBC. However, all the variables listed above are taken into account to determine a patient’s proclivity for developing sepsis and severe sepsis. ', style={'margin': 30} ),

    sep1_thumbnail,

    html.H4('How reliable is the prediction and what to look for when evaluating a Logistic Regression?', style={'margin': 30} ),
    html.H6('The CARS model has a good Coordination Statistic (c-statistic) of 0.73 for predicting all sepsis, 0.78 for sepsis, and 0.80 for severe sepsis. For c-statistics, a value of one is considered a perfect prediction and 0.5 is essentially a coin toss. The c-statistic explains how well a model can discriminate a sepsis case from a non-sepsis case. For this model, the 95 percent confidence intervals of the c-statistics are also very narrow, which further demonstrates the strength of the CARS model in predicting patient sepsis. ', style={'margin': 30} ),
    html.H6('Additionally, the model uses a cut-off in the calculated predictive score which strikes a balance between test sensitivity and specificity. Like most diagnostic tools, it’s hard to have a test that is both highly sensitive and very specific, so this model achieves an average of 70 percent sensitivity and specificity.' , style={'margin': 30} ),

    sep2_thumbnail
])

@app.callback([Output(component_id='result', component_property='children'),Output('example-graph','figure')],[Input(component_id='age', component_property='value'),
    Input(component_id='haemoglobin', component_property='value'),Input(component_id='potassium', component_property='value'),
    Input(component_id='sodium', component_property='value'),Input(component_id='white', component_property='value'),
    Input(component_id='examples', component_property='value'),Input(component_id='urea', component_property='value'),
    Input(component_id='sex', component_property='value'),Input(component_id='oxy', component_property='value')])
def update_output_div(age, haemoglobin, potassium, sodium, white, example, urea, Sex, Oxy):
    if(age == None):
        age = 0
    if(haemoglobin == None):
        haemoglobin = 0
    if(potassium == None):
        potassium = 0.00001
    if(sodium == None):
        sodium = 0
    if(white == None):
        white = 0.00001 #log number
    if(urea == None):
        urea = 0.00001 #log numbers so can't be 0
    if(Sex == 'm'):
        sex = "Male"
    else:
        sex = "Female"
    if(Oxy == 'y'):
        oxy = 1
    else:
        oxy = 0
    currentCase = Case(age, sex, oxy, haemoglobin, potassium, sodium, white, urea)
    processed = processCase(currentCase)
    data = [[0,0,0],[0,1,processed]]
    return ['Custom Output {0:.4f}'.format(processed),
        {'data' :
            [go.Scatter(
                x=[0,1],
                y=[0,0],
                marker = {'symbol' : 'square', 'color' : 'blue'},
                showlegend = False
            ),
            go.Scatter(
                x=[0.5,0.5],
                y=[-0.5,0.5],
                marker = {'symbol' : 'square', 'color' : 'red'},
                showlegend = False
            ),
            go.Scatter(
                x=[processed],
                y=[0],
                marker = {'symbol' : 'cross', 'color' : 'grey', 'size' : 20},
                name = "Patient Probability",
                showlegend = False
            )
            ],
        'layout': go.Layout(
            xaxis={
                'title': "Probability", #TODO import from data package
                'zeroline': False
            },
            yaxis={
                'showgrid':False,
                'zeroline':False,
                'showline':False,
                'showticklabels':False
            },
            hovermode=False
        )}
        ]

@app.callback(Output('patientbox', 'children'), [Input('examples', 'value')])
def update_preset_div(example):
    if(example == "Patient 1"):
        currentCase = copy.deepcopy(healthyPatient)
    elif(example == "Patient 2"):
        currentCase = copy.deepcopy(sickPatient)
    return 'Example Patient Output {0:.4f}'.format(processCase(currentCase))

if __name__ == '__main__':
    currentCase = copy.deepcopy(healthyPatient)
    app.run_server(debug=True)
