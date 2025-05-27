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
    st.header("Overview")
    with open("description.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

with col2:
    st.markdown(" ")
    with open("terms.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <div class="flourish-embed flourish-table" data-src="visualisation/23411515"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23411515/thumbnail" width="100%" alt="table visualization" /></noscript></div>
    """
    components.html(flourish_iframe, height=230)

with col2:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23434228/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23434228/?utm_source=embed&utm_campaign=visualisation/23434228' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=230)


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
line.data[1].line.color = 'rgb(211,211,211)'  # Grey color for the index line

line

st.markdown(" ")

st.header("Risk & Returns")
st.markdown("Risk-free rate = 3 month T-Bill")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23412618"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23412618/thumbnail" width="100%" alt="chart visualization" /></noscript></div>    
    """
    components.html(flourish_iframe, height=195)

with col2:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23412923"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23412923/thumbnail" width="100%" alt="chart visualization" /></noscript></div>    
    """
    components.html(flourish_iframe, height=195)

st.markdown(" ")

st.header("Market Commentary")

col1, col2 = st.columns(2)
col1, col2 = st.columns([2, 1])  #column widths ratios

with col1:
    with open("commentary.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

with col2:
    st.markdown(" ")

st.markdown(" ")

st.header("Exposure")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23433880/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23433880/?utm_source=embed&utm_campaign=visualisation/23433880' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=580)

with col2:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23436330/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23436330/?utm_source=embed&utm_campaign=visualisation/23436330' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=580)

st.markdown(" ")

st.header("Gross Exposure")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23433368"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23433368/thumbnail" width="100%" alt="chart visualization" /></noscript></div>
    """
    components.html(flourish_iframe, height=580)

with col2:
    flourish_iframe = """
    <div class="flourish-embed flourish-chart" data-src="visualisation/23433406"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23433406/thumbnail" width="100%" alt="chart visualization" /></noscript></div>
    """
    components.html(flourish_iframe, height=580)

st.markdown("---")

st.header("Terms of the Fund")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 10])  #column widths ratios

with col1:
    st.markdown("Structure")
    st.markdown("Initial Allocation")
    st.markdown("Fees")
    st.markdown("Prime Brokers")
    st.markdown("Auditor")
    st.markdown("Regulatory")
with col2:
    st.markdown("Master Feeder, Cayman Ltd and Delaware LP")
    st.markdown("USD 1 million")
    st.markdown("1.5% / 20%")
    st.markdown("Goldman Sachs and J.P. Morgan")
    st.markdown("Ernst & Young")
    st.markdown("US SEC registered and Hong Kong SFC licensed")

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

