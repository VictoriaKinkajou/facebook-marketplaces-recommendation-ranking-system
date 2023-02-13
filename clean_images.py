from PIL import Image
import os

def clean_image_data(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.LANCZOS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im

def make_folder():
    dir = "cleaned_images"
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        pass

if __name__ == '__main__':
    make_folder()
    path = "images_fb_raw/"
    dirs = os.listdir(path)
    final_size = 512
    
    for n, item in enumerate(dirs, 1):
        im = Image.open('images_fb_raw/' + item)
        new_im = clean_image_data(final_size, im)
        new_im.save(f'cleaned_images/{n}_resized.jpg')
