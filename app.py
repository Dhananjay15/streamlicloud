import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('./analysis.csv')

#############################
#preprocess
loc_rate = df['rate'].groupby(df['location'],sort=True)
d={}
for i,j in df['location'].value_counts()[:10].to_dict().items():
    d[i]=round(loc_rate.get_group(i).mean(),2)
loc_rate = pd.DataFrame(list(d.items()),columns=['location',"avg_rating"])


type_rate = df['rate'].groupby(df['listed_in(type)'],sort=True)
d={}
for i,j in df['listed_in(type)'].value_counts()[:10].to_dict().items():
    d[i]=round(type_rate.get_group(i).mean(),2)
type_rate = pd.DataFrame(list(d.items()),columns=['Type',"avg_rating"])


restaurants_cost = df['approx_cost_for_two'].groupby(df['name'],sort=True)
d={}
for i,j in df['name'].value_counts()[:10].to_dict().items():
    d[i]=round(restaurants_cost.get_group(i).mean(),2)
new = pd.DataFrame(list(d.items()),columns=['name',"avg_cost"])
##############################

st.sidebar.title("Zomato Analysis")
st.sidebar.image('./image_side.jpg')
user_menu = st.sidebar.radio(
    'Select a Query',
    ('Home','Restaurants delivering Online or not','Restaurants allowing table booking or not',
     'Relation between Location and Rating','Restaurant Type','Relation between Type and Rating',
     'Top 10 most famous restaurant chains','Cost for 2 people','No. of restaurants in a Location')
)

if user_menu == 'Home':    
    st.title("Zomato analysis of Banglore based restaurants")
    st.text('This dataset is a collection of restaurants that are registered on Zomato.')
    st.text('In this dataset, we have more than 50000 rows and 17 columns, a fairly large dataset.')
    st.text('The original Dataset is sourced from Kaggle.')
    st.caption('https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset?datasetId=2755701&sortBy=voteCount')
    st.text('For analysis purpose dataset is preprocessed accordingly')
    st.dataframe(df.head(10))

if user_menu == 'Restaurants delivering Online or not':    
    st.title("Restaurants delivering Online or not")
    final = df['online_order'].value_counts()
    fig = px.pie(df,values=final,names=["YES","NO"], title='Restaurants delivering Online or not',labels=['YES','NO'],color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
    

if user_menu == 'Restaurants allowing table booking or not':    
    st.title("Restaurants allowing table booking or not")
    final = df['book_table'].value_counts()
    fig = px.pie(df,values=final,names=["NO","YES"], title='Restaurants allowing table booking or not',labels=['YES','NO'],color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)    
    
if user_menu == "Relation between Location and Rating":
    st.title("Relation between Location and Rating")
    final = loc_rate.sort_values(by=['avg_rating'],ascending=False)
    fig = px.bar(final, x="avg_rating",y="location" ,color="location",text='avg_rating',title="Top 10 locations average ratings")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)

if user_menu == "Restaurant Type":
    st.title("Restaurant Type")
    final = df['rest_type'].value_counts().head(10).rename_axis('Restaurants').reset_index(name='Counts')
    fig = px.bar(final, x="Counts",y='Restaurants',color="Restaurants",text='Counts',title="Top 10 Restaurant Types")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
    
if user_menu == "Relation between Type and Rating":
    st.title("Relation between Type and Rating")
    final = type_rate.sort_values(by=['avg_rating'],ascending=False)
    fig = px.bar(final, x="avg_rating",y='Type',color="Type",text='avg_rating',title="Restaurant Type average ratings")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
    
    
if user_menu == "Top 10 most famous restaurant chains":
    st.title("Top 10 most famous restaurant chains")
    final = df['name'].value_counts().head(10).rename_axis('Restaurants').reset_index(name='Counts')
    fig = px.bar(final, x='Counts',y='Restaurants',color="Restaurants",text='Counts',title="Top 10 most famous restaurant chains")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
    
if user_menu == "Cost for 2 people":
    st.title("Top 10 Restaurants average cost for 2 people")
    final = new.sort_values(by=['avg_cost'],ascending=False)
    fig = px.bar(final, x='avg_cost',y='name',color="name",text='avg_cost',title="Top 10 Restaurants average cost for 2 people")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
    
if user_menu == "No. of restaurants in a Location":
    st.title("No. of restaurants in a Location")
    final = df['location'].value_counts().head(10).rename_axis('Locations').reset_index(name='Counts')
    fig = px.bar(final, x='Counts',y='Locations',color="Locations",text='Counts',title="Top 10 locations restaurant count")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)
