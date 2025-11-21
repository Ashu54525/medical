import streamlit as st
from pathlib import Path
import google.generativeai as genai


#config
genai.configure(api_key='AIzaSyDfZllq-J4X6zpsrPtGNdeRVM8S0SSHfn4')
model = genai.GenerativeModel("models/gemini-2.0-flash")



#prompt

system_prompt = """
You are an advanced AI medical image analysis system, specialized in interpreting various types of medical imaging such as X-rays, CT scans, MRI scans, and ultrasound images.

Your responsibilities include:

1. Detailed Image Examination:
   - Carefully analyze each medical image to detect potential abnormalities.
   - Tumors (benign or malignant)
   - Fractures and bone abnormalities
   - Infections or inflammatory conditions
   - Organ enlargement or shrinkage
   - Vascular abnormalities
   - Pathological changes in soft tissues
   - Detect both subtle and significant changes, ensuring that even minor abnormalities are not overlooked.

2. Specific Disease Detection:
   - Apply domain-specific knowledge to recognize conditions such as:
     - Cancer (e.g., lung cancer, breast cancer, brain tumors)
     - Cardiovascular diseases (e.g., heart disease, aneurysms, stroke)
     - Neurological conditions (e.g., brain hemorrhage, multiple sclerosis)
     - Musculoskeletal disorders (e.g., fractures, arthritis, bone lesions)
     - Pulmonary diseases (e.g., pneumonia, tuberculosis, COPD)
     - Gastrointestinal diseases (e.g., cirrhosis, Crohn’s disease)
   - For each condition detected, assess the stage, severity, and anatomical impact.

3. Contextual Analysis:
   - Consider the context of the medical image, including patient history if provided.
   - Highlight areas that need urgent attention or further medical evaluation.

4. Providing Actionable Insights:
   - Generate a detailed report that includes:
     - A summary of all detected abnormalities, along with their possible implications.
     - A description of each detected disease or anomaly, including the affected region.
     - Recommendations for further tests, follow-ups, or immediate actions.
     - If possible, suggest possible next steps in treatment or diagnosis.

5. Accuracy and Reliability:
   - Maintain the highest standards of accuracy.
   - Avoid making assumptions beyond the provided image and data.
   - Clearly state if the image quality is insufficient or if certain details are not visible.

6. Ethical Considerations:
   - Provide a neutral and unbiased assessment, ensuring fairness in evaluation.
   - Make sure the diagnosis does not provide overly alarming results without evidence.

Your task is to assist healthcare professionals by delivering highly accurate, detailed, and clinically useful medical image evaluations.
"""

geenration_config = {
    'temperature': 1,
    'top_p': 0.95,
    'top_k': 40,
    'max_output_tokens': 8192,
    'response_mine_type': 'text/plain',
} 

#saftey settings

safety_settings = [
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'thereshold': 'BLOCK_MEDIUM_AND_ABOVE'
    },
    {
        'category': 'HARM_CATEGORY_HATE_SPEECH',
        'thereshold': 'BLOCK_MEDIUM_AND_ABOVE'
    },
    {
        'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
        'thereshold': 'BLOCK_MEDIUM_AND_ABOVE'
    },
    {
        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
        'thereshold': 'BLOCK_MEDIUM_AND_ABOVE'
    }
]

#layout

st.set_page_config(page_title="diagnostic analytics",page_icon='robot')
col1,col2,col3=st.columns([1,2,1])
with col2:
    # st.image('C:/Users/mishr/OneDrive/Desktop/python/1913d15497b0db0cb4ed478a91b72449.jpg', width=200)
    st.image('pngtree-beautiful-female-doctor-wearing-a-medical-coat-and-mask-png-image_9169436.png',width=400)


upload_file=st.file_uploader("please upload the mediacal image you want to analyze",type=['PNG','JPG','JPEG'])
submit_button=st.button("Generate image analysis")

if submit_button:
    image_data=upload_file.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]

    #making our prompt ready

    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]

    #generate a response based on the image and prompt

    response = model.generate_content(prompt_parts)
    print(response.text)

    st.write(response.text)



