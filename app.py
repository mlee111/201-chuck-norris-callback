######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['Pick your meal', 'McDouble', 'McRib', 'McNuggets', 'McChicken']
githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
image1='download.jpg'
list_of_images=['download.jpg', 'double.jpeg', 'rib.jpeg', 'nuggies.jpeg', 'chicken.jpeg']
heading1='McDonald\'s menu'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Mickey D\'s'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='image-output'),
    dcc.Dropdown(id='your-input-here',
                options=[{'value': list_of_images[i], 'label': list_of_choices[i]} for i in range(0, 5)],
                value='Pick your meal',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    if (whatever_you_chose != 'Pick your meal'):
        return f'You have ordered a {whatever_you_chose}.'
    else:
        return 'Pick a menu item'

@app.callback(dash.dependencies.Output('image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'label')])
def display_value(whatever_you_chose):
    return whatever_you_chose


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
