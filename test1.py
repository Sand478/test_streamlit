import streamlit as st

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Добрый день! 👋")

    st.sidebar.markdown("Главная страница")

    st.markdown(
        """
        Это проверка работы стримлита.  
        👈 Кликните в сайдбаре слева.
        """)

if __name__ == "__main__":
    run()
