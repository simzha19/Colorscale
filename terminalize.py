from PIL import Image
import os
import time


start_time = time.time()
os.getcwd()
os.chdir("Images/Original")

for entry in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), entry)):
        print(entry)
        im = Image.open(entry)
        grayscale_image = im.convert("L")
        
        output_image = Image.new("RGB", (grayscale_image.width, grayscale_image.height), "white")
        pixels = output_image.load()
        for i in range(output_image.width):
            for j in range(output_image.height):
                pixel = grayscale_image.getpixel((i, j))
                current_pixel = pixels[i, j]
                
                
                red = pixel * 166/284.162
                green = pixel * 226 / 284.162
                blue = pixel * 46 / 284.162
                
                pixels[i, j] = (int(red), int(green), int(blue))
        
        os.chdir("../Grayscale")
        grayscale_image.save(str(entry)+ "_greyscale.jpeg")
        os.chdir("../Colorscale")
        output_image.save(str(entry) + "_colorscale.jpeg")
                
print("--- %s seconds ---" % (time.time()-start_time))
