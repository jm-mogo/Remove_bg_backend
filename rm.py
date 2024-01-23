from rembg import remove,new_session
from PIL import Image
model_name = "u2net_human_seg"
session = new_session(model_name)

input_path = 'pic.JPG'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input, session=session)
output.save(output_path)