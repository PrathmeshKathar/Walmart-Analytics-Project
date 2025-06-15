import plotly.express as px

def plot_sales_by_category(df):
    if 'category' not in df.columns or 'Predicted Total' not in df.columns:
        return None

    category_sales = df.groupby('category')['Predicted Total'].sum().reset_index()
    fig = px.bar(category_sales, x='category', y='Predicted Total',
                 title='Predicted Sales by Category',
                 color='category', height=400)
    return fig
