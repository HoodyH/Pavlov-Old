from core.src.utils.formatting import remap_range
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

GRAY = (105, 105, 105)
GRAY_BLUE = (180, 180, 255)
DARK_GRAY = (62, 62, 62)
LIGHT_GRAY = (180, 180, 180)
LIGHT_GRAY2 = (230, 230, 230)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

COLOR_BACKGROUND = DARK_GRAY
COLOR_TOWER_1 = GRAY
COLOR_TOWER_2 = GRAY_BLUE

COLOR_TOP_TITLE = LIGHT_GRAY2
COLOR_GRAPH_TITLE = LIGHT_GRAY
COLOR_TEXT = LIGHT_GRAY


class DrawLevel(object):

    def __init__(self):
        return


"""
    +-----------------------------------------+
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+         |
    |                                         | span    |
    |             SPAN_TOP_TITLE              | span    |SPAN_TITLE_SECTION
    |                                         | span    |
    +-----------------------------------------+         |
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+                
    |             SPAN_GRAPH_TITLE            | span                
    |                                         | span                
    +-----------------------------------------+                     
    |             SPAN_GRAPH_SUBTITLE         | span    |           
    +--+-----------------------------------+--+         |              
    |  |          GRAPH_BORDER             |  | span    |           
    |--+-----------------------------------+--|         |           
    |  |                                   |  | span    |           
    |  |          GRAPH                    |  | span    |SPAN_GRAPH 
    |  |                                   |  | span    |           
    |  |                                   |  | span    |           
    |--+-----------------------------------+--|         |           
    |  |          GRAPH_BORDER             |  | span    |           
    +--+-----------------------------------+--+                                         
    |                                         | span                
    |             SPAN_GRAPH_TEXT             | span                
    |                                         | span        
    |                                         | span                
    +-----------------------------------------+
    |             SPAN_BORDER                 | span  
    +-----------------------------------------+                      
"""
# span border
SPAN_BORDER = 1
# span top title
SPAN_TOP_TITLE = 2.5
# end span top title
SPAN_TITLE_SECTION = SPAN_BORDER + SPAN_TOP_TITLE + SPAN_BORDER
SPAN_TITLE_SECTION_PIXELS = 250

# span graph section
SPAN_GRAPH_TITLE = 2

SPAN_GRAPH_SUBTITLE = 1
GRAPH_BORDER = 1
GRAPH = 4
SPAN_GRAPH = SPAN_GRAPH_SUBTITLE + GRAPH_BORDER + GRAPH + GRAPH_BORDER

SPAN_GRAPH_TEXT = 4
# end span graph section
SPAN_GRAPH_PIXELS = 300
SPAN_GRAPH_SECTION_PIXELS = 150 + SPAN_GRAPH_PIXELS

"""
      B     T  TS T  T                                 
      O     O  OP O  O                                
      R     W  WA W  W
      D     E  EC E  E
      E     R  RE R  R
      R     A  B  A  B                                              
    +------+----------------------------------+------+
    |      |                                  |      |
    |------+----------------------------------+------|
    |      |   -                       -      |      | 
    |      |----     -                 -     -|      |
    |      |----  ----     -        ----  ----|      |
    |      |----  ----  ----  ----  ----  ----|      |
    |------+----------------------------------+------|
    |      |                                  |      | 
    +------+----------------------------------+------+
          

"""
BORDER_DIM = 2
TOWER_1_DIM = 0.75
TOWER_2_DIM = 0.25
SPACE_DIM = 0.25


class DrawImage(object):

    def __init__(self, data, username):

        """
        :param data: is a dictionary with 'TITLE': data_array
        data_array is built as: [[time_format_array], [message_counter_array], [time_spent_counter_array]]
        time_format_array: is a printed value int os str
        message_counter_array: int
        time_spent_counter_array: int
        :param username: the name as str of the user of the data
        """

        self.data = data
        self.username = username

        self.color_background = DARK_GRAY
        self.color_tower_1 = GRAY
        self.color_tower_2 = GRAY_BLUE
        self.color_top_title = LIGHT_GRAY2
        self.color_graph_title = LIGHT_GRAY
        self.color_text = LIGHT_GRAY

        n_sections = len(data.keys())
        self.width = 1200
        self.height = SPAN_TITLE_SECTION_PIXELS + SPAN_GRAPH_SECTION_PIXELS * n_sections

        self.image = Image.new("RGB", (self.width, self.height), COLOR_BACKGROUND)
        self.draw = ImageDraw.Draw(self.image)

        self.span_x = 0
        graph_section = SPAN_GRAPH_TITLE + SPAN_GRAPH * 2 + SPAN_GRAPH_TEXT
        self.span_y = self.height / (SPAN_TITLE_SECTION + graph_section * n_sections + SPAN_BORDER)

        dir_helvetica = 'core/src/utils/fonts/helveticaneue-light.ttf'
        self.font_title = ImageFont.truetype(dir_helvetica, int(self.span_y * SPAN_TOP_TITLE))
        self.font_graph_title = ImageFont.truetype(dir_helvetica, int(self.span_y * SPAN_GRAPH_TITLE))
        self.font_graph_subtitle = ImageFont.truetype(dir_helvetica, int(self.span_y * SPAN_GRAPH_SUBTITLE))
        self.font_graph_text = ImageFont.truetype(dir_helvetica, int(self.span_y * GRAPH_BORDER / 2))

    def __remap_values(self, data, max_value):
        value_array = []
        for el in data:
            value_array.append(remap_range(el, 0, max_value, 0, self.span_y * GRAPH))
        return value_array

    def __draw_text_in_center(self, x, y, text, fill=None, font=None, anchor=None):
        """
        :param x: value of x entry point
        :param y: value of y entry point
        :param text: string of the name that you want to print
        :param fill: fill
        :param font: font
        :param anchor: anchor
        """
        w, h = self.draw.textsize(text, font=font)
        self.draw.text([(x - w/2), (y - h/2)], text, fill=fill, font=font, anchor=anchor)

    def __draw_towers_names(self, x, y, tower_dim, space, data, font):
        """
        :param x: value of x entry point
        :param y: value of y entry point
        :param tower_dim: value of the global definition for the tower
        :param space: distance between 2 elements
        :param data: string of the name that you want to print
        :param font: font
        """
        for el in data:
            entry_x = x + self.span_x * tower_dim / 2
            entry_y = y + self.span_y / 2
            self.__draw_text_in_center(entry_x, entry_y, str(el), fill=self.color_text, font=font)

            x += self.span_x * tower_dim + self.span_x * space

    def __draw_towers_value_on_top(self, x, y, tower_dim, space, value, data, font):

        for i in range(len(data)):
            if data[i] is not 0:
                entry_x = x + self.span_x * tower_dim / 2
                entry_y = y - value[i] - GRAPH_BORDER * self.span_y / 2
                self.__draw_text_in_center(entry_x, entry_y, str(data[i]), fill=self.color_text, font=font)

            x += self.span_x * tower_dim + self.span_x * space

    def __draw_towers(self, x, y, tower_dim, space, tower_color, value):

        for el in value:
            x_2 = x + self.span_x * tower_dim
            y_2 = y - el
            self.draw.rectangle([(x, y), (x_2, y_2)], fill=tower_color)

            x += self.span_x * tower_dim + self.span_x * space

    def __draw_graph_multi_tower(self, towers_name_array, towers_data_array, section, sub_section):

        n_towers = len(towers_data_array)
        if n_towers is 0:
            return

        graph_subsection = (SPAN_GRAPH_TITLE + SPAN_GRAPH * sub_section + SPAN_GRAPH_TEXT) * section

        rm = SPAN_GRAPH_TEXT + SPAN_GRAPH + SPAN_GRAPH_SUBTITLE
        y = self.span_y * (SPAN_TITLE_SECTION + graph_subsection - rm)
        self.__draw_text_in_center(
            self.width / 2,
            y - SPAN_GRAPH_SUBTITLE * self.span_y / 2,
            "name_here",
            font=self.font_graph_subtitle,
            fill=COLOR_GRAPH_TITLE)

        y = self.span_y * (SPAN_TITLE_SECTION + graph_subsection - SPAN_GRAPH_TEXT - GRAPH_BORDER)

        border_subdivision = BORDER_DIM * 2
        tower_subdivision = n_towers * TOWER_1_DIM
        space_subdivision = (n_towers * SPACE_DIM - SPACE_DIM) if n_towers > 1 else 0
        self.span_x = self.width / (border_subdivision + tower_subdivision + space_subdivision)
        x = self.span_x * BORDER_DIM

        max_1 = max(towers_data_array[1])
        max_2 = max(towers_data_array[2])
        max_value = max_1 if max_1 > max_2 else max_2

        dim = TOWER_1_DIM + TOWER_2_DIM
        self.__draw_towers_names(
            x, y, dim, SPACE_DIM, towers_data_array[0], self.font_graph_text
        )

        space = SPACE_DIM + TOWER_2_DIM
        value = self.__remap_values(towers_data_array[1], max_value)
        self.__draw_towers(
            x, y, TOWER_1_DIM, space, self.color_tower_1, value
        )
        self.__draw_towers_value_on_top(
            x, y, TOWER_1_DIM, space, value, towers_data_array[1], self.font_graph_text
        )

        x += self.span_x * TOWER_1_DIM
        space = SPACE_DIM + TOWER_1_DIM
        value = self.__remap_values(towers_data_array[2], max_value)
        self.__draw_towers(
            x, y, TOWER_2_DIM, space, self.color_tower_2, value
        )
        self.__draw_towers_value_on_top(
            x, y, TOWER_2_DIM, space, value, towers_data_array[2], self.font_graph_text
        )

    def __draw_graph(self, towers_name_array, towers_data_array, section, sub_section):

        n_towers = len(towers_data_array)
        if n_towers is 0:
            return

        graph_subsection = (SPAN_GRAPH_TITLE + SPAN_GRAPH * sub_section + SPAN_GRAPH_TEXT) * section

        rm = SPAN_GRAPH_TEXT + SPAN_GRAPH + SPAN_GRAPH_SUBTITLE
        y = self.span_y * (SPAN_TITLE_SECTION + graph_subsection - rm)
        self.__draw_text_in_center(
            self.width / 2,
            y - SPAN_GRAPH_SUBTITLE * self.span_y / 2,
            "name_here",
            font=self.font_graph_subtitle,
            fill=COLOR_GRAPH_TITLE)

        y = self.span_y * (SPAN_TITLE_SECTION + graph_subsection - SPAN_GRAPH_TEXT - GRAPH_BORDER)

        border_subdivision = BORDER_DIM * 2
        tower_subdivision = n_towers * TOWER_1_DIM
        space_subdivision = (n_towers * SPACE_DIM - SPACE_DIM) if n_towers > 1 else 0
        self.span_x = self.width / (border_subdivision + tower_subdivision + space_subdivision)
        x = self.span_x * BORDER_DIM

        max_value = max(towers_data_array)

        self.__draw_towers_names(
            x, y, TOWER_1_DIM, SPACE_DIM, towers_name_array, self.font_graph_text
        )
        value = self.__remap_values(towers_data_array, max_value)
        self.__draw_towers(
            x, y, TOWER_1_DIM, SPACE_DIM, self.color_tower_1, value
        )
        self.__draw_towers_value_on_top(
            x, y, TOWER_1_DIM, SPACE_DIM, value, towers_data_array, self.font_graph_text
        )

    def __draw_graph_section(self, towers_data_array, section, section_name):

        n_subsections = 1

        graph_section = (SPAN_GRAPH_TITLE + SPAN_GRAPH * n_subsections + SPAN_GRAPH_TEXT) * section
        rm = SPAN_GRAPH_TEXT + SPAN_GRAPH * n_subsections
        y = self.span_y * (SPAN_TITLE_SECTION + graph_section - rm)
        self.__draw_text_in_center(
            self.width / 2,
            y - SPAN_GRAPH_TITLE * self.span_y / 2,
            section_name,
            font=self.font_graph_title,
            fill=COLOR_GRAPH_TITLE)

        self.__draw_graph_multi_tower(towers_data_array, towers_data_array, section, 1)

    def draw_msg_stats(self):

        y = self.span_y * SPAN_TITLE_SECTION
        self.__draw_text_in_center(
            self.width / 2,
            y - SPAN_TITLE_SECTION * self.span_y / 2,
            '{}'.format(self.username),
            font=self.font_title,
            fill=COLOR_TOP_TITLE)

        section_counter = 1
        for key in self.data.keys():
            self.__draw_graph_section(self.data.get(key), section_counter, key)
            section_counter += 1

    def get_image(self):

        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'image.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes
