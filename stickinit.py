 
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

size = (1002, 720)
background = Image.open("images/sample.png")
overlay = Image.open("images/bpb.png")

print("yas")

new_img = Image.new("RGB", size)
background.paste(overlay, (0, 0), overlay)
new_img = background

print("yaaas")

new_img.save("stickittoem.png","PNG")
print("yaaaaAAAAAAS!!!!!")

new_img.show()

print("DONE")