PROJECT_ID = "rahul-research-test"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

# Initialize Vertex AI
import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)
from vertexai.generative_models import GenerativeModel, Image
import http.client
import io
import typing
import urllib.request

import IPython.display
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps


def display_image(image: Image, max_width: int = 600, max_height: int = 350) -> None:
    pil_image = typing.cast(PIL_Image.Image, image._pil_image)
    if pil_image.mode != "RGB":
        # Modes such as RGBA are not yet supported by all Jupyter environments
        pil_image = pil_image.convert("RGB")
    image_width, image_height = pil_image.size
    if max_width < image_width or max_height < image_height:
        # Resize to display a smaller notebook image
        pil_image = PIL_ImageOps.contain(pil_image, (max_width, max_height))
    display_image_compressed(pil_image)


def display_image_compressed(pil_image: PIL_Image.Image) -> None:
    image_io = io.BytesIO()
    pil_image.save(image_io, "jpeg", quality=80, optimize=True)
    image_bytes = image_io.getvalue()
    ipython_image = IPython.display.Image(image_bytes)
    IPython.display.display(ipython_image)


def get_image_bytes_from_url(image_url: str) -> bytes:
    with urllib.request.urlopen(image_url) as response:
        response = typing.cast(http.client.HTTPResponse, response)
        print(response.headers["Content-Type"])
        # if response.headers["Content-Type"] not in ("image/png", "image/jpeg","image/jpg"):
        #     raise Exception("Image can only be in PNG or JPEG format")
        image_bytes = response.read()
    return image_bytes


def load_image_from_url(image_url: str) -> Image:
    image_bytes = get_image_bytes_from_url(image_url)
    return Image.from_bytes(image_bytes)


def print_multimodal_prompt(contents: list):
    """
    Given contents that would be sent to Gemini,
    output the full multimodal prompt for ease of readability.
    """
    for content in contents:
        if isinstance(content, Image):
            display_image(content)
        else:
            print(content)




def chair_rec():
    # urls for room images
    room_image_url = "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/rooms/spacejoy-c0JoR_-2x3E-unsplash.jpg"

    # load room images as Image Objects
    room_image = load_image_from_url(room_image_url)

    # Download and display sample chairs
    furniture_image_urls = [
        "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/cesar-couto-OB2F6CsMva8-unsplash.jpg",
        "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/daniil-silantev-1P6AnKDw6S8-unsplash.jpg",
        "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/ruslan-bardash-4kTbAMRAHtQ-unsplash.jpg",
        "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/furnitures/scopic-ltd-NLlWwR4d3qU-unsplash.jpg",
    ]

    # Load furniture images as Image Objects
    furniture_images = [load_image_from_url(url) for url in furniture_image_urls]

    # To recommend an item from a selection, you will need to label the item number within the prompt.
    # Labelling images within your prompt also help to reduce hallucinations and overall produce better results.
    contents = [
        "Consider the following chairs:",
        "chair 1:",
        furniture_images[0],
        "chair 2:",
        furniture_images[1],
        "chair 3:",
        furniture_images[2],
        "chair 4:",
        furniture_images[3],
        "room:",
        room_image,
        '''You are an interior designer. For each chair, explain whether it would be appropriate for the style of the room in brief with a rating out of 5, also give assesment in tabular form, keep tone formal
        
        Output format :- 
        Room assesment(heading): contents in bulleted manner 
        Product assesment(heading): contents in tabular manner 
        Additional considerations : (if any then only)
        ''',
    ]

    multimodal_model = GenerativeModel("gemini-1.5-pro")
    responses = multimodal_model.generate_content(contents)
    return responses.text



def switchboard_rec():

    # urls for room images
    room_image_url = "https://media.istockphoto.com/id/1390233984/photo/modern-luxury-bedroom.jpg?s=612x612&w=0&k=20&c=po91poqYoQTbHUpO1LD1HcxCFZVpRG-loAMWZT7YRe4="

    # "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/rooms/spacejoy-c0JoR_-2x3E-unsplash.jpg"

    # load room images as Image Objects
    room_image = load_image_from_url(room_image_url)



    # Download and display sample chairs
    furniture_image_urls = [
        "https://img.staticmb.com/mbcontent/images/crop/uploads/2023/3/Wooden-modular-switchboard-designs-with-switches-and-sockets_0_1200.jpg",
       "https://t3.ftcdn.net/jpg/06/25/01/76/240_F_625017618_XEaENhgwNaQibpH5yzlqFvVNuyq1jBNE.jpg",
        "https://5.imimg.com/data5/SG/TT/MY-44167071/electrical-switche-500x500.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU5Z_HeKkI078zmFYQATbDQBQW5BjLZvZ8SA&s",
    ]

    # Load furniture images as Image Objects
    furniture_images = [load_image_from_url(url) for url in furniture_image_urls]

    # To recommend an item from a selection, you will need to label the item number within the prompt.
    # Labelling images within your prompt also help to reduce hallucinations and overall produce better results.
    contents = [
        "Consider the following swatch boards:",
        "switch board 1:",
        furniture_images[0],
        "switch board 2:",
        furniture_images[1],
        "switch board 3:",
        furniture_images[2],
        "switch board 4:",
        furniture_images[3],
        "room:",
        room_image,
        '''You are an interior designer. For each switch board , explain whether it would be appropriate for the style of the room in brief with a rating out of 5, also give assesment in tabular form, keep tone formal. 
        
        Output format :- 
        Room assesment(heading): contents in bulleted manner 
        Product assesment(heading): contents in tabular manner 
        Additional considerations : (if any then only)
        ''',
    ]



    multimodal_model = GenerativeModel("gemini-1.5-pro")
    responses = multimodal_model.generate_content(contents)
    return responses.text




def glasses_rec():
    # urls for room images
    user_face_image_url = "https://yt3.ggpht.com/yti/ANjgQV-XT-CXzcNZ5w8CXilWChhX8lHH-2j1Rk5krVzxyprd5pg=s108-c-k-c0x00ffffff-no-rj"

    # "https://storage.googleapis.com/github-repo/img/gemini/retail-recommendations/rooms/spacejoy-c0JoR_-2x3E-unsplash.jpg"

    # load room images as Image Objects
    user_image = load_image_from_url(user_face_image_url)



    # Download and display sample chairs
    spec_image_urls = [
        "https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//j/i/john-jacobs-jj-e16116-c2-eyeglasses_g_8777_19_10_2023.jpg",
       "https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//v/i/Purple-Silver-Purple-Transparent-Full-Rim-Round-Vincent-Chase-SLEEK-STEEL-VC-E13784-C1-Eyeglasses_vincent-chase-vc-e13784-c1-eyeglasses_g_301709_02_2022.jpg",
        "https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//j/o/john-jacobs-jj-e13346-c2-eyeglasses_g_5793.jpg",
        "https://static5.lenskart.com/media/catalog/product/pro/1/thumbnail/628x301/9df78eab33525d08d6e5fb8d27136e95//v/i/brown-transparent-silver-full-rim-cat-eye-vincent-chase-blend-edit-vc-e14973-c2-eyeglasses_g_3516_10_14_22.jpg",
    ]

    # Load furniture images as Image Objects
    spec_images = [load_image_from_url(url) for url in spec_image_urls]

    # To recommend an item from a selection, you will need to label the item number within the prompt.
    # Labelling images within your prompt also help to reduce hallucinations and overall produce better results.
    contents = [
        "Consider the following swatch boards:",
        "spec type 1:",
        spec_images[0],
        "spec type 2:",
        spec_images[1],
        "spec type 3:",
        spec_images[2],
        "spec type 4:",
        spec_images[3],
        "user face pic:",
        user_image,
        '''You are a glasses/spectacles fashion advisor your task is to analyse user face structure and advice them with best options of given glasses. For each spec type , explain whether it would be appropriate for the user to choose them to wear in brief with a rating based upon looks of the glass and how it would affect user face, also give assesment in tabular form. keep tone formal.
        Output format :- 
        Face assesment(heading): contents in bulleted manner 
        Product assesment(heading): contents in tabular manner 
        Additional considerations : (if any then only)
        ''',
    ]

    multimodal_model = GenerativeModel("gemini-1.5-pro")
    responses = multimodal_model.generate_content(contents)
    return responses.text