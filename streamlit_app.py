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
    # catalog_data = session.sql(
    #     """
    #     select
    #           file_name
    #         , file_url
    #         , price
    #         , size_list
    #         , upsell_product_desc
    #     from catalog_for_website
    #     where color_or_style = '{selected_color}'
    #     """.format(selected_color=selected_option)
    # ).to_pandas()

    prod_data = session.table('catalog_for_website') \
        .select(['FILE_NAME', 'FILE_URL', 'PRICE', 'SIZE_LIST', 'UPSELL_PRODUCT_DESC']) \
        .where(col('COLOR_OR_STYLE') == selected_option).to_pandas()

    file_url = prod_data['FILE_URL'].iloc[0]
    price = '$' + str(prod_data['PRICE'].iloc[0]) + '0'
    size_list = prod_data['SIZE_LIST'].iloc[0]
    upsell = prod_data['UPSELL_PRODUCT_DESC'].iloc[0]

    product_caption = "Our warm, comfortable, {color} sweatsuit!" \
        .format(color=selected_option)

    # Render image
    st.image(image=file_url, width=400, caption=product_caption)
    st.markdown('**Price:** ' + price)
    st.markdown('**Size List:** ' + size_list)
    st.markdown(upsell)


main()
