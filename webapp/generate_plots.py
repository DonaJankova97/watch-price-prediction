import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

df = pd.read_csv('Luxury watch.csv')


def get_price_distribution():
    plt.close('all')
    df['Price (USD)'] = df['Price (USD)'].apply(lambda x: float(str(x).replace(',', '')))
    fig1 = sns.histplot(df['Price (USD)'], bins=30, kde=True)
    fig1.spines['right'].set_visible(False)
    fig1.spines['top'].set_visible(False)
    plt.title("Price Distribution")

    # Save the plot to a BytesIO object
    img1 = BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)

    # Encode the image to base64
    price_distribution = base64.b64encode(img1.getvalue()).decode()

    return price_distribution


def get_categorical_distribution():
    plt.close('all')
    col = ['Brand', 'Model', 'Case Material', 'Strap Material', 'Movement Type', 'Water Resistance', 'Dial Color',
           'Crystal Material', 'Power Reserve']
    plt.figure(figsize=(15, 13))
    for num, i in enumerate(col, 1):
        plt.subplot(5, 2, num)
        fig = sns.countplot(x=df[i], data=df, order=df[i].value_counts().head().index)
        fig.spines['right'].set_visible(False)
        fig.spines['top'].set_visible(False)
    plt.tight_layout()
    plt.suptitle("Categorical Distribution")
    plt.subplots_adjust(top=0.95)

    # Save the plot to a BytesIO object
    img2 = BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)

    # Encode the image to base64
    categorical_distribution = base64.b64encode(img2.getvalue()).decode()

    return categorical_distribution


def get_numerical_distribution():
    plt.close('all')
    fig, axes = plt.subplots(figsize=(15, 7), nrows=2, ncols=2)

    sns.histplot(df['Price (USD)'], bins=30, kde=True, ax=axes[0, 0])
    axes[0, 0].spines['right'].set_visible(False)
    axes[0, 0].spines['top'].set_visible(False)

    sns.histplot(df['Case Diameter (mm)'], bins=30, kde=True, ax=axes[0, 1])
    axes[0, 1].spines['right'].set_visible(False)
    axes[0, 1].spines['top'].set_visible(False)

    sns.histplot(df['Case Thickness (mm)'], bins=30, kde=True, ax=axes[1, 0])
    axes[1, 0].spines['right'].set_visible(False)
    axes[1, 0].spines['top'].set_visible(False)

    sns.histplot(df['Band Width (mm)'], bins=30, kde=True, ax=axes[1, 1])
    axes[1, 1].spines['right'].set_visible(False)
    axes[1, 1].spines['top'].set_visible(False)

    plt.tight_layout()
    plt.suptitle("Numerical Distribution")
    plt.subplots_adjust(top=0.92)

    # Save the plot to a BytesIO object
    img3 = BytesIO()
    plt.savefig(img3, format='png')
    img3.seek(0)

    # Encode the image to base64
    numerical_distribution = base64.b64encode(img3.getvalue()).decode()

    return numerical_distribution




