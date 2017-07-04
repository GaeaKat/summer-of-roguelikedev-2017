import tdl
import itertools

class Tile():
    """A tile on the map"""

    def __init__(self):
        self.walkable = True
        self.transparent = True

    def isWalkable(self):
        return self.walkable

    def isTransparent(self):
        return self.transparent


class Wall(Tile):
    "A wall on the map"

    def __init__(self):
        super().__init__()
        self.walkable = False
        self.transparent = False


class Map():
    """A basic map, will contain the tdl map amongst other things"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tdl_map = tdl.map.Map(width, height)
        self.floor = [[Tile() for y in range(height)] for x in range(width)]
        self.objects = [[None for y in range(height)] for x in range(width)]
        self.color_dark_wall = (0, 0, 100)
        self.color_dark_ground = (50, 50, 150)

    def sync(self):
        for x in range(self.width):
            for y in range(self.height):
                curr = self.floor[x][y]
                self.tdl_map.transparent[x, y] = curr.isTransparent()
                self.tdl_map.walkable[x, y] = curr.isWalkable()
                curr_object = self.objects[x][y]
                if curr_object is not None:
                    self.tdl_map.transparent[x, y] = curr_object.isTransparent()
                    self.tdl_map.walkable[x, y] = curr_object.isWalkable()

    def addobject(self,object):
        self.objects[object.x][object.y]=object
        self.tdl_map.walkable[object.x,object.y]=object.isWalkable()
        self.tdl_map.transparent[object.x,object.y]=object.isTransparent()

    def moveobject(self,oldPos,newPos):
        if self.tdl_map.walkable[newPos[0],newPos[1]] and self.objects[newPos[0]][newPos[1]] is None:
            obj=self.objects[oldPos[0]][oldPos[1]]
            obj.x=newPos[0]
            obj.y = newPos[1]
            self.objects[newPos[0]][newPos[1]]=obj
            self.objects[oldPos[0]][oldPos[1]]=None
            self.tdl_map.walkable[oldPos[0],oldPos[1]]=self.floor[oldPos[0]][oldPos[1]].isWalkable()
            self.tdl_map.transparent[oldPos[0], oldPos[1]] = self.floor[oldPos[0]][oldPos[1]].isTransparent()
            return True
        else:
            return False

    def render(self,con):
        for y in range(self.height):
            for x in range(self.width):
                wall = not self.tdl_map.walkable[x,y]
                if wall:
                    con.draw_char(x, y, '#', fg=(0,0,0), bg=self.color_dark_wall)
                else:
                    con.draw_char(x, y, '.', fg=(0,0,0), bg=self.color_dark_ground)
        for object in itertools.chain(*self.objects):
            if(object is not None):
                object.draw(con)