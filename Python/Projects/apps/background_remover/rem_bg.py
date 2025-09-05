from rembg import remove
from PIL import Image
from pathlib import Path

path = Path(__file__).parent

input_image = path / ("initial.jpg")
output_image = path / ("final.png")

img = Image.open(input_image)

without_bg = remove(img)
without_bg.save(output_image)