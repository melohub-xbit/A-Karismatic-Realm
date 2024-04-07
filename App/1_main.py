import base64
import streamlit as st
from ML_Model import selectbox_items
st.set_page_config(
    page_title="A Karismatic Realm",
    page_icon="🐅",
    initial_sidebar_state="collapsed"
)
import streamlit as st

# Set the background image
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('startbackground.png');
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Your Streamlit app content goes here



# st.markdown("""
# <style>
# .eyeqlp51.st-emotion-cache-1pbsqtx.ex0cdmw0
# {visibility:hidden}
# </style""",unsafe_allow_html=True)

# background_image = "startbackground.png"

# Set background image using st.markdown() and CSS
# st.markdown(
#     f"""
#     <style>
#         .reportview-container {{
#             background: url("{background_image}") no-repeat center center fixed;
#             background-size: cover;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

def apply_css(file):
    with open(file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():

#     st.markdown("""
#     <style>
#         .main.st-emotion-cache-uf99v8.ea3mdgi8 {
#             overflow: hidden;
#         }
#     </style>
# """, unsafe_allow_html=True)
    bin_str = get_base64('./won.png')
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    '''% bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # apply_css("welcome.css")

    st.sidebar.write("About")
    st.markdown('<h1 style="color:orange; font-size: 100px;">A KARISMATIC REALM</h1>', unsafe_allow_html=True)

    st.markdown('<style>.text-box {border: 2px solid #333;padding: 20px;border-radius: 10px;background-color: orange;height:100%;width:100%;}</style><div class="text-box">This is a game which uses Aspis/GPT2-Genre-Story-Generation to progress the stories based on the inputs given by the user. It uses SDXL-Ligthning Model to generate Images of the storyline from the output generated by the GPT ML Model. As the story progesses and you reach towards the conclusion you have to fight a monster in order to win. For the game we have used opencv and pygame to make it more interesting and interactive. To start the game, hover to the sidebar and click on "Game".</div>', unsafe_allow_html=True)
    
    if "counter" not in st.session_state:
        st.session_state["counter"]=0
    if "choice" not in st.session_state:
        st.session_state["choice"]=0
        
    st.session_state["choice"] = st.selectbox("CHOOSE YOUR DESIRED STORY :",options = selectbox_items)[0]
    
    # st.markdown('<div style="text-align:center; background-color:black; padding:10px;"></div>', unsafe_allow_html=True)
    
    st.page_link("pages/2_StoryTeller.py", label="START",use_container_width=True)
    
    
    # if "counter" not in st.session_state:
    # if "counter" not in st.session_state:
main()
