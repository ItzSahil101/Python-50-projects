from PIL import Image, ImageDraw, ImageFont

txt = input("Enter Any Text: ")

img = Image.new("RGB", (800, 400), color=(255, 255, 255))
d = ImageDraw.Draw(img)

font = ImageFont.load_default()

d.text((50, 50), txt, font=font, fill=(0, 0, 0))
img.save("demo.png")
print("END")
