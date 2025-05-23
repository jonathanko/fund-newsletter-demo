import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
#from dash import Dash, dash_table

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
st.markdown("The Fund uses an equity long-short strategy. " \
"The firm was founded by investment professionals with decades of experience in capital markets.  " \
"The fund is focused on participating in the growth of the markets while protecting on the downside. " \
"The firm is both SFC licensed and SEC registered.")

#st.button("Contact Us", key="contact_us", help="Contact us for more information")

st.container(border=True, height=200).write("Contact Us")


df = pd.read_csv(r"returns.csv")

df

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


st.markdown("April markets were impacted by the repercussions of the U.S. trade policy as the tariffs announced in March finally took effect on April 2nd. " \
"Mid-month, facing concerns from businesses and negative market reactions, the Trump administration adjusted its stance, " \
"pausing escalations and resetting rates to a 10% baseline for many trading partners (excluding China) – a move generally perceived positively by markets. " \
"Later, Beijing signaled openness to negotiation, though the market struggled to assess these developments amid rapidly escalating tariffs between the two nations.")

st.markdown("As we issue this update, the negotiation landscape has become clearer. " \
"Following the May 6th announcement of upcoming discussions, U.S. Treasury Secretary Scott Bessent and Chinese Vice Premier He Lifeng " \
"met in Geneva over the weekend of May 12th and announced a significant agreement: a 90-day pause in the escalating tariff war. " \
"This interim agreement reduces U.S. tariffs on Chinese imports from recent peaks of 145% to a consolidated 30%, while China's retaliatory " \
"tariffs on U.S. goods drop from 125% to 10%. This window is intended to facilitate discussions toward a more comprehensive trade deal.")

st.markdown("We believe achieving a 'grand bargain' remains challenging. Structural imbalances persist on both sides – China's economy " \
"cannot transition to consumption-driven growth overnight, just as relocating complex manufacturing supply chains to the U.S. cannot be accomplished quickly. " \
"While markets expressed relief at the temporary truce, particularly given the rollback from exceptionally high tariff levels, the feasibility " \
"of a comprehensive long-term agreement remains uncertain.")

st.markdown("A key takeaway is the fundamental shift in the market's perception of U.S. policy risk. " \
"The risk premium associated with U.S. policy has increased. This uncertainty extends beyond financial markets. " \
"Many business leaders have discussed that this is making them more cautious on decision-making on supply chains, " \
"capital expenditures, hiring plans, and overall business strategies.")

st.markdown("In response to this evolving landscape, we've adjusted our portfolio accordingly. " \
"We've focused on identifying and investing in companies whose fundamental business drivers demonstrate strength " \
"and resilience, even in a challenging tariff environment marked by policy uncertainty. This approach was validated " \
"by several key Q1 earnings reports.")

st.markdown("Beyond the direct U.S.-China dynamic, we've also observed China adopting domestic policies " \
"geared toward countering U.S. trade pressures. China's policy response typically favors incremental stimulus measures" \
"rather than large-scale interventions. We expect this pattern to continue, though the cumulative effect of these " \
"incremental stimuli may eventually catalyze significant positive movement within the Chinese economy and markets.")

st.markdown("The portfolio today is positioned to capitalize on what we see as attractive valuations in certain segments of" \
" the Chinese market which is coupled with the shift we see in China toward a more pro-business and pragmatic policy orientation"
" in response to external pressures. While we've strategically taken profits on some positions, for the US to maintain leadership" \
" on AI, the long-term build out of critical infrastructure needs to happen. We also maintain positions in companies where the " \
"business and earnings outlook is robust and relatively less impacted by tariff uncertainties.")

