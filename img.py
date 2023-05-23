from PIL import Image, ImageDraw, ImageFont


def merge_images(canvas, poster, text, text_size, color, font):
    # Resize the images to the same dimensions (optional)
    canvas = canvas.resize((1000, 500))
    poster = poster.resize((350, 500))

    # Create a new image with transparency (RGBA mode)
    result = Image.new("RGBA", canvas.size)

    # Paste image1 onto the result image at the top-left corner
    result.paste(canvas, (0, 0))

    # Paste poster onto the result image with an offset
    offset = (50, 50)
    result.paste(poster)

    # Create a draw object
    draw = ImageDraw.Draw(result)

    # Configure font
    font_map = {
        "Arial": "arial.ttf",
        "Times New Roman": "times.ttf",
        "Courier New": "cour.ttf",
        "Georgia": "georgia.ttf",
        "Verdana": "verdana.ttf",
        "Tahoma": "tahoma.ttf",
    }

    # Set the font and size of the text
    font = ImageFont.truetype(font_map[font], text_size)

    # Write the text on the image
    draw.text((400, 100), text=text, fill=color, font=font)

    return result

    # # Save the overlapped image
    # result.save('overlap.png')
