from PIL import Image, ImageDraw
import random
import os

red = (255, 0, 0)      # Red
blue = (0, 0, 255)     # Blue
yellow = (255, 255, 0) # Yellow
white = (255, 255, 255) # White
colors_dict={'red':red,'blue':blue,'yellow':yellow,'white':white}

# os.makedirs("random_color_images/red", exist_ok=True)

colors=[red,blue,yellow,white]

for i in range(100):
    image=Image.new("RGB", (300,300))
    draw = ImageDraw.Draw(image)
    center_x, center_y = 300 // 2, 300 // 2
    radius = random.randint(10,150)
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=yellow)#fill=random.choice(colors))
    image_path = os.path.join("random_color_images/yellow", f"image_{i}.png")
    image.save(image_path)

print("Images saved successfully.")