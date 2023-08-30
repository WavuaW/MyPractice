from PIL import Image
import requests
import streamlit as st 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",page_icon=":two_hearts:", layout="wide")

lottie_coding = "https://lottie.host/3c21c6f2-5e9c-42f8-887f-9ccf3c17d805/TLesUCSsP0.json"
img_contact_form = Image.open("Images/pexels-thisisengineering-3861969.jpg")
img_lottie_image = Image.open("Images/pexels-antoni-shkraba-4348401.jpg")

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

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)       
    with text_column:
        st.subheader("Sample of What I might work on as a data scientist in the future")
        st.write(
            """
            At Quantum HealthTech Solutions, our data science team spearheaded a transformative project aiming to optimize patient outcomes in intensive care units (ICUs).
            Utilizing a vast dataset comprising multi-year electronic health records, the team developed a predictive analytics model to anticipate the risk of sepsis—a life-threatening condition resulting from infections—hours before clinical symptoms became apparent. By integrating real-time patient monitoring data with historical trends, the model achieved an impressive 95% accuracy rate. 
            This proactive approach not only ensured timely interventions but also significantly reduced ICU mortality rates. Furthermore, by implementing this solution across several hospitals, the organization saw a marked decrease in medical costs associated with prolonged ICU stays. This initiative perfectly exemplifies the power of data science in revolutionizing healthcare, making treatments more personalized, timely, and efficient.
            """
        )
        st.markdown("[Watch Video ...](https://www.youtube.com/watch?v=VqgUkExPvLY&list=TLPQMzAwODIwMjPwamnV3r0dmQ&index=3)")
with st.container():
    st.write("---")
    text_column, image_column = st.columns((2, 1))
    with text_column:
        st.subheader("Yet another sample of Future Chris The Data Scientist ")
        st.write(
            """
            AIn an urban setting, a data scientist was tasked with optimizing the city's public transportation system. 
            By gathering vast amounts of data from bus and train sensors, passenger check-ins, and ticket sales, the data scientist built a predictive model to analyze peak travel times, routes with the highest traffic, and areas of delay. Leveraging machine learning techniques, they were able to forecast demand, suggesting where and when additional buses or trains might be needed. Furthermore, by studying patterns in delays, they recommended infrastructure upgrades at specific bottlenecks, ensuring smoother transit for thousands of daily commuters. The project not only improved the efficiency of the city's transportation but also significantly enhanced the commuting experience for its residents.
            """
        )
        st.markdown("[Watch Video ...](https://www.youtube.com/watch?v=VqgUkExPvLY&list=TLPQMzAwODIwMjPwamnV3r0dmQ&index=3)")
    with image_column:
        st.image(img_lottie_image)

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    # https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/wavuamuroka@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True )
with right_column:
    st.empty()