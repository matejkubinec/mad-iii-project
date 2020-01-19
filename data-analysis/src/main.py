import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os


def plot_states(states, z):
    fig = go.Figure(data=go.Choropleth(
        locations=states,
        z=z,  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Millions USD",
    ))

    fig.update_layout(
        title_text='2011 US Agriculture Exports by State',
        geo_scope='usa',  # limite map scope to USA
    )

    fig.show()
    # fig.write_image('map.png')


def plot_counties(fips, values):
    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['usa'],
        show_state_data=False,
        show_hover=True,
        asp=2.9,
        title_text='USA by Unemployment %',
        legend_title='% unemployed'
    )

    fig.layout.template = None
    fig.show()


def main():
    base_path = os.path.dirname(os.path.realpath(__file__))
    data_path = f'{base_path}/data/deepsolar_tract.csv'
    df = pd.read_csv(data_path)

    states_df = df['state']
    solar_panels_count_df = df['solar_system_count']

    state_dict = {}

    for i in range(len(states_df)):
        state = states_df[i]
        count = solar_panels_count_df[i]

        if state not in state_dict:
            state_dict[state] = 0
        else:
            state_dict[state] += count

    states = [st.upper() for st in state_dict.keys()]
    states_solar = list(state_dict.values())

    # plot_states(states, states_solar)

    df.groupby(['fips'])



    pass


if __name__ == "__main__":
    main()
