import streamlit as st

def main():
    # Configure Page
    st.set_page_config(
        page_title="Home",
        page_icon="🏡",
        layout='centered',
        initial_sidebar_state="expanded",
    )
    
    st.logo("images/rudra.png")
    st.balloons()

    big_col1, big_col2 = st.columns([1, 2])

    with big_col1:
        # Display the image below the name
        st.image("images/Rudra.png", width=250, use_container_width=False)

        # Profile Section
        st.markdown("""
        <div style="text-align: center;">
            <h3 style="color: #5e17eb; font-family: 'Helvetica';">Rudra Prasad Bhuyan</h3>
        </div>
        """, unsafe_allow_html=True)

    with big_col2:
        st.markdown('<h5 style="color: #5e17eb;">Who am I?</h5>', unsafe_allow_html=True)
        st.markdown("""
        Hello, Data Enthusiasts! 😄👋

        I’m a specialist in Prompt Engineering, a Data Analyst, and a proud Kaggle Expert with a deep passion for creative storytelling and continuous learning.
        Currently, I am studying Mathematics for Data Science and have created this interactive tool to help users explore systems of linear equations in an intuitive way.
        """)

        st.divider()

        st.markdown('<h5 style="color: #5e17eb;">Why did I build this?</h5>', unsafe_allow_html=True)
        st.markdown("""
        This interactive web app is designed to help users understand and visualize systems of linear equations.

        With this tool, you can manipulate different parameters of equations and observe how they impact the solutions.
        By experimenting with these variables, you can gain a deeper insight into the underlying mathematical concepts and their real-world applications.

        This hands-on approach makes learning more engaging and effective!
        """)

if __name__ == "__main__":
    main()