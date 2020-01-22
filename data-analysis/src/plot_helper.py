from sklearn import preprocessing
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import os


def plot_us_map(locations, z, colorscale, colorbar_title, title_text, filename=None):
    fig = go.Figure(data=go.Choropleth(
        locations=locations,
        z=z,
        locationmode='USA-states',
        colorscale=colorscale,
        colorbar_title=colorbar_title,
    ))
    fig.update_layout(
        title_text=title_text,
        geo_scope='usa',
    )
    write_or_show_fig(fig, filename)


def plot_fips(fips, values, colorbar_title, title_text, filename=None):
    fig = ff.create_choropleth(
        fips=fips,
        values=values
    )
    fig.update_layout(
        title_text=title_text,
        geo_scope='usa',
    )
    write_or_show_fig(fig, filename)


def plot_hist(data_frame, nbins, x, labels, filename=None):
    fig = px.histogram(data_frame, x=x, nbins=nbins, labels=labels, )
    write_or_show_fig(fig, filename)


def plot_box_plot(df, y, labels, filename=None):
    fig = px.box(df, y=y, labels=labels)
    write_or_show_fig(fig, filename)


def plot_multiple_box_plots(boxes, filename=None):
    fig = go.Figure()
    for box in boxes:
        fig.add_trace(go.Box(
            y=box['y'],
            x=box['x'],
            name=box['name'],
        ))

    write_or_show_fig(fig, filename)


def plot_line(df, x, y, title, filename=None):
    fig = px.line(df, x=x, y=y, title=title)
    write_or_show_fig(fig, filename)

def plot_bar(df, x, y, title, color, filename=None):
    fig = go.Figure(data=[go.Bar(
        x=df[x],
        y=df[y],
        
        marker={
            'color': df[x],
            'colorscale': 'Viridis'
        }
        )],
        layout=go.Layout(
            title=title,
        )
    )
    write_or_show_fig(fig, filename)

def write_or_show_fig(fig, filename):
    base_path = os.path.dirname(os.path.realpath(__file__))
    if filename is None:
        fig.show()
    else:
        fig.write_image(f'{base_path}/images/{filename}.jpg')
