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
        .select(col('color_or_style')).to_pandas()
    selected_option = st.selectbox(
        "Pick a sweatsuit color or style:",
        available_colors
    )

    catalog_column_list = [
        'FILE_NAME',
        'FILE_URL',
        'PRICE',
        'SIZE_LIST',
        'UPSELL_PRODUCT_DESC'
    ]
    prod_data = session.table('catalog_for_website') \
        .select(catalog_column_list) \
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
