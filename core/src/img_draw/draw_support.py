from PIL import Image, ImageDraw


class DrawSupport(object):

    @staticmethod
    def create_image(color_type, width, height, background_color):
        return Image.new(color_type, (width, height), background_color)

    @staticmethod
    def create_draw(image):
        return ImageDraw.Draw(image)

    @staticmethod
    def draw_text_in_center(draw_obj, x, y, text, fill=None, font=None, anchor=None):
        """
        :param draw_obj: object where draw
        :param x: value of x entry point
        :param y: value of y entry point
        :param text: string of the name that you want to print
        :param fill: fill
        :param font: font
        :param anchor: value_printed
        """
        w, h = draw_obj.textsize(text, font=font)
        draw_obj.text([(x - w / 2), (y - h / 2)], text, fill=fill, font=font, anchor=anchor)

    @staticmethod
    def draw_multiline_text_in_center(draw_obj, x, y, text, fill=None, font=None, anchor=None, align=None):
        """
        :param draw_obj: object where draw
        :param x: value of x entry point
        :param y: value of y entry point
        :param text: string of the name that you want to print
        :param fill: fill
        :param font: font
        :param anchor: anchor
        :param align: align
        """
        w, h = draw_obj.textsize(text, font=font)
        draw_obj.multiline_text([(x - w / 2), (y - h / 2)], text, fill=fill, font=font, anchor=anchor, align=align)

    @staticmethod
    def draw_rectangle(draw_obj, x, y, x_2, y_2, fill=None):
        draw_obj.rectangle([(x, y), (x_2, y_2)], fill=fill)