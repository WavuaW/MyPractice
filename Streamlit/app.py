import requests
import streamlit as st 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",page_icon=":two_hearts:", layout="wide")

lottie_coding = "https://lottie.host/3c21c6f2-5e9c-42f8-887f-9ccf3c17d805/TLesUCSsP0.json"

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


with st.container():
    st.subheader("Hi, I am Chris :alien_monster:")
    st.title("A Future Data Scientist From Kenya")
    st.write("I am passionate about tech and finding solutions and innovations related to tech")
    st.write("[Learn More >](https://www.webfx.com/tools/emoji-cheat-sheet/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            A Data Scientist plays a multifaceted role in extracting valuable insights from vast amounts of data to drive business decisions. In their career, a Data Scientist might:
                - Data Collection & Cleaning: Gather raw data from diverse sources and preprocess it, ensuring it is clean, reliable, and ready for analysis.
                
                - Statistical Analysis & Machine Learning: Implement statistical methods and machine learning algorithms to predict future events, classify data points, or uncover patterns.
                
                - Data Visualization: Create compelling visualizations that help stakeholders understand the significance of the data insights, using tools like Matplotlib, Seaborn, or Tableau.
                
                - Big Data Technologies: Utilize big data platforms and tools like Hadoop and Spark to manage and analyze vast amounts of data efficiently.
               
                - Collaboration: Work alongside business analysts, product managers, and other professionals to ensure data-driven recommendations align with company objectives and stakeholder needs.
                
                - Stay Updated: Continuously learn about the latest trends, tools, and techniques in the data science world, ensuring their skills remain relevant.
                
                - Ethical Considerations: Ensure that data usage and analytical processes adhere to ethical standards and respect privacy concerns.
            In essence, a Data Scientist bridges the technical and business realms, transforming raw data into actionable insights that can steer a company's future direction.
            """
        )

        st.write("[Patreon](https://www.patreon.com/login)")

    with right_column:
        st_lottie(lottie_coding, height=700, key="coding") 
