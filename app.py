import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import plotly.express as px
import time

st.set_page_config(
    page_icon='💊',
    page_title='AERS',
    layout='wide'
)

# for the connecting with mysql
@st.cache_resource
def get_engine():
    return create_engine('mysql+pymysql://root:1771@localhost/pharma_safety')

# used to fetch data from signals ranked
@st.cache_data(ttl = 300,show_spinner=False)
def load_signals():
    conn = get_engine()
    return pd.read_sql("""SELECT * FROM signals_ranked""",conn)

# it is for abalyst_decision table
@st.cache_data(ttl=60,show_spinner=False)
def load_decisions():
    conn = get_engine()
    return pd.read_sql("""SELECT * FROM analyst_decision""" , conn)

with st.sidebar:
    st.header('Adeversal Event Ranking System')
    st.markdown('---')
    page = st.radio('Navigate' , options=['📊Signal ranker' , '🔍Signal details' , '📈Dashboard overview' , '🕒Decision History'])



if page == '📊Signal ranker':
    st.header('📊Signal ranker')
    st.markdown('---')
    df = load_signals()
    # st.dataframe(df)

    # metric cards
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Total Signals" , df.shape[0])

    with col2:
         df1 =df[df['final_score'] == df['final_score'].max()]
         top_drug = df1.iloc[0,0]
        #  st.dataframe(df1)
         st.metric("Top Drug" , top_drug)

    with col3:
        st.metric("Top Drug Severity Score" , df['final_score'].max())

    with col4:
         df1 =df[df['final_score'] == df['final_score'].max()]
         top_drug = df1.iloc[0,0]
         top_rection = df.iloc[0,1]
         st.metric("Top Drug - Reaction Pair",top_drug + " - " +top_rection)

    st.markdown('---')
    # top signals . Value >= 8
    st.subheader("Top Signals")
    df = df[df['final_score'] >= 8]
    df = df[['drugname','reaction','final_score']]
    st.dataframe(df)

    st.markdown('---')
    st.subheader('Filters')

    # taking input
    st.warning("Before search for the Drug name and Reaction name , Make sure you enter correct name (spelling) ")
    drug_name = st.text_input('Drug search :  ',placeholder='Enter the Drug name')
    max_score = st.slider("Select the final score" , 0.0 , 10.0 , 5.0,step=0.01)
    reaction_name = st.text_input("Reaction Search : " , placeholder='Enter the reaction name')


    df = load_signals()

    #filtering dataframe
    filtered_df = df[
    df['drugname'].str.contains(drug_name, case=False, na=False) &
    df['reaction'].str.contains(reaction_name, case=False, na=False) &
    (df['final_score'] >= max_score)
    ]

    # appluting color palatte
    # def row_color(row):
    #     if row['final_score'] >= 8:
    #         return ['background-color: red; color: white'] * len(row)
    #     elif row['final_score'] >= 6:
    #         return ['background-color: orange; color: white'] * len(row)
    #     else:
    #         return ['background-color: green; color: white'] * len(row)
    
    # styled_df = filtered_df.style.apply(row_color, axis=1)
    # st.dataframe(styled_df, use_container_width=True)
    
    # shoeing dataframe and rpoviding download button
    st.write("Filtered dataframe")
    st.dataframe(filtered_df)
    data = filtered_df.to_csv(index=False).encode('utf-8')

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.download_button(" ⬇️ Download Filtered Data"  , file_name='Filtered_dataframe.csv', data = data)

    with col2 : 
        st.metric("Total signals : " , filtered_df.shape[0])

    with col3:
        last_updated = str(df.iloc[0,8])
        st.metric("Last date Updated" , last_updated)

elif page == '🔍Signal details':
    st.header('🔍Signal details')
    st.markdown('---')

    # showing dataframe for selected drug and reaction 
    df = load_signals()
    drug_name = st.selectbox("Select the Drug : ", df['drugname'].unique())
    df = df[df['drugname'] == drug_name]
    reaction_name = st.selectbox(f"Select the Reaction for {drug_name} : ", df['reaction'].unique())
    df = df[df['reaction'] == reaction_name]
    st.markdown('---')

    # Extract single values using iloc[0]
    row = df.iloc[0]

    row_df = pd.DataFrame({
        'Parameters' : row.index ,
        'values' : row.values
    }  
    )
    st.subheader("Info about Drug and Reaction Pair")
    st.dataframe(row_df)

    # Build score breakdown DataFrame
    score_df = pd.DataFrame({
        'Score': ['Novelty', 'Severity', 'Population'],
        'Value': [row['novelty_score'], row['severity_score'], row['population_score']]
    })
    st.markdown('---')

    # Plot bar chart
    fig = px.bar(
        score_df,
        x='Score',
        y='Value',
        color='Score',
        title=f'Score breakdown — {drug_name} + {reaction_name}',
        range_y=[0, 10],
        text='Value'
    )

    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('---')

    # signal details
    from sqlalchemy import text
    from datetime import datetime

    st.header('Analyst Action section')
    note = st.text_area("Enter the Note" , placeholder='Enter the Note')
    engine = get_engine()

    col1 , col2 , col3 = st.columns(3)

    with col1 :
        if st.button("Confirm Signal"):
            with engine.connect() as conn:
                conn.execute(

                text(
                """ INSERT INTO analyst_decision
                (drug_name , reaction , decision , analyst_note , decided_at)
                VALUES
                (:drug , :reaction , :decision , :note , :ts)
                    """),

                 {
                     'drug' : row['drugname'] , 
                     'reaction' : row['reaction'] ,
                     'decision' : 'Confirmed',
                     'note' : note ,
                     'ts' : datetime.now()
                 } 
                )
                conn.commit()

            st.success("Siganl Confirmed and Saved")
            load_decisions.clear()
            time.sleep(5)
            st.rerun()

    with col2 :
        if st.button("Dismiss Signal"):
            with engine.connect() as conn:
                conn.execute(

                text(
                """ INSERT INTO analyst_decision
                (drug_name , reaction , decision , analyst_note , decided_at)
                VALUES
                (:drug , :reaction , :decision , :note , :ts)
                    """),

                 {
                     'drug' : row['drugname'] , 
                     'reaction' : row['reaction'] ,
                     'decision' : 'Dismissed',
                     'note' : note ,
                     'ts' : datetime.now()
                 }  
                )
                conn.commit()

            st.warning("Siganl Dismissed and Saved")
            load_decisions.clear()
            time.sleep(5)
            st.rerun()

    with col3:
        if st.button("Escalte to Medical Officer"):
            with engine.connect() as conn:
                conn.execute(

                text(
                """ INSERT INTO analyst_decision
                (drug_name , reaction , decision , analyst_note , decided_at)
                VALUES
                (:drug , :reaction , :decision , :note , :ts)
                    """),

                 {
                     'drug' : row['drugname'] , 
                     'reaction' : row['reaction'] ,
                     'decision' : 'Escalated',
                     'note' : note ,
                     'ts' : datetime.now()
                 }  

                )
                conn.commit()
            st.error("Escalte to Medical Officer")
            load_decisions.clear()
            time.sleep(5)
            st.rerun()


elif page == '📈Dashboard overview':
    st.header('📈Dashboard overview')
    st.markdown('---')

    # displaying decision and signal dataframe
    signal = load_signals()
    decision = load_decisions()

    # st.subheader("Signals")
    # st.dataframe(signal)
    # st.markdown('---')

    # st.subheader("Decisions")
    # st.dataframe(decision)
    # st.markdown('---')

    # metric cards
    col1 , col2 , col3 , col4 = st.columns(4)

    with col1:
        len_signal = len(signal)
        st.metric("Total Signals" , len_signal)

    with col2:
        urgent_signals = signal[signal['final_score'] >= 8]
        st.metric("Urgent Signals" ,len(urgent_signals) )
        
    with col3:
        len_decision = len(decision)
        st.metric("Total Decisions Made" , len_decision)
        

    with col4:
        confirmed_decisions = decision[decision['decision'] == 'Confirmed']
        st.metric("Confirmed Decisions" , len(confirmed_decisions))

    st.markdown('---')

    # charts

    col1 , col2 = st.columns(2)

    with col1 :
        df = decision.groupby('decision')['decision'].count().reset_index(name = 'Decision_count')

        if(len(decision) != 0):
            fig = px.pie(df , values='Decision_count' , names='decision' , title='Decision breakdown pie chart')
            st.plotly_chart(fig)
        else:
            st.info("No Decision made Yet !")

    with col2 :
        df = signal.groupby('drugname')['final_score'].max().reset_index(name='Most_dangerous').sort_values('Most_dangerous' , ascending=False).head(10)
  
        fig = px.bar(df , x = 'drugname' , y = 'Most_dangerous' , title=' Top 10 drugs bar chart' , color_continuous_scale='Reds')   
        st.plotly_chart(fig)

    st.markdown('---')

    # full chart
    df = load_signals()
    bins = [0,2,4,6,8,10]
    df['score_range'] = pd.cut(df['final_score'] , bins = bins).astype('str')

    dist = df['score_range'].value_counts().sort_index()
    dist = dist.reset_index(name = 'No_of_Signals')
    st.subheader('Score distribution DataFrame')
    st.dataframe(dist)

    fig = px.bar(dist , x = 'score_range' , y = 'No_of_Signals' , title = 'Score distribution chart')
    st.plotly_chart(fig)

    st.markdown('---')

    # last 5 decision chart

    df = load_decisions()
    temp_df = df.sort_values('decided_at',ascending=False).head(5)
    st.subheader('Recent decisions table')
    st.dataframe(temp_df)


elif page == '🕒Decision History':
    st.header('🕒Decision History')
    st.markdown('---')

    df = load_decisions()
    if len(df) == 0:
        st.info("No decisions are made yet , Go to Signal Detail page and Review Signal")
        st.stop()

    # Summary metrics at the top
    col1 , col2 , col3 , col4 = st.columns(4)

    with col1:
        st.metric("Total Decicions" , len(df))

    with col2 :
        temp_df = df[df['decision'] == 'Confirmed']
        st.metric("Confirmed Decicions" , len(temp_df))

    with col3 :
        temp_df = df[df['decision'] == 'Dismissed']
        st.metric("Dismissed Decicions" , len(temp_df))

    with col4 :
        temp_df = df[df['decision'] == 'Escalated']
        st.metric("Escalated Decicions" , len(temp_df))
    st.markdown('---')

    # Filters
    st.subheader('Filters')
    df = load_decisions()

    selct = st.multiselect("Select The Decicion Type" , options=df['decision'].unique() , default = df['decision'].unique())
    filtered_df = df[df['decision'].isin(selct)]
    st.dataframe(filtered_df)

    name = st.selectbox("Enter the Drug Name" , options=df['drug_name'].unique() )
    filtered_df = filtered_df[filtered_df['drug_name'] == name]
    st.dataframe(filtered_df)
    st.markdown('---')


    # The full decision Table
    temp_df = df
    temp_df.rename(columns={'drug_name' : 'Drug Name' , 'reaction' : 'Reaction' , 'decision' : 'Decision' , 'analyst_note': 'Analyst Note' , 'decided_at' : 'Time and Date'} , inplace=True)
    st.subheader('Full Decision Table')
    st.dataframe(temp_df)
    

    #Download the DataFrame
    col1 , col2 = st.columns(2)

    with col1:
        df = load_decisions()
        data = df.to_csv(index=False)
        st.download_button('Download Entire Data' , file_name='Analyst Decicsion .csv' , data = data)

    with col2:
        data = filtered_df.to_csv(index=False)
        st.download_button('Download Filtered Data' , file_name='Filtered data .csv' , data = data)





    





