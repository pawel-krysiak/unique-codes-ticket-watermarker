from PIL import Image, ImageDraw, ImageFont

class PictureWatermarker:
    # Watermark given picture with any text

    def __init__(self):
        # self.font = ImageFont.truetype("SignPainter.ttf", 85)
        # self.font = ImageFont.truetype("CODE_Bold.otf", 55)
        self.font = ImageFont.truetype("Oswald-Medium.ttf", 55)

    def __process_image(self, file_path, watermark):
        # Watermark picture with number
        main = Image.open(file_path)
        watermark_layer = Image.new("RGBA", main.size)
        waterdraw = ImageDraw.ImageDraw(watermark_layer, "RGBA")
        waterdraw.text((40, 40), watermark, font=self.font)
        main.paste(watermark_layer, None, watermark_layer)
        main.save("export/image-" + watermark + '.jpg' , "JPEG")

    def watermark_picture(self, file_path, watermark):
        self.__process_image(file_path, watermark)
        print "Processed image: " + "image-" + watermark + '.jpg'
