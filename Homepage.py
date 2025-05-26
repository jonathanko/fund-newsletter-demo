import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
#from dash import Dash, dash_table
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Demo | Monthly Newsletter",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "https://www.telligentcapital.com",
    }
)

st.sidebar.title("Table of Contents")

st.title("Monthly Update | Fund April 2025")



#st.button("Contact Us", key="contact_us", help="Contact us for more information")



col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    st.markdown(" ")
    with open("description.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

with col2:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23411515/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23411515/?utm_source=embed&utm_campaign=visualisation/23411515' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>    
    """
    components.html(flourish_iframe, height=250)


st.header("Risk & Returns")
st.markdown("Risk-free rate = 3 month T-Bill")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23412618"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23412618/thumbnail" width="100%" alt="chart visualization" /></noscript></div>    
    """
    components.html(flourish_iframe, height=300)

with col2:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23412923"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23412923/thumbnail" width="100%" alt="chart visualization" /></noscript></div>    
    """
    components.html(flourish_iframe, height=300)


st.header("Market Commentary")

col1, col2 = st.columns(2)
col1, col2 = st.columns([2, 1])  #column widths ratios

with col1:
    with open("commentary.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

with col2:
    st.markdown(" ")

st.markdown("---")



st.header("Contact Details")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 2.5])  #column widths ratios

with col1:
    st.markdown("Telligent Capital Management Ltd")
    st.markdown("Address: 1603-05, Lippo Centre Tower 2, 89 Queensway, Admiralty, Hong Kong")
    st.markdown("Tel: +852 3150 0888")
    st.markdown("Email: investor@tellcap.com")
    st.markdown("Website: www.tellcap.com")
with col2:
    st.markdown("John Lin, Managing Director <john@tellcap.com>")
    st.markdown("George Lin, Chief Executive Officer <george@tellcap.com>")

st.markdown("---")

st.header("Disclaimer")

with open("disclaimer.txt", "r", encoding="utf-8") as file:
    text = file.read()

st.markdown(text)


#save for further use
st.markdown("---")

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


df = pd.read_csv(r"returns.csv")

df

st.container(border=True, height=200).write("Contact Us")