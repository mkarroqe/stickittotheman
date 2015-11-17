 
#	stickittotheman
#       
#      _    ,`,
#     (_\   |_|
#      \_\  |_|    
#      _\_\,/_|    
#     (`\(_|`\|
#    (`\,)  \ \
#     \,)   | |    filter by Ethan Bloom
#       \__(__|    site by Mary Karroqe

from PIL import Image

def process():
	sticker = Image.open("images/bpb.png")
	img = Image.open("images/sample.png")
	size = img.size

	sticker = sticker.convert("RGBA")
	sticker = sticker.resize(size)

	img = img.convert("RGBA")

	new_img = Image.new("RGB", size)
	img.paste(sticker, (0, 0), sticker)
	new_img = img

	new_img.save("stickittoem.png","PNG")

	new_img.show()

process()