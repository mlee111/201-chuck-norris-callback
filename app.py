######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['Pick your meal', 'McDouble', 'McRib', 'McNuggets', 'McChicken']
githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
list_of_images=['download.png', 'double.jpeg', 'rib.jpeg', 'nuggies.jpeg', 'chicken.jpeg']
heading1='McDonald\'s menu'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Mickey D\'s'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='image-output', src=app.get_asset_url('download.png')),
    dcc.Dropdown(id='your-input-here',
                options=[{'value': i, 'label': list_of_choices[i]} for i in range(0, 5)],
                value=list_of_choices[0],
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
    if (whatever_you_chose != 0):
        return f'You have ordered a {list_of_choices[whatever_you_chose]}.'
    else:
        return 'Pick a menu item'

@app.callback(dash.dependencies.Output('image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
