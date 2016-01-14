 
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
#from flask import Flask, redirect, jsonify, render_template, request, send_file

def process():
	sticker = Image.open("images/bpb_sq.png")
	img = Image.open("images/sample2.jpg")

	sticker = sticker.convert("RGBA")
	img = img.convert("RGBA")

	# adds padding to make image square if it's not
	longer_side = max(img.size)
	horizontal_padding = (longer_side - img.size[0]) / 2
	vertical_padding = (longer_side - img.size[1]) / 2
	img = img.crop(
	    (
	        -horizontal_padding,
	        -vertical_padding,
	        img.size[0] + horizontal_padding,
	        img.size[1] + vertical_padding
	    )
	)

	size = img.size
	sticker = sticker.resize(size)

	img.paste(sticker, (0, 0), sticker)
	new_img = img

	new_img.save("stickittoem.jpg","JPEG")
	new_img.show()

process()





