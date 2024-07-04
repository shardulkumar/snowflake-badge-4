import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


def main():
    render_elements()
    return None


def render_elements():
    # Get session
    session = get_active_session()

    # Render title
    st.title("Zena's Amazing Athleisure Catalog")

    # Set the dropdown with relevant data
    available_colors = session \
        .table('ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE') \
        .select(col('color_or_style'))
    available_colors = available_colors.to_pandas()
    st.selectbox("Pick a sweatsuit color or style:", available_colors)


if __name__ == '__main__':
    main()
