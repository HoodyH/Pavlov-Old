from core.src.settings import (
    DEFAULT_BACKGROUND_COLOR, DEFAULT_LEVEL_COLOR, DEFAULT_TEXT_COLOR,
    DIR_DEFAULT_FONT,
    DEFAULT_BACKGROUND_BAR_COLOR, DEFAULT_BAR_COLOR, DEFAULT_XP_INSIDE_DARK_COLOR, DEFAULT_XP_INSIDE_LIGHT_COLOR
)
from PIL import ImageFont
from io import BytesIO
from math import ceil
from core.src.utils.internal_formatting import remap_range
from core.src.img_draw.draw_support import DrawSupport
draw_support = DrawSupport()


class DrawLevelSupport(object):

    def __init__(self):

        self.y_resolution = 30
        self.x_resolution = 25
    """    
    def draw_xp_bar(self, y, x_start, x_end, current_xp, total_xp_level, bar_background_color, bar_color):
       
        border_offset = self.x_resolution*DIM_OFFSET
        x_1 = border_offset
        x_max = self.width - border_offset
        x_2 = remap_range(current_xp, 0, total_xp_level, x_1, x_max)

        y_1 = y - SPAN_BAR*self.y_resolution/2
        y_2 = y + SPAN_BAR*self.y_resolution/2

        draw_support.draw_rectangle(self.draw, x_1, y_1, x_max, y_2, fill=bar_background_color)
        draw_support.draw_rectangle(self.draw, x_1, y_1, x_2, y_2, fill=bar_color)

        text_xp_inside = ' {} XP'.format(current_xp)
        w, h = draw_support.get_text_dimension(self.draw, text_xp_inside, font=self.font_xp_inside)
        if (x_2 - x_1) > w:
            _origin_x = 'left'
            _fill = bar_background_color
        else:
            _origin_x = 'right'
            _fill = bar_color

        draw_support.draw_text(
            self.draw,
            x_2,
            self.y_cursor,
            text_xp_inside,
            font=self.font_xp_inside,
            fill=_fill,
            origin_x=_origin_x,
        )

        _y_cursor_temp = self.y_cursor + (SPAN_BAR/2 + SPAN_XP_VALUES/2)*self.y_resolution

        draw_support.draw_text(
            self.draw,
            self.width - border_offset,
            _y_cursor_temp,
            '{} / {} XP'.format(current_xp, total_xp_level),
            font=self.font_xp_values,
            fill=self.text_color,
            origin_x='left',
        )
        
    def draw_level(self):
        return " he"
"""


example_level_up = {
    'background_color': (62, 62, 62),
    'level': '10',
    'level_color': (230, 230, 230),
    'title': 'Congratulations User',
    'title_color': (180, 180, 180),
    'text': 'You have gained a level',
    'text_color': (180, 180, 180),
}

"""                   
    +-----------------------------------------+  
    |              SPAN_BORDER                | span  |              
    +-----------------------------------------+       |                               
    |                                         | span  |                          
    |              SPAN_LEVEL                 | span  |  SPAN_LEVEL_SECTION                        
    |                                         | span  |                                                  
    +-----------------------------------------+       | 
    |              SPAN_BORDER                | span  | 
    +-----------------------------------------+                            
    |              SPAN_BOLD_TEXT             | span  
    |                                         | span                             
    +-----------------------------------------+            
    |              SPAN_TEXT                  | span                         
    +-----------------------------------------+     
    |              SPAN_BORDER                | span     at the end of all                        
    +-----------------------------------------+        
"""
SPAN_BORDER = 0.3
SPAN_LEVEL = 2
SPAN_BOLD_TEXT = 1
SPAN_TEXT = 1

SPAN_LEVEL_SECTION = SPAN_BORDER + SPAN_LEVEL + SPAN_BORDER


class DrawLevelUp(object):

    def __init__(self, data):

        """
        :param data: is a dictionary look the documentation on the top of this file:
        """

        self.data = data

        self.y_resolution = 30
        self.width = 350
        self.height = 0

        self.level = str(self.data.get('level', False))
        if self.level is not False:
            self.height += SPAN_LEVEL_SECTION * self.y_resolution
        self.level_color = self.data.get('level_color', DEFAULT_LEVEL_COLOR)

        self.title = self.data.get('title', False)
        if self.title is not False:
            self.height += SPAN_BOLD_TEXT * self.y_resolution
        self.title_color = self.data.get('title_color', DEFAULT_LEVEL_COLOR)

        # add space for SPAN_TEXT
        self.text = self.data.get('text', False)
        if self.text is not False:
            self.text_lines = self.text.count('\n') + 1
            self.height += SPAN_TEXT * self.text_lines * self.y_resolution
        self.text_color = self.data.get('text_color', DEFAULT_TEXT_COLOR)

        self.height += SPAN_BORDER * self.y_resolution

        self.height = ceil(self.height)
        background_color = self.data.get('background_color', DEFAULT_BACKGROUND_COLOR)
        self.image = draw_support.create_image("RGB", self.width, self.height, background_color)
        self.draw = draw_support.create_draw(self.image)

        self.y_cursor = 0

        self.font_dir = self.data.get('font', DIR_DEFAULT_FONT)
        self.font_level = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_LEVEL))
        self.font_title = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_BOLD_TEXT / 1.3))
        self.font_text = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_TEXT / 2))

    def draw_level_up(self):

        if self.level is not False:
            self.y_cursor += (SPAN_LEVEL_SECTION / 2) * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.level,
                font=self.font_level,
                fill=self.level_color
            )
            self.y_cursor += (SPAN_LEVEL_SECTION / 2) * self.y_resolution

        if self.title is not False:
            self.y_cursor += (SPAN_BOLD_TEXT / 2) * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.title,
                font=self.font_title,
                fill=self.title_color
            )
            self.y_cursor += (SPAN_BOLD_TEXT / 2) * self.y_resolution

        if self.text is not False:
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution
            draw_support.draw_multiline_text_in_center(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.text,
                font=self.font_text,
                fill=self.text_color,
                align='center'
            )
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution

    def get_image(self):

        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'level_up.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes

    def save_image(self, file_dir):
        self.image.save(file_dir, format='PNG')


example_level_card = {
    'background_color': (62, 62, 62),
    'username': 'Congratulations User',
    'username_color': (180, 180, 180),
    'data': {
        'rank': 'N/D',
        'rank_label': 'RANK',
        'rank_color': (230, 230, 230),
        'level': '10',
        'level_label': 'LEVEL',
        'level_color': (230, 230, 230),
    },
    'bar': {
        'value': '2341',
        'max': '8000',
        'bar_color': (230, 230, 230),
        'bar_background_color': (230, 230, 230),
        'inside_xp_dark_color': (230, 230, 230),
        'inside_xp_light_color': (230, 230, 230),
    },
    'text': 'Cool keep going like that',
    'text_color': (180, 180, 180),
}

"""                   
    +-----------------------------------------+  
    |              SPAN_BORDER                | span  |              
    +-----------------------------------------+       |                               
    |              SPAN_USERNAME              | span  |  SPAN_USERNAME_SECTION                         
    |                                         | span  |                                                                    
    +-----------------------------------------+       | 
    |              SPAN_BORDER                | span  | 
    +-----------------------------------------+                            
    |              SPAN_DATA                  | span  
    |                                         | span   
    +-----------------------------------------+            
    |              SPAN_XP_VALUES             | span  |                         
    +--+-----------------------------------+--+       |     
    |  |           SPAN_BAR                |  | span  |  SPAN_BAR_SECTION                     
    +--+-----------------------------------+--+       |
    |              SPAN_XP_VALUES             | span  |
    +-----------------------------------------+  
    |              SPAN_TEXT                  | span                         
    +-----------------------------------------+  
    |              SPAN_BORDER                | span     at the end of all                        
    +-----------------------------------------+        
"""
SPAN_BORDER = 0.3
SPAN_USERNAME = 1.6
SPAN_DATA = 1
SPAN_BAR = 0.8
SPAN_XP_VALUES = 0.6

SPAN_USERNAME_SECTION = SPAN_BORDER + SPAN_USERNAME + SPAN_BORDER
SPAN_BAR_SECTION = SPAN_XP_VALUES + SPAN_BAR + SPAN_XP_VALUES


class DrawLevelCard(object):

    def __init__(self, data):

        """
        :param data: is a dictionary look the documentation on the top of this file:
        """

        self.data = data

        self.y_resolution = 30
        self.width = 350
        self.x_border_offset = 25
        self.height = 0

        self.username = str(self.data.get('username', False))
        if self.username is not False:
            # reserve the space
            self.height += SPAN_USERNAME_SECTION * self.y_resolution
            # get values
            self.username_color = self.data.get('username_color', DEFAULT_TEXT_COLOR)

        self.data_section = self.data.get('data', False)
        if self.data_section is not False:
            # reserve the space
            self.height += SPAN_DATA * self.y_resolution
            # get values
            self.rank = self.data_section.get('rank', False)
            self.rank_label = self.data_section.get('rank_label', False)
            self.rank_color = self.data_section.get('rank_color', DEFAULT_TEXT_COLOR)
            self.level = self.data_section.get('level', False)
            self.level_label = self.data_section.get('level_label', False)
            self.level_color = self.data_section.get('level_color', DEFAULT_TEXT_COLOR)

        # add space for SPAN_BAR
        self.bar_section = self.data.get('bar', False)
        if self.bar_section is not False:
            # reserve the space
            self.height += SPAN_BAR_SECTION * self.y_resolution
            # get values
            self.bar_value = self.bar_section.get('value', False)
            self.bar_max = self.bar_section.get('max', False)
            self.bar_color = self.bar_section.get('bar_color', DEFAULT_BAR_COLOR)
            self.bar_background_color = self.bar_section.get('bar_background_color', DEFAULT_BACKGROUND_BAR_COLOR)
            self.inside_xp_dark_color = self.bar_section.get('inside_xp_dark_color', DEFAULT_XP_INSIDE_DARK_COLOR)
            self.inside_xp_light_color = self.bar_section.get('inside_xp_light_color', DEFAULT_XP_INSIDE_LIGHT_COLOR)

        # add space for SPAN_TEXT
        self.text = self.data.get('text', False)
        if self.text is not False:
            # the line of text will be added based on the line terminator
            self.text_lines = self.text.count('\n') + 1
            # reserve the space
            self.height += SPAN_TEXT * self.text_lines * self.y_resolution

        self.text_color = self.data.get('text_color', DEFAULT_TEXT_COLOR)

        # last border in the end
        # reserve the space
        self.height += SPAN_BORDER * self.y_resolution

        # prepare the canvas
        # ceil the value to from float to decimal value, cause the img creation need int
        self.height = ceil(self.height)
        background_color = self.data.get('background_color', DEFAULT_BACKGROUND_COLOR)
        self.image = draw_support.create_image("RGB", self.width, self.height, background_color)
        self.draw = draw_support.create_draw(self.image)

        self.y_cursor = 0

        # prepare dynamic fonts dimensions
        self.font_dir = self.data.get('font', DIR_DEFAULT_FONT)

        self.font_username = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_USERNAME / 1.4))
        self.font_data_value = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_DATA / 1.2))
        self.font_data_label = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_DATA / 2.2))
        self.font_xp_inside = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_BAR / 1.6))
        self.font_xp_values = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_XP_VALUES / 1.2))
        self.font_text = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_TEXT / 2))

    def draw_xp_bar(self, y, current_xp, total_xp_level):
        """
        draw shadow frame of the xp bar
        draw the real xp bar
        draw the xp values
        """
        x_1 = self.x_border_offset
        x_max = self.width - self.x_border_offset
        x_2 = remap_range(current_xp, 0, total_xp_level, x_1, x_max)

        y_1 = y - SPAN_BAR*self.y_resolution/2
        y_2 = y + SPAN_BAR*self.y_resolution/2

        draw_support.draw_rectangle(self.draw, x_1, y_1, x_max, y_2, fill=self.bar_background_color)
        draw_support.draw_rectangle(self.draw, x_1, y_1, x_2, y_2, fill=self.bar_color)

        text_xp_inside = ' {} XP'.format(current_xp)
        w, h = draw_support.get_text_dimension(self.draw, text_xp_inside, font=self.font_xp_inside)
        if (x_2 - x_1) > w:
            _origin_x = 'left'
            _fill = self.inside_xp_dark_color
        else:
            _origin_x = 'right'
            _fill = self.inside_xp_light_color

        draw_support.draw_text(
            self.draw,
            x_2,
            self.y_cursor,
            text_xp_inside,
            font=self.font_xp_inside,
            fill=_fill,
            origin_x=_origin_x,
        )

        _y_cursor_temp = self.y_cursor + (SPAN_BAR/2 + SPAN_XP_VALUES/2)*self.y_resolution

        draw_support.draw_text(
            self.draw,
            self.width - self.x_border_offset,
            _y_cursor_temp,
            '{} / {} XP'.format(current_xp, total_xp_level),
            font=self.font_xp_values,
            fill=self.text_color,
            origin_x='left',
        )

    def draw_data_section(self):

        if self.rank is not False:
            draw_support.draw_text(
                self.draw,
                self.x_border_offset,
                self.y_cursor,
                self.rank_label,
                font=self.font_data_label,
                fill=self.rank_color,
                origin_x='right',
                origin_y='up'
            )
            w, h = draw_support.get_text_dimension(self.draw, str(self.rank_label), font=self.font_data_label)
            draw_support.draw_text(
                self.draw,
                self.x_border_offset + w,
                self.y_cursor,
                ' #{}'.format(self.rank),
                font=self.font_data_value,
                fill=self.rank_color,
                origin_x='right',
                origin_y='up'
            )

        if self.level is not False:
            draw_support.draw_text(
                self.draw,
                self.width - self.x_border_offset,
                self.y_cursor,
                '{}'.format(self.level),
                font=self.font_data_value,
                fill=self.level_color,
                origin_x='left',
                origin_y='up'
            )
            w, h = draw_support.get_text_dimension(self.draw, str(self.level), font=self.font_data_value)
            draw_support.draw_text(
                self.draw,
                self.width - (self.x_border_offset + w),
                self.y_cursor,
                '{} '.format(self.level_label),
                font=self.font_data_label,
                fill=self.level_color,
                origin_x='left',
                origin_y='up'
            )

    def draw_level_card(self):

        if self.username is not False:
            self.y_cursor += (SPAN_USERNAME_SECTION / 2) * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.username,
                font=self.font_username,
                fill=self.level_color
            )
            self.y_cursor += (SPAN_USERNAME_SECTION / 2) * self.y_resolution

        if self.data_section is not False:
            self.y_cursor += SPAN_DATA * self.y_resolution
            self.draw_data_section()
            # self.y_cursor += (SPAN_DATA / 2) * self.y_resolution

        if self.bar_section is not False:
            self.y_cursor += (SPAN_BAR_SECTION / 2) * self.y_resolution
            self.draw_xp_bar(
                self.y_cursor,
                current_xp=self.bar_value,
                total_xp_level=self.bar_max
            )
            self.y_cursor += (SPAN_BAR_SECTION / 2) * self.y_resolution

        if self.text is not False:
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution
            draw_support.draw_multiline_text_in_center(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.text,
                font=self.font_text,
                fill=self.text_color,
                align='center'
            )
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution

    def get_image(self):

        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'level_up.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes

    def save_image(self, file_dir):
        self.image.save(file_dir, format='PNG')


example_level_rank = {
    'background_color': (62, 62, 62),
    'title': 'Ranking of most Active Users',
    'title_color': (180, 180, 180),
    'rank': {
        '1': {
            'username': 'Username',
            'highlights': True,
            'rank_color': (230, 230, 230),
            'level': '10',
            'level_label': 'LEVEL',
            'level_color': (230, 230, 230),
            'value': '2341',
            'max': '8000',
            'bar_color': (230, 230, 230),
            'bar_background_color': (230, 230, 230),
            'inside_xp_dark_color': (230, 230, 230),
            'inside_xp_light_color': (230, 230, 230),
        },
    },
    'text': 'Cool keep going like that',
    'text_color': (180, 180, 180),
}

"""                   
    +-----------------------------------------+  
    |              SPAN_BORDER                | span  |              
    +-----------------------------------------+       |                               
    |              SPAN_TITLE                 | span  |  SPAN_TITLE_SECTION                         
    |                                         | span  |                                                                    
    +-----------------------------------------+       | 
    |              SPAN_BORDER                | span  |                         
    +-----------------------------------------+            
    |                                         | span  |                         
    |              SPAN_RANK                  |       |    
    |                                         | span  |  SPAN_RANK_SECTION                     
    +-----------------------------------------+       |
    |              SPAN_SEPARATOR             | span  |    
    +-----------------------------------------+  
    |              SPAN_TEXT                  | span                         
    +-----------------------------------------+  
    |              SPAN_BORDER                | span     at the end of all                        
    +-----------------------------------------+        

"""

SPAN_BORDER = 0.3
SPAN_TITLE = 1.6
SPAN_RANK = 0.8
SPAN_SEPARATOR = 0.8

SPAN_TITLE_SECTION = SPAN_BORDER + SPAN_TITLE + SPAN_BORDER
SPAN_RANK_SECTION = SPAN_RANK + SPAN_SEPARATOR

"""
        +-+------+--------------------+---------------------+-+----------+-+            
        | |      |                    |                     | |          | |                      
   +--> | | RANK |      USERNAME      |    XP_BAR           | | LEVEL    | |      
   |    | |      |                    |                     | |          | |                   
   |    +-+------+--------------------+---------------------+-+----------+-+
OFFSET

"""
DIM_OFFSET = 0.5
DIM_RANK = 1.5
DIM_USERNAME = 8
DIM_XP_BAR = 6
DIM_LEVEL = 4


class DrawRanking(object):

    def __init__(self, data):

        """
        :param data: is a dictionary look the documentation on the top of this file:
        """

        self.data = data

        self.y_resolution = 30
        self.x_resolution = 30
        self.width = (DIM_OFFSET+DIM_RANK+DIM_USERNAME+DIM_XP_BAR+DIM_OFFSET+DIM_LEVEL+DIM_OFFSET)*self.x_resolution
        self.height = 0

        self.title = str(self.data.get('title', False))
        if self.title is not False:
            # reserve the space
            self.height += SPAN_TITLE_SECTION * self.y_resolution
            # get values
            self.title_color = self.data.get('title_color', DEFAULT_TEXT_COLOR)

        self.rank_sections = []
        sections = self.data.get('rank', False)
        if sections is not False:
            # extract the sections and put them into an array
            for key in sections.keys():
                self.rank_sections.append(sections.get(key))
            # reserve the space
            self.height += SPAN_RANK_SECTION * self.y_resolution * len(self.rank_sections)

        # add space for SPAN_TEXT
        self.text = self.data.get('text', False)
        if self.text is not False:
            # the line of text will be added based on the line terminator
            self.text_lines = self.text.count('\n') + 1
            # reserve the space
            self.height += SPAN_TEXT * self.text_lines * self.y_resolution
            self.text_color = self.data.get('text_color', DEFAULT_TEXT_COLOR)

        # last border in the end
        # reserve the space
        self.height += SPAN_BORDER * self.y_resolution

        # prepare the canvas
        # ceil the value to from float to decimal value, cause the img creation need int
        self.height = ceil(self.height)
        self.width = ceil(self.width)
        background_color = self.data.get('background_color', DEFAULT_BACKGROUND_COLOR)
        self.image = draw_support.create_image("RGB", self.width, self.height, background_color)
        self.draw = draw_support.create_draw(self.image)

        self.y_cursor = 0

        # prepare dynamic fonts dimensions
        self.font_dir = self.data.get('font', DIR_DEFAULT_FONT)

        self.font_username = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_USERNAME / 1.4))
        self.font_data_value = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_DATA / 1.2))
        self.font_data_label = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_DATA / 2.2))
        self.font_xp_inside = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_BAR / 1.6))
        self.font_xp_values = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_BORDER * 1.6))
        self.font_text = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_TEXT / 2))

    def draw_xp_bar(self, y, x_start, x_end, current_xp, total_xp_level, bar_background_color, bar_color):
        """
        draw shadow frame of the xp bar
        draw the real xp bar
        draw the xp values
        """
        bar_dim_pixels = SPAN_RANK*self.y_resolution

        x_1 = x_start
        x_max = x_end
        x_2 = remap_range(current_xp, 0, total_xp_level, x_1, x_max)

        y_1 = y - bar_dim_pixels
        y_2 = y

        draw_support.draw_rectangle(self.draw, x_1, y_1, x_max, y_2, fill=bar_background_color)
        draw_support.draw_rectangle(self.draw, x_1, y_1, x_2, y_2, fill=bar_color)

        text_xp_inside = ' {} XP'.format(current_xp)
        w, h = draw_support.get_text_dimension(self.draw, text_xp_inside, font=self.font_xp_inside)
        if (x_2 - x_1) > w:
            _origin_x = 'left'
            _fill = bar_background_color
        else:
            _origin_x = 'right'
            _fill = bar_color

        draw_support.draw_text(
            self.draw,
            x_2,
            self.y_cursor - bar_dim_pixels/2,
            text_xp_inside,
            font=self.font_xp_inside,
            fill=_fill,
            origin_x=_origin_x,
        )

        _y_cursor_temp = self.y_cursor + SPAN_BORDER/1.9*self.y_resolution

        draw_support.draw_text(
            self.draw,
            x_max,
            y + self.y_resolution/4,
            '{} / {} XP'.format(current_xp, total_xp_level),
            font=self.font_xp_values,
            fill=self.text_color,
            origin_x='left',
        )

    def draw_rank_section(self, data):

        username = data.get('username', 'Anonymous')
        highlights = data.get('highlights', False)
        rank = data.get('rank', False)
        rank_label = data.get('rank_label', False)
        rank_color = data.get('rank_color', DEFAULT_TEXT_COLOR)
        level = data.get('level', False)
        level_label = data.get('level_label', False)
        level_color = data.get('level_color', DEFAULT_TEXT_COLOR)
        bar_value = data.get('value', False)
        bar_max = data.get('max', False)
        bar_color = data.get('color', DEFAULT_BAR_COLOR)
        bar_background_color = data.get('background_color', DEFAULT_BACKGROUND_BAR_COLOR)

        x_cursor = self.x_resolution*DIM_OFFSET

        if rank is not False:
            draw_support.draw_text(
                self.draw,
                x_cursor,
                self.y_cursor,
                ' #{}'.format(rank),
                font=self.font_data_value,
                fill=rank_color,
                origin_x='right',
                origin_y='up'
            )
        x_cursor += DIM_RANK * self.x_resolution

        if username is not False:
            draw_support.draw_text(
                self.draw,
                x_cursor,
                self.y_cursor,
                username,
                font=self.font_data_value,
                fill=rank_color,
                origin_x='right',
                origin_y='up'
            )
        x_cursor += DIM_USERNAME * self.x_resolution

        if bar_value is not False:
            self.draw_xp_bar(
                self.y_cursor,
                x_cursor,
                x_cursor + DIM_XP_BAR * self.x_resolution,
                current_xp=bar_value,
                total_xp_level=bar_max,
                bar_color=bar_color,
                bar_background_color=bar_background_color

            )
        x_cursor += DIM_XP_BAR * self.x_resolution
        x_cursor += self.x_resolution * DIM_OFFSET

        if level is not False:
            draw_support.draw_text(
                self.draw,
                x_cursor,
                self.y_cursor,
                '{}'.format(level_label),
                font=self.font_data_label,
                fill=level_color,
                origin_x='right',
                origin_y='up'
            )
            w, h = draw_support.get_text_dimension(self.draw, str(level_label), font=self.font_data_label)
            draw_support.draw_text(
                self.draw,
                x_cursor + w,
                self.y_cursor,
                ' {}'.format(level),
                font=self.font_data_value,
                fill=level_color,
                origin_x='right',
                origin_y='up'

            )

    def draw_ranking(self):

        if self.title is not False:
            self.y_cursor += (SPAN_TITLE_SECTION / 2) * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.title,
                font=self.font_username,
                fill=self.title_color
            )
            self.y_cursor += (SPAN_TITLE_SECTION / 2) * self.y_resolution

        if self.rank_sections is not []:
            for el in self.rank_sections:
                self.y_cursor += SPAN_RANK * self.y_resolution
                self.draw_rank_section(el)
                self.y_cursor += SPAN_SEPARATOR * self.y_resolution

        if self.text is not False:
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution
            draw_support.draw_multiline_text_in_center(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.text,
                font=self.font_text,
                fill=self.text_color,
                align='center'
            )
            self.y_cursor += (SPAN_TEXT * self.text_lines / 2) * self.y_resolution

    def get_image(self):

        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'level_up.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes

    def save_image(self, file_dir):
        self.image.save(file_dir, format='PNG')
