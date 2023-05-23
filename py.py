import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import plotly.graph_objects as go
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SBP Dashboard", page_icon=":bar_chart:", layout="wide")
# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard")
st.markdown("##")

# ---- READ EXCEL ----
df = pd.read_excel(
        io="Sample for Dashboard-Interns Session 4th Aug 2022.xlsx",
        engine="openpyxl",
        sheet_name="A",
        skiprows=0,
        usecols="A:R",
        nrows=1000,
    )
df2 = pd.read_excel(
        io="Sample for Dashboard-Interns Session 4th Aug 2022.xlsx",
        engine="openpyxl",
        sheet_name="B",
        skiprows=0,
        usecols="A:R",
        nrows=1000,
    )
df3 = pd.read_excel(
        io="Sample for Dashboard-Interns Session 4th Aug 2022.xlsx",
        engine="openpyxl",
        sheet_name="C",
        skiprows=0,
        usecols="A:R",
        nrows=1000,
    )  

df4 = pd.read_excel(
        io="Sample for Dashboard-Interns Session 4th Aug 2022.xlsx",
        engine="openpyxl",
        sheet_name="D",
        skiprows=0,
        usecols="A:R",
        nrows=1000,
    )

#st.dataframe(df)
#st.dataframe(df2)
#st.dataframe(df3)
#st.dataframe(df4)

# --- PLOT PIE CHART
pie_chartA = px.pie(df,
                title='Status of Team A',
                values='S.NO',
                names='Status')

#st.plotly_chart(pie_chartA)
pie_chartB = px.pie(df2,
                title='Status of Team B',
                values='S.NO',
                names='Status')

#st.plotly_chart(pie_chartB)
pie_chartC = px.pie(df3,
                title='Status of Team C',
                values='S.NO',
                names='Status')
pie_chartD = px.pie(df4,
                title='Status of Team D',
                values='S.NO',
                names='Status')
left_column, right_column,left_column2, right_column2 = st.columns(4)
left_column.plotly_chart(pie_chartA, use_container_width=True)
right_column.plotly_chart(pie_chartB, use_container_width=True)
left_column2.plotly_chart(pie_chartC, use_container_width=True)
right_column2.plotly_chart(pie_chartD, use_container_width=True)
#barchart 
slide=px.bar(df, y='severity', x='vulnerability_title' , title="<b>Team_A</b>",
      color_discrete_sequence=["#E8D943"],
      template="plotly_white",)
slide2=px.bar(df2, y='severity', x='vulnerability_title' , title="<b>Team_B</b>",
       color_discrete_sequence=["#E8D943"],
       template="plotly_white",)
slide3=px.bar(df3, y='severity', x='vulnerability_title' , title="<b>Team_C</b>",
       color_discrete_sequence=["#E8D943"],
       template="plotly_white",)
slide4=px.bar(df4, y='severity', x='vulnerability_title' , title="<b>Team_D</b>",
       color_discrete_sequence=["#E8D943"],
       template="plotly_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(slide, use_container_width=True)
right_column.plotly_chart(slide2, use_container_width=True)

left_column, right_column = st.columns(2)
left_column.plotly_chart(slide3, use_container_width=True)
right_column.plotly_chart(slide4, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
