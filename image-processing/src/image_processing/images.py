from PIL import Image, ImageFilter


def pokemon():
    img = Image.open('./images/pikachu.jpg')

    ## Blur images
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save('./processed_images/pikachu_blur.png', 'png')

    ## Convert image to different format
    filtered_img_convert = img.convert('L')
    filtered_img_convert.save('./processed_images/pikachu_black_and_white.png', 'png')

    ## Rotate images
    filtered_img_rotate = img.convert('L')
    crooked = filtered_img_rotate.rotate(90)
    crooked.save('./processed_images/pikachu_black_and_white_rotate.png', 'png')

    ## Resize images
    filtered_img_resize = img.resize((300, 300))
    filtered_img_resize.save('./processed_images/pikachu_resized.png', 'png')

    ## Crop images
    box = (100, 100, 400, 400)
    filtered_img_crop = img.crop(box)
    filtered_img_crop.save('./processed_images/pikachu_cropped.png', 'png')


def astronaut():
    image = Image.open('./images/astronaut.jpg')
    image.thumbnail((400, 400))
    image.save('./processed_images/astronaut_resized.jpg')
    print(image.size)


if __name__ == '__main__':
    # pokemon()
    astronaut()
