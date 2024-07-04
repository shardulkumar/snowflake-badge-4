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
        .table('catalog_for_website') \
        .select(col('color_or_style'))
    available_colors = available_colors.to_pandas()
    selected_option = st.selectbox(
        "Pick a sweatsuit color or style:",
        available_colors
    )

    # Get image_link, size etc from catalog view
    catalog_data = session.sql(
        """
        select
              file_name
            , file_url
            , price
            , size_list
            , upsell_product_desc
        from catalog_for_website
        where color_or_style = '{selected_color}'
        """.format(selected_color=selected_option)
    ).to_pandas()

    st.text(catalog_data)

    # Render image
    # st.image(image='', width=400, caption='test caption')
    # st.markdown('**Price:** ' + price)


main()
