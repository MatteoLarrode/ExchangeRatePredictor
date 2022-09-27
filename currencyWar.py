from PIL import Image

im1 = Image.open('./images/USD-BRL.png')
im2 = Image.open('./images/USD-INR.png')
im3 = Image.open('./images/USD-THB.png')
im4 = Image.open('./images/USD-KRW.png')

def get_concat_h(im1, im2, im3, im4):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (0, im1.height))
    dst.paste(im4, (im1.width, im1.height))
    return dst

get_concat_h(im1, im2, im3, im4).save('./images/currency-war.jpg')