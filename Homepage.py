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

st.sidebar.image("logo.png", width=500)
st.sidebar.title("Table of Contents")
st.sidebar.markdown("[Overview](#overview)")
st.sidebar.markdown("[Strategy Description](#strategy-description)")
st.sidebar.markdown("[Portfolio Performance](#portfolio-performance)")
st.sidebar.markdown("[Market Commentary](#market-commentary)")
st.sidebar.markdown("[Risk & Returns](#risk-and-returns)")
st.sidebar.markdown("[Portfolio Exposure](#portfolio-exposure)")
st.sidebar.markdown("[Terms of the Fund](#terms-of-the-fund)")
st.sidebar.markdown("[Contact Details](#contact-details)")
st.sidebar.markdown("[Disclaimer](#disclaimer)")

st.title("Monthly Update | Fund April 2025")

#st.button("Contact Us", key="contact_us", help="Contact us for more information")



col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios


with col1:
    st.header("Overview")
    col1a, col1b = st.columns(2)
    col1a, col1b = st.columns([1, 3])  #column widths ratios
    with col1a:
        st.markdown("Bloomberg Ticker:")
        st.markdown("Prime Brokers:")
        st.markdown("Fund Administrator:")
        st.markdown("Auditor:")
        st.markdown("Regulatory:")
        st.markdown("Inception Date:")
    with col1b:
        st.markdown("TELLGNT KY Equity")
        st.markdown("Goldman Sachs & J.P. Morgan")
        st.markdown("State Street")
        st.markdown("Ernst & Young")
        st.markdown("US SEC registered and Hong Kong SFC licensed")
        st.markdown("August 1, 2004")

with col2:
    st.header("Strategy Description")
    with open("description.txt", "r", encoding="utf-8") as file:
        text = file.read()
    st.markdown(text)

st.markdown(" ")
st.markdown(" ")

st.header("Portfolio Performance")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    st.subheader("Quick Update")
    flourish_iframe = """
    <div class="flourish-embed flourish-table" data-src="visualisation/23411515"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/23411515/thumbnail" width="100%" alt="table visualization" /></noscript></div>
    """
    components.html(flourish_iframe, height=190)

with col2:
    st.subheader("Contribution Breakdown")
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23434228/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23434228/?utm_source=embed&utm_campaign=visualisation/23434228' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=190)

st.subheader("Growth of $100 Since Inception")

df = pd.read_csv(r"data.csv")
                
df = df.set_index('Month')

fig = px.line(df, labels={'varible':''})

fig = fig.update_layout(
    title='',
    template='plotly_white',
    plot_bgcolor='white',   # Background inside the plotting area
    paper_bgcolor='white',       # Background of the entire figure
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis_title="Time Period",
    yaxis_title="Performance",
    height=500,
    width=2000,
    )


fig.update_xaxes(tick0=5, dtick=12)

#x_vals = fig.data[0].x  # assuming first trace's x-values
#tickvals = x_vals[::12]  # every 5th value
#ticktext = [str(val) for val in tickvals]
#fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)


fig.data[0].line.color = 'rgb(0,128,0)'
fig.data[1].line.color = 'rgb(211,211,211)'  # Grey color for the index line

fig

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

st.header("Risk & Returns")
st.markdown("Risk-free rate = 3 month T-Bill")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23412618/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:200px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23412618/?utm_source=embed&utm_campaign=visualisation/23412618' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=195)

with col2:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23412923/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:200px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23412923/?utm_source=embed&utm_campaign=visualisation/23412923' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=195)

st.markdown(" ")
st.markdown(" ")

st.header("Portfolio Exposure")

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

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 1])  #column widths ratios

with col1:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23433368/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23433368/?utm_source=embed&utm_campaign=visualisation/23433368' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>    
    """
    components.html(flourish_iframe, height=580)

with col2:
    flourish_iframe = """
    <iframe src='https://flo.uri.sh/visualisation/23433406/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/23433406/?utm_source=embed&utm_campaign=visualisation/23433406' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    """
    components.html(flourish_iframe, height=580)

st.markdown(" ")
st.header("Terms of the Fund")

col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 5])  #column widths ratios

with col1:
    st.markdown("Legal Structure:")
    st.markdown("Initial Allocation:")
    st.markdown("Fee Structure:")
    st.markdown("High-water Mark Protection:")
    st.markdown("Subscription Fee:")
    st.markdown("Withdrawal Fee:")
    st.markdown("Withdrawal Notice Period:")
    st.markdown("Liquidity:")

with col2:
    st.markdown("Master Feeder, Cayman Ltd and Delaware LP")
    st.markdown("USD 1 million")
    st.markdown("1.5% / 20%")
    st.markdown("Yes, applies to all investors")
    st.markdown("None")
    st.markdown("None")
    st.markdown("30 days")
    st.markdown("Monthly")
    
st.markdown(" ")
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

