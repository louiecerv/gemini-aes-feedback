import base64
import google.generativeai as genai
import streamlit as st
import os
import time
import PIL.Image

GOOGLE_API_KEY=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)


def app():

    model = genai.GenerativeModel(
        "gemini-pro-vision",
    )


    # Create two columns
    col1, col2 = st.columns([1, 4])

    # Display the image in the left column
    with col1:
        st.image("wvsu-logo.jpg")

    # Display the title in the right column
    with col2:
        st.title("Automated Essay Scoring System using Gemini on Google AI Studio")

    text = """Prof. Louie F. Cervantes, M. Eng. (Information Engineering) \n
    CCS 229 - Intelligent Systems
    Department of Computer Science
    College of Information and Communications Technology
    West Visayas State University
    """
    with st.expander("Click to display developer information."):
        st.text(text)
        link_text = "Click here to visit [Gemini 1.5 Pro](https://developers.googleblog.com/2024/04/gemini-15-pro-in-public-preview-with-new-features.html)"
        st.write(link_text)
        link_text = "Click here to visit [Gemini Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)"
        st.write(link_text)

    st.subheader("Empower Your Teaching with AI: The Gemini Teacher Copilot")
    text = """Unleash creativity and personalize learning in your classroom with 
    the Gemini Teacher Copilot, a revolutionary data app powered by Google's 
    cutting-edge large language model, Gemini 1.5 on Vertex AI. This AI co-pilot 
    equips educators with a treasure trove of ideas and resources to spark 
    student engagement, tackle challenging concepts, differentiate instruction, 
    design formative assessments, and seamlessly integrate technology into 
    lessons, all while saving educators time and boosting their teaching potential."""
    st.write(text)

    options = ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4', 'Sample 5', 'Sample 6', 'Sample 7']
  
    selected_option = st.sidebar.selectbox(
    label="Select an essay sample to use:",
    options=options,
    index=0  # Optionally set a default selected index
    )

    if selected_option == 'Sample 1':
        filename = "01.jpg"
    elif selected_option == 'Sample 2':
        filename = "02.jpg"
    elif selected_option == 'Sample 3':
        filename = "03.jpg"
    elif selected_option == 'Sample 4':
        filename = "04.jpg"
    elif selected_option == 'Sample 5':
        filename = "05.jpg"
    elif selected_option == 'Sample 6':
        filename = "06.jpg"
    elif selected_option == 'Sample 7':
        filename = "07.jpg"
    
    img = PIL.Image.open('./essays/' + filename)

    prompt = """You are a language teacher.  Score the essay response 
    found in this image.  Provide feedback and suggestions for improvement."""

    # Button to generate response
    if st.button("Score Essay"):
        progress_bar = st.progress(0, text="The AI teacher co-pilot is processing the request, please wait...")
       

        # Generate response from emini
        bot_response = model.generate_content([prompt, img])

        # Access the content of the response text
        bot_response = bot_response.text
        st.write(f"Gemini: {bot_response}")

        # update the progress bar
        for i in range(100):
            # Update progress bar value
            progress_bar.progress(i + 1)
            # Simulate some time-consuming task (e.g., sleep)
            time.sleep(0.01)
        # Progress bar reaches 100% after the loop completes
        st.success("AI teacher co-pilot task completed!") 

#run the app
if __name__ == "__main__":
  app()
