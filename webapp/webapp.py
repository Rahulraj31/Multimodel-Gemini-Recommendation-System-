import streamlit as st
from example_main import * 
from stqdm import stqdm


st. set_page_config(layout="wide")
st.title("Multi Model Recommendation Engine")
st.subheader(" Using Gemini to recommend items based on images and image reasoning")
# Define options
options = ["Select Options","1. Furniture Recommendations", "2. Wall Fixtures Recommendations", "3. Fashion Recommendations"]
# Select box for user input
selected_option = st.selectbox("Select an option to view different categories of recommendations:", options,placeholder="Select Options")
# Display content based on the selected option, with error handling

if selected_option == options[0]:
    st.markdown('''
    
## Overview
For retail companies, recommendation systems improve customer experience and thus can increase sales.

This demo shows how you can use the multimodal capabilities of Gemini 1.5 Pro model to rapidly create a multimodal recommendation system out-of-the-box.
Understanding the Power of Multimodal Models

Gemini 1.5 Pro, with its advanced multimodal capabilities, is uniquely positioned to revolutionize retail recommendation systems. 
It empowers retailers to build powerful multimodal recommendation systems that drive sales and customer satisfaction. 
By leveraging the model's ability to understand and process diverse data modalities, businesses can deliver personalized and 
engaging shopping experiences.
    
##### Key Advantages of Multimodal Recommendation Systems

 - **Enhanced Product Understanding:** By analyzing product descriptions, images, and customer reviews, the model can gain a deeper understanding of product attributes and customer preferences.
 - **Improved Recommendation Accuracy:** Multimodal models can capture subtle nuances and contextual information that may be missed by traditional text-based systems.
 - **Personalized Experiences:** By considering user behavior, demographics, and purchase history, the model can tailor recommendations to individual preferences.
 - **Visual Search and Discovery:** Users can search for products using images, enabling a more intuitive and efficient shopping experience.       ''')

elif selected_option == options[1]: # Chair product
    st.markdown(''' ### Furniture Recommendation Based on Room Aesthetic
The customer shows uploads a pic of their living room and wants recommendations on which of the following chairs will look best in the room.   

     ''' 
        ,unsafe_allow_html=True)
    cols = st.columns(2,gap="small", vertical_alignment="center")
    with cols[0]:
        st.subheader("Room Image")
        st.image("https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/rooms/spacejoy-c0JoR_-2x3E-unsplash.jpg", width=600)
        st.text("")
    
    with cols[1]:
        st.subheader("Products Selected")
        sub_cols = st.columns(2,gap="small",vertical_alignment="center")
        sub_cols[0].image("https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/cesar-couto-OB2F6CsMva8-unsplash.jpg",width=125, caption="Product 1",)
        sub_cols[1].image("https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/daniil-silantev-1P6AnKDw6S8-unsplash.jpg",width=125,caption="Product 2")
        sub_cols[0].image("https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/ruslan-bardash-4kTbAMRAHtQ-unsplash.jpg",width=125,caption="Product 3")
        sub_cols[1].image("https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/scopic-ltd-NLlWwR4d3qU-unsplash.jpg",width=125,caption="Product 4")

    _,but_col,_ = st.columns(3,gap="large",vertical_alignment="center")
    if but_col.button("Generate Recommendations"):
        with st.spinner("Generating..."):
            st.write(chair_rec())

elif selected_option == options[2]: # Switch board Product
    st.markdown(''' ### Wall Fixtures Recommendation Based on Room Aesthetic
The customer shows uploads a pic of their living room and wants recommendations on which of the following products will look best in the room.   

     ''' 
        ,unsafe_allow_html=True)
    cols = st.columns(2,gap="small", vertical_alignment="center")
    with cols[0]:
        st.subheader("Room Image")
        st.image("https://media.istockphoto.com/id/1390233984/photo/modern-luxury-bedroom.jpg?s=612x612&w=0&k=20&c=po91poqYoQTbHUpO1LD1HcxCFZVpRG-loAMWZT7YRe4=", width=600)
        st.text("")
    
    with cols[1]:
        st.subheader("Products Selected")
        sub_cols = st.columns(2,gap="small",vertical_alignment="center")
        sub_cols[0].image("https://img.staticmb.com/mbcontent/images/crop/uploads/2023/3/Wooden-modular-switchboard-designs-with-switches-and-sockets_0_1200.jpg",width=125, caption="Product 1",)
        sub_cols[1].image("https://t3.ftcdn.net/jpg/06/25/01/76/240_F_625017618_XEaENhgwNaQibpH5yzlqFvVNuyq1jBNE.jpg",width=200,caption="Product 2")
        sub_cols[0].image("https://5.imimg.com/data5/SG/TT/MY-44167071/electrical-switche-500x500.jpg",width=125,caption="Product 3")
        sub_cols[1].image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU5Z_HeKkI078zmFYQATbDQBQW5BjLZvZ8SA&s",width=225,caption="Product 4")

    _,but_col,_ = st.columns(3,gap="large",vertical_alignment="center")
    if but_col.button("Generate Recommendations"):
        with st.spinner("Generating..."):
            st.write(switchboard_rec())


elif selected_option == options[3]: # Glasses Product
    st.markdown(''' ### Fashion Recommendation Based on User Appearance 
The customer uploads their image and wants recommendations on which of the following chairs products look best on them.   

     ''' 
        ,unsafe_allow_html=True)
    cols = st.columns(2,gap="small", vertical_alignment="center")
    with cols[0]:
        st.subheader("User Image")
        st.image("https://raw.githubusercontent.com/Rahulraj31/Multimodel-Gemini-Recommendation-System-/refs/heads/main/sample-user-image.jpeg", width=250)
        st.text("")
    
    with cols[1]:
        st.subheader("Products Selected")
        sub_cols = st.columns(2,gap="small",vertical_alignment="center")
        sub_cols[0].image("https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//j/i/john-jacobs-jj-e16116-c2-eyeglasses_g_8777_19_10_2023.jpg"
        ,width=300, caption="Product 1",)
        sub_cols[1].image("https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//v/i/Purple-Silver-Purple-Transparent-Full-Rim-Round-Vincent-Chase-SLEEK-STEEL-VC-E13784-C1-Eyeglasses_vincent-chase-vc-e13784-c1-eyeglasses_g_301709_02_2022.jpg"
        ,width=300,caption="Product 2")
        sub_cols[0].image("https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//j/o/john-jacobs-jj-e13346-c2-eyeglasses_g_5793.jpg"
        ,width=300,caption="Product 3")
        sub_cols[1].image("https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//v/i/brown-transparent-silver-full-rim-cat-eye-vincent-chase-blend-edit-vc-e14973-c2-eyeglasses_g_3516_10_14_22.jpg"
        ,width=300,caption="Product 4")

    _,but_col,_ = st.columns(3,gap="large",vertical_alignment="center")
    if but_col.button("Generate Recommendations"):
        with st.spinner("Generating..."):
            st.write(glasses_rec())

else:
    pass 
