class Line:

    """
    Description: A class is a text string and its attributes
    ----------

    Parameters:
        x0: The attribute describes the upper horizontal position of the symbol
        y0: The attribute describes the upper vertical position of the symbol
        x1: The attribute describes the lower horizontal position of the symbol
        y1: The attribute describes the lower vertical position of the symbol
        text: The attribute describes line text
        fontname: The attribute describes line Font
        size: The attribute describes line size
        no_change_font_name: Attribute describing that the font of the string has not changed
        no_change_text_size: Attribute describing that the size of the string has not changed
        page: The attribute describes the page on which the line is located
        chars: The attribute list of characters that make up the string

    """

    def __init__(self,x0,y0,x1,y1,text,fontname,size,no_change_font_name,no_change_text_size,page,chars):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.text = text
        self.fontname = fontname
        self.size = size
        self.no_change_font_name = no_change_font_name
        self.no_change_text_size = no_change_text_size
        self.page = page
        self.chars = chars

    @property
    def x0(self):
        return self._x0

    @x0.setter
    def x0(self, value):
        self._x0 = value

    @property
    def x1(self):
        return self._x1

    @property
    def y0(self):
        return self._y0

    @property
    def y1(self):
        return self._y1

    @property
    def text(self):
        return self._text

    @property
    def fontname(self):
        return self._fontname

    @property
    def size(self):
        return self._size

    @property
    def no_change_font_name(self):
        return self._no_change_font_name

    @property
    def no_change_text_size(self):
        return self._no_change_text_size

    @property
    def page(self):
        return self._page

    @property
    def chars(self):
        return self._chars

    @x1.setter
    def x1(self, value):
        self._x1 = value

    @y0.setter
    def y0(self, value):
        self._y0 = value

    @y1.setter
    def y1(self, value):
        self._y1 = value

    @text.setter
    def text(self, value):
        self._text = value

    @fontname.setter
    def fontname(self, value):
        self._fontname = value

    @size.setter
    def size(self, value):
        self._size = value

    @no_change_font_name.setter
    def no_change_font_name(self, value):
        self._no_change_font_name = value

    @no_change_text_size.setter
    def no_change_text_size(self, value):
        self._no_change_text_size = value

    @page.setter
    def page(self, value):
        self._page = value

    @chars.setter
    def chars(self, value):
        self._chars = value