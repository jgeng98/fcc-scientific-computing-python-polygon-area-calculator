class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={width}, height={height})".format(
            width=self.width, height=self.height
        )

    def set_width(self, new_width):
        self.width = new_width

    def sef_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture"

        picture = ["*" * self.width + "\n" for i in range(self.height)]

        return "".join(picture)

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)

    def __str__(self):
        return "Square(side={side_length})".format(side_length=self.width)

    def set_side(self, new_side_length):
        self.height = new_side_length
        self.width = new_side_length
