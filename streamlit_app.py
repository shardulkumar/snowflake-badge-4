import streamlit as st
from snowflake.snowpark.functions import col


def main():
    render_elements()


def render_elements():
    # Get session
    cnx = st.connection("snowflake")
    session = cnx.session()

    # Render title
    st.title("Zena's Amazing Athleisure Catalog")

    # Set the dropdown with relevant data
    available_colors = session \
        .table('ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE') \
        .select(col('color_or_style'))
    available_colors = available_colors.to_pandas()
    st.selectbox("Pick a sweatsuit color or style:", available_colors)


main()
