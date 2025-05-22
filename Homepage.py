import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


st.set_page_config(
    page_title="Demo | Telligent Fund Monthly Newsletter",
    page_icon="👋",
)

st.title("Monthly Update | April 2025")
st.text("The Telligent Fund uses an equity long-short strategy. The firm was founded by investment professionals with decades of experience in capital markets.  The fund is focused on participating in the growth of the markets while protecting on the downside. The firm is both SFC licensed and SEC registered.")

st.header("Performance Data")

with st.sidebar:
    st.markdown("Performance Line Chart")

df = pd.read_csv(r"data.csv")
                
df = df.set_index('Date')

line = px.line(df, labels={'varible':''})

line = line.update_layout(
    title='',
    template='plotly_white',
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis_title="Date",
    yaxis_title="Performance",
    height=500,
    width=2000,
    )

line.data[0].line.color = 'rgb(0,128,0)'
line.data[1].line.color = 'orange'
line.data[2].line.color = 'grey'

line

st.header("Performance Summary")

df = pd.read_csv(r"returns.csv")

fig = go.Figure(data=[go.Table(
    columnwidth=[1, 1, 1],
    header=dict(
        values=list(df.columns),
        fill_color='rgb(0,128,0)',
        font=dict(color='white', size=12),
        align='center'
        ),
    cells=dict(
        values=[df[col].tolist() for col in df.columns],
        fill_color='rgb(248,246,240)',
        align='center'
        )
    )])

fig.update_layout(width=250)

st.plotly_chart(fig, use_container_width=True)

st.header("Risk Ratios")

df = pd.read_csv(r"risk_ratios.csv")

color_map = {
    'Telligent': 'rgb(0,128,0)',
    'Index': 'grey',
}

fig = px.bar(
    df,
    x='Metrics',
    y='Values',
    color='Products',
    barmode='group',
    labels={'Products':''},
    color_discrete_map=color_map
)

fig.update_layout(
    title='',
    xaxis_title="",
    yaxis_title="",
    bargap=0.5,
    width=380,
)

st.plotly_chart(fig, use_container_width=True)
