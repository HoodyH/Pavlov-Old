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
COLOR_TOWERS = GRAY

COLOR_TOP_TITLE = LIGHT_GRAY2
COLOR_GRAPH_TITLE = LIGHT_GRAY
COLOR_TEXT = LIGHT_GRAY

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
    |             SPAN_GRAPH_TITLE            | span                |
    |                                         | span                |
    +--+-----------------------------------+--+                     |
    |  |          GRAPH_BORDER             |  | span    |           |
    |--+-----------------------------------+--|         |           |
    |  |                                   |  | span    |           |
    |  |          GRAPH                    |  | span    |           |
    |  |                                   |  | span    |SPAN_GRAPH |SPAN_GRAPH_SECTION
    |  |                                   |  | span    |           |
    |--+-----------------------------------+--|         |           |
    |  |          GRAPH_BORDER             |  | span    |           |
    +--+-----------------------------------+--+                     |
    |                                         | span                |
    |             SPAN_GRAPH_TEXT             | span                |
    |                                         | span                |
    |                                         | span                |
    +-----------------------------------------+
    |             SPAN_BORDER                 | span  
    +-----------------------------------------+                    


"""
# span border
SPAN_BORDER = 1
# span top title
SPAN_TOP_TITLE = 3
# end span top title
SPAN_TITLE_SECTION = SPAN_BORDER + SPAN_TOP_TITLE + SPAN_BORDER
SPAN_TITLE_SECTION_PIXELS = 250

# span graph section
SPAN_GRAPH_TITLE = 2

GRAPH_BORDER = 1
GRAPH = 4
SPAN_GRAPH = GRAPH_BORDER + GRAPH + GRAPH_BORDER

SPAN_GRAPH_TEXT = 4
# end span graph section
SPAN_GRAPH_SECTION = SPAN_GRAPH_TITLE + SPAN_GRAPH + SPAN_GRAPH_TEXT
SPAN_GRAPH_SECTION_PIXELS = 450


def draw_user_msg_stats(input_data, username):
    """
    :param input_data: is a dictionary with 'TITLE': data_array
    data_array is built as: [time_format, message_counter, time_spent_counter]
    time_format: is a printed value int os str
    message_counter: int
    time_spent_counter: int
    :param username: the name as str of the user of the data
    :return: image converted as byte array
    """
    granularity_sections = len(input_data.keys())

    width, height = (1000, SPAN_TITLE_SECTION_PIXELS + SPAN_GRAPH_SECTION_PIXELS*granularity_sections)

    span = height / (SPAN_TITLE_SECTION + SPAN_GRAPH_SECTION * granularity_sections + SPAN_BORDER)

    image = Image.new("RGB", (width, height), COLOR_BACKGROUND)
    draw = ImageDraw.Draw(image)

    def draw_text_in_center(x, y, text, fill=None, font=None, anchor=None):
        w, h = draw.textsize(text, font=font)
        draw.text([(x - w/2), (y - h/2)], text, fill=fill, font=font, anchor=anchor)

    def draw_graph(towers_data_array, section):
        number_of_towers = len(towers_data_array)
        if number_of_towers is 0:
            return
        subdivisions = 4 + number_of_towers + (number_of_towers/2 - 0.5) if number_of_towers > 1 else 0
        towers_x_dim = width / subdivisions
        tower_x_space_dim = towers_x_dim / 2
        side_x_border_dim = towers_x_dim * 2
        y = span*(SPAN_TITLE_SECTION + (SPAN_GRAPH_SECTION*section - SPAN_GRAPH_TEXT - GRAPH_BORDER))
        x = side_x_border_dim

        max_value_msg = 0
        for i in range(number_of_towers):
            if max_value_msg < towers_data_array[i][1]:
                max_value_msg = towers_data_array[i][1]

        for i in range(number_of_towers):
            tower_value = remap_range(towers_data_array[i][1], 0, max_value_msg, 0, span*GRAPH)
            draw.rectangle([(x, y), (x + towers_x_dim, y - tower_value)], fill=COLOR_TOWERS)
            draw_text_in_center(x+towers_x_dim/2, y+span/2, str(towers_data_array[i][0]), fill=COLOR_TEXT)
            draw_text_in_center(x+towers_x_dim/2, y-tower_value-GRAPH_BORDER*span/2, str(towers_data_array[i][1]), fill=COLOR_TEXT)
            x += towers_x_dim + tower_x_space_dim

    def draw_graph_section(towers_data_array, section_name, section):
        y = span*(SPAN_TITLE_SECTION + (SPAN_GRAPH_SECTION*section - SPAN_GRAPH_TEXT - SPAN_GRAPH))
        draw_text_in_center(width / 2, y - SPAN_GRAPH_TITLE * span / 2, section_name, font=font_graph_title, fill=COLOR_GRAPH_TITLE)
        draw_graph(towers_data_array, section)

    font_title = ImageFont.truetype('core/src/utils/fonts/helveticaneue-light.ttf', int(span * SPAN_TOP_TITLE))
    font_graph_title = ImageFont.truetype('core/src/utils/fonts/helveticaneue-light.ttf', int(span * SPAN_GRAPH_TITLE))

    y = span*SPAN_TITLE_SECTION
    title = '{}'.format(username)
    draw_text_in_center(width/2, y-SPAN_TITLE_SECTION*span/2, title, font=font_title, fill=COLOR_TOP_TITLE)

    section_counter = 1
    for key in input_data.keys():
        draw_graph_section(input_data.get(key), key, section_counter)
        section_counter += 1

    # convert the image in bytes to send it
    img_bytes = BytesIO()
    img_bytes.name = 'image.png'
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return img_bytes
