import streamlit as st
from PIL import Image





#import style.css
#import Algorithms

st.set_page_config(
    page_title="EntreprenuershipD.am",
    page_icon=":heart:", 
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
        
    }
)



def local_css(file_name):
    with open(file_name) as f:
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



def remote_css(url):
    st.sidebar.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


st.sidebar.markdown('# Welcome to Our Creativity Game!')
st.sidebar.image("Getter.png", width = 300)
Pages = st.sidebar.radio('Pages', ('Kitchen', "Technology", "Surprise"))



if Pages == 'Technology':

    
    
    tab1, tab2, tab3, tab4 = st.tabs(["Choose","Easy", "Medium", "Hard"] )
    
    with tab1 :
        st.image("Getter1.png")
        
        
    with tab2:
        st.title("What is this for?")
        st.image("vaccum.jpeg")
        
      
        
    with tab3:
        st.title("What type of creativity was this car?")
        st.image("firstcar.png")
        
    with tab4:
        st.title("What type of creativity is Iphone 14?")
        
        
if Pages == 'Kitchen':

    

    tab1, tab2, tab3, tab4 = st.tabs(['Choose',"Easy", "Medium", "Hard"] )
    
    with tab1 :
        st.image("Getter1.png")

    with tab2:
    
        st.title("What is this for?")
        st.image("water.jpeg")
        
        
    with tab3:
        st.title("Mention the pattern behind the creation of dish washer")
        
    with tab4:
        st.title("For what this tool is used for?")
        st.image("hard.png")
        
        

if Pages == 'Surprise':

    

    tab1, tab2, tab3, tab4 = st.tabs(['Choose',"Easy", "Medium", "Hard"] )
    
    with tab1 :
        st.image("Getter1.png")
    
    with tab2:
   
        st.title("What is this for?")
        st.image("tapchka.png")
        
    with tab3:
        st.title("What is convergent and divergent thinking?")
        
    with tab4:
        st.title("5 factors that block creativity")
        