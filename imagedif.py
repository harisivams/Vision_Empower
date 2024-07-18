from PIL import Image, ImageChops,ImageStat

# assign images
img1 = Image.open("./static/upload/1.png")
img2 = Image.open("./static/upload/1.png")

# finding difference
diff = ImageChops.difference(img1, img2)

stat = ImageStat.Stat(diff)
diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)

res = diff_ratio * 100




