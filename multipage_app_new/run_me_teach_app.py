#################
# App Description
'''
This page is the skeleton for the entire app, run this to start the app
The first page the user sees when you run this is app1
'''

################
#Imports/Set UP
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from apps import home_teach_app, vid, tool, logic, sepsis, sepsisModel

#################
# App Layout

app.layout = html.Div([
    dcc.Location(
        id='url', 
        refresh=False,
    ),
    html.Div(id='page-content')
])

################
# Callbacks

# Controls the page layout displayed based on the url pathname input
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')]
)

def display_page(pathname):
    if pathname ==  '/' or  pathname == None:
        return home_teach_app.layout
    elif pathname == '/apps/vid':
        return vid.layout
    elif pathname == '/apps/tool':
        return tool.layout
    elif pathname == '/apps/sepsis':
        return sepsis.layout
    elif pathname == '/apps/logic':
        return logic.layout
    elif pathname == '/apps/sepsisModel':
        return sepsisModel.layout
    return home_teach_app.layout

################
# Running

if __name__ == '__main__':
    app.run_server(debug=True)
