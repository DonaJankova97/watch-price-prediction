import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import st_static_export as sse

df = pd.read_csv("../model/processed_df.csv", index_col=0)
catcols = list(df.select_dtypes(include=['object']).columns)
numcols = list(df.select_dtypes(include=['float64','int']).columns)


def categorical_data():
    for num, i in enumerate(catcols, 1):
        fig, ax = plt.subplots(figsize=(20, 10))
        sns.countplot(x=df[i], data=df, order=df[i].value_counts().index)
        plt.xticks(rotation=90)
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2., p.get_height(), '%d' % int(p.get_height()),
                    fontsize=12, color='black', ha='center', va='bottom')
        st.pyplot(fig)


def numerical_data():
    plot_type = st.sidebar.radio("Choose a plot type", ["Distribution", "Outliers", "Correlation"])

    if plot_type == "Density":
        for num, i in enumerate(numcols, 1):
            fig, ax = plt.subplots(figsize=(20, 10))
            sns.distplot(df[i], bins=30)
            st.pyplot(fig)
    elif plot_type == "Outliers":
        for num, i in enumerate(numcols, 1):
            fig, ax = plt.subplots(figsize=(20, 10))
            sns.boxplot(x=df[i])
            st.pyplot(fig)
    elif plot_type == "Correlation":
        fig, ax = plt.subplots(figsize=(20, 10))
        sns.heatmap(df[numcols].corr())
        st.pyplot(fig)


# Sidebar
st.sidebar.title('Select Data Type')
data_type = st.sidebar.selectbox('Data Type', ['Categorical', 'Numerical'])

# Main content
st.markdown("<h1 style='text-align: center;'>Here are some plots to gain better understanding of the data</h1>", unsafe_allow_html=True)

if data_type == 'Categorical':
    categorical_data()
elif data_type == 'Numerical':
    numerical_data()
