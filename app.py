import streamlit as st
from PIL import Image
from img import merge_images

# making the app full width
st.set_page_config(layout="wide")

# title
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom : 30px'>Image Merger</h1>
    """,
    unsafe_allow_html=True,
)

# file uploader
fcol1, fcol2 = st.columns(2)
with fcol1:
    poster_file = st.file_uploader("Choose an image for poster", type="jpg")

with fcol2:
    canvas_file = st.file_uploader("Choose an image for canvas (optional)", type="jpg")

# getting inputs for text
text = st.text_area("Enter the text to display")

icol1, icol2 = st.columns(2)

with icol1:
    text_size = st.slider("Select Text Size", 10, 100, 50)

with icol2:
    iicol1, iicol2 = st.columns(2)

    with iicol1:
        color = st.color_picker("Select Text Color", "#00f900")

    with iicol2:
        font = st.selectbox(
            "Select Font",
            ["Arial", "Times New Roman", "Courier New", "Georgia", "Verdana", "Tahoma"],
        )

# converting the files to PIL images
poster = Image.open(poster_file) if poster_file is not None else None
canvas = Image.open(canvas_file) if canvas_file is not None else None

# displaying the images
dcol1, dcol2 = st.columns(2)
with dcol1:
    if poster is not None:
        st.image(poster, caption="Poster Image", use_column_width=True)
        st.write("")

with dcol2:
    if canvas is not None:
        st.image(canvas, caption="Canvas Image", use_column_width=True)
        st.write("")

result = None

canvas = Image.open("Canvas.jpg") if canvas is None else canvas

# merging the images
if poster is not None:
    result = merge_images(
        canvas=canvas,
        poster=poster,
        text=text,
        text_size=text_size,
        color=color,
        font=font,
    )
else:
    st.write("Please upload Poster image")

# displaying the result
if result is not None:
    st.image(result, caption="Result Image", use_column_width=True)
    st.write("")
