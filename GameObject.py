class GameObject():
    """A basic game object"""
    def __init__(self,x,y,character,main_colour):
        """
        Initialize a game object
        :param character: The single character to use
        :param main_colour: Main colour to use in the foreground.
        """
        self.character=character
        self.main_colour=main_colour
        self.walkable=False
        self.transparent=False
        self.x=x
        self.y=y


    def isWalkable(self):
        return self.walkable


    def isTransparent(self):
        return self.transparent

    def set_position(self,x,y):
        self.x=x
        self.y=y

    def draw(self,con):
        con.draw_char(self.x,self.y,self.character,self.main_colour)
