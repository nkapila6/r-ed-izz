import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Image to Video Generator",
    page_icon="🎬",
    layout="wide"
)

# Title
st.title("Image to Video Generator")

def generate_video(image, prompt):
    """
    Placeholder function for API call to generate video
    Replace with actual API integration
    """
    try:
        # Add your API integration here
        # Example structure:
        # response = requests.post(
        #     "YOUR_API_ENDPOINT",
        #     files={"image": image},
        #     data={"prompt": prompt}
        # )
        # return response.json()["video_url"]
        return "placeholder_video_url"
    except Exception as e:
        st.error(f"Error generating video: {str(e)}")
        return None

def main():
    # Sidebar
    
    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    # Text input for prompt
    prompt = st.text_area("Enter your prompt for video generation", 
                         help="Describe how you want the video to be generated from the image")
    
    if uploaded_file and prompt:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Generate button
        if st.button("Generate Video"):
            with st.spinner("Generating video..."):
                # Call API function
                video_url = generate_video(uploaded_file, prompt)
                
                if video_url:
                    # Display generated video
                    st.success("Video generated successfully!")
                    st.video(video_url)
                else:
                    st.error("Failed to generate video. Please try again.")

if __name__ == "__main__":
    main()
