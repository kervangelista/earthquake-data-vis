import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'dv_plotly/significant_month.json'
with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

title_name = all_eq_data["metadata"]["title"]
my_layout = Layout(title=title_name)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake_30.html')
