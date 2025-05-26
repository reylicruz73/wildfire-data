import pandas as pd
import plotly.express as px

# Load the data
url = "/Users/reylicruz/PycharmProjects/wildfire-data/Rey's Data test/mapdataall (1).csv"
df = pd.read_csv(url)

# Convert date and extract year
df['incident_date_created'] = pd.to_datetime(df['incident_date_created'], errors='coerce')
df['year'] = df['incident_date_created'].dt.year

# Clean: remove rows with missing data
df = df.dropna(subset=['incident_latitude', 'incident_longitude', 'incident_acres_burned', 'year'])
df = df[df['incident_acres_burned'] > 0]

df['hover'] = (
    "🔥 " + df['incident_name'] +
    "<br>📍 " + df['incident_county'].fillna("Unknown") +
    "<br>🗓️ " + df['incident_date_created'].dt.strftime('%Y-%m-%d') +
    "<br>🌲 " + df['incident_acres_burned'].astype(int).astype(str) + " acres"
)

#  interactive map
fig = px.scatter_mapbox(
    df,
    lat='incident_latitude',
    lon='incident_longitude',
    size='incident_acres_burned',
    color='incident_acres_burned',
    color_continuous_scale='YlOrRd',
    size_max=25,
    zoom=5,
    mapbox_style='carto-positron',
    hover_name='incident_name',
    hover_data={'incident_acres_burned': True, 'incident_date_created': True, 'incident_county': True},
    custom_data=['hover'],
    animation_frame='year'  # 🎞️ adds year slider
)

fig.update_traces(
    hovertemplate="%{customdata[0]}<extra></extra>"
)

fig.update_layout(
    title='🔥 Interactive Wildfire Map of California by Year',
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    coloraxis_colorbar=dict(title="Acres Burned"),
    updatemenus=[
        dict(
            buttons=[
                dict(label="All Years", method="animate", args=[None]),
                *[
                    dict(
                        label=str(year),
                        method="animate",
                        args=[[str(year)], dict(frame=dict(duration=500, redraw=True), mode="immediate")]
                    )
                    for year in sorted(df['year'].dropna().unique())
                ]
            ],
            direction="down",
            showactive=True,
            x=0.05,
            xanchor="left",
            y=1.15,
            yanchor="top"
        )
    ]
)

fig.show()
