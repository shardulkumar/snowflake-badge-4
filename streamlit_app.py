import streamlit as st
from snowflake.snowpark.context import get_active_session


def main():
    return None


def render_elements():
    # Get session
    session = get_active_session()

    # Render title
    st.title("Zena's Amazing Athleisure Catalog")

    # Set the dropdown with relevant data
    available_colors = session.sql("""
        select color_or_style
        from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE
    """).to_pandas()
    st.selectbox("Pick a sweatsuit color or style:", available_colors)

    return None


if __name__ == '__main__':
    main()
