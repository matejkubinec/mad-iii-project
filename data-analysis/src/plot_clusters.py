from load_labels import load_labels
from cleanup_dataset import cleanup_dataset
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import os

base_path = os.path.dirname(os.path.realpath(__file__))
data_path = f'{base_path}/data/deepsolar_tract.csv'
df = pd.read_csv(data_path)
state_col = [st.upper() for st in df['state']]

df.drop(['fips', 'county', 'state', 'voting_2012_dem_win',
         'voting_2016_dem_win'], axis=1, inplace=True)
df = df.select_dtypes(exclude=['object', 'bool'])
df = cleanup_dataset(df)
labels = load_labels()
indexes = list(df.iloc[:, 0])

states = dict([(st, {}) for st in set(state_col)])
st_val = list(state_col)
for i in range(len(indexes)):
    idx = indexes[i]

    if idx == 0.0:
        continue

    st = st_val[int(idx - 1)]
    cl = labels[i]

    if cl not in states[st]:
        states[st][cl] = 1
    else:
        states[st][cl] += 1

for st in states:
    max_cl = None

    for cl in states[st]:

        if max_cl is None or states[st][max_cl] < states[st][cl]:
            max_cl = cl

    states[st] = max_cl

locations = list(states.keys())
z = list(states.values())

fig = go.Figure(data=go.Choropleth(
    locations=locations,
    z=z,
    locationmode='USA-states',
    colorscale='Blackbody',
    colorbar_title="Cluster",
))

fig.update_layout(
    title_text='Clusters',
    geo_scope='usa',
)

# fig.show()
fig.write_image(f'{base_path}/images/clusters.jpg')
