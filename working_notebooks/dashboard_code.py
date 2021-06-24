import json
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv("/Users/kevinmcdonough/Documents/Flatiron/phase_3/phase_3_project/phase_3_project/data/dash_df.csv", index_col=0)


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Tanzanian Water Wells", style={'text-align': 'center'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(id="slct_cat",
                        options=[
                            {"label": "Basin", "value": "basin"},
                            {"label": "Public Meeting", "value": "public_meeting"},
                            {"label": "Payment", "value": "payment"},
                            {"label": "Water Quality", "value": "water_quality"},
                            {"label": "Source Class", "value": "source_class"},
                            {"label": "Binned Age", "value": "bin_age"},
                            {"label": "Quantity", "value": "quantity"},
                            {"label": "Installer", "value": "installer"}],
                        multi=False,
                        value="basin", 
                        style={'width': "85%", 'padding-left': '15%'}
                        ),

            html.Div(id='output_container', children=[]),
            html.Br(),
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(id="slct_num",
                        options=[
                            {"label": "Age", "value": "age"},
                            {"label": "Latitude", "value": "latitude"},
                            {"label": "Longitude", "value": "longitude"}],
                        multi=False,
                        value="age",
                        style={'width': "85%", 'padding-left': '15%'}
                        ),
            html.Br(),
        ], style={'width': '49%', 'text-align': 'center', 'display': 'inline-block'})
    ]),
    html.Div([
    dcc.Graph(id='my_cat_chart'),
    ], style={'width': '49%', 'display': 'inline-block', 'height': '80vh'}),
    html.Div([
    dcc.Graph(id='my_num_chart'),
    ], style={'display': 'inline-block', 'width': '49%', 'height': '80vh'}),
])

# # ------------------------------------------------------------------------------
# # Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='my_cat_chart', component_property='figure'),
    [Input(component_id='slct_cat', component_property='value')]
)

def create_chart(slct_cat):
    
    dff = df.copy()
    dff['count'] = dff.groupby('region')['longitude'].transform(lambda grp: len(grp))
    dff = dff.groupby(slct_cat).mean().reset_index()
    dff.sort_values(by='functional', ascending=True, inplace=True) 

    def update_length(dff):
        if len(dff) > 20:
            dff.sort_values(by='installer_count', ascending=False, inplace=True)
            dff = dff[0:30]
        else: 
            dff = dff.copy()
        return dff
     
    dff = update_length(dff)
    
    fig = px.bar(dff, y=slct_cat, x=['functional', 'non_functional', 'fnr'], orientation='h')
    fig.update_layout(title_text=slct_cat + " Status Group % Breakdown", height=750, title_x=0.5, xaxis_title="Percentage")
    
    return fig 

@app.callback(
    Output(component_id='my_num_chart', component_property='figure'),
    [Input(component_id='slct_num', component_property='value')]
)

def create_num_chart(slct_num):
    
    def clean_df(df, slct_num):
        if slct_num == "age":
            df_new = df[df[slct_num] < 2000]
        elif slct_num == "longitude":
            df_new = df[df[slct_num] > 0]
        else:
            df_new = df.copy()
        return df_new
    
    df_new = clean_df(df, slct_num)
    

    fig = px.box(df_new, y=slct_num, x=['status_group'])
    fig.update_layout(title_text="Status Group by " + slct_num, height=750, title_x=0.5)
    
    return fig 
# @app.callback(
#     Output(component_id='my_bar_chart', component_property='figure'),
#     [Input(component_id='my_ufo_map', component_property='hoverData'),
#     Input(component_id='slct_chart', component_property='value')]
# )

# def update_chart(hoverData, slct_chart):
#     state_name = hoverData['points'][0]['customdata'][0]
#     df_new = df.copy()
#     df_new = df_new[df_new['state'] == state_name]
#     print(state_name)
#     return create_chart(df_new, slct_chart, hoverData)

# @app.callback(
# Output('my-hoverdata', 'children'),
# [Input('my_ufo_map', 'hoverData')])

# def callback_image(hoverData):
#     return json.dumps(hoverData, indent=2)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)