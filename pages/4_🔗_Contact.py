import streamlit as st
import pandas as pd

def main():
    
    st.set_page_config(
    page_title="Contact Info",
    page_icon="🔗",
    layout='centered',
    )
    
    st.logo("images/rudra.png")
    
    st.title("My Social Media Links")
    
    col1, col2 = st.columns(2)
    with col1:
        # Display the image below the name
        st.image("images/Rudra.png", width=250, use_container_width=False)    

        # Profile Section
        st.markdown("""
        <div style="text-align:left;">
            <h3 style="color: #5e17eb; font-family: 'Helvetica';">Rudra Prasad Bhuyan</h3>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:  
        st.subheader("I am glad to connect with you! 😄")  
        social_media = {
            "LinkedIn": "https://www.linkedin.com/in/rudra-prasad-bhuyan-44a388235/",  
            "GitHub": "https://github.com/Rudra-G-23" ,
            "YouTube": "https://www.youtube.com/@Rudra_love_with_data",
            "Kaggle": "https://www.kaggle.com/rudraprasadbhuyan",
            
        }

        # Create a Pandas DataFrame from the dictionary
        df = pd.DataFrame(list(social_media.items()), columns=["Social Media", "Link"])

        # Function to create clickable links in the table
        def make_clickable(link):
            return f'<a target="_blank" href="{link}">Link</a>'

        # Apply the make_clickable function to the 'Link' column
        df['Link'] = df['Link'].apply(make_clickable)

        # Display the table as HTML to render links
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
        
        st.markdown("**Thank You 🙏**")

if __name__ == "__main__":
    main()
  