maze_example1 = {
   'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}

def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print (s)
    print (' ')

print_maze(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_example1['m'], maze_example1['s'], maze_example1['f']
class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]




maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])


def maze_controller(maze_runner):
	import random
	x = 0
	y = 0
	array = []
	flag = 'to'
	while maze_runner.found() != True:
		if (maze_runner.go()):
			if flag == 'left':
				y += 1
			elif flag == 'right':
				y -= 1
			elif flag == 'to':
				x += 1
			else:
				x -= 1
			array.append((x,y));
			if (x,y) in array:
				if random.randint(0, 1) == 0:
					maze_runner.turn_left()
					if flag == 'left':
						flag = 'from'
					elif flag == 'right':
						flag = 'to'
					elif flag == 'from':
						flag = 'right'
					else:
						flag = 'left'	
				else:
					maze_runner.turn_right()
					if flag == 'right':
						flag = 'from'
					elif flag == 'left':
						flag = 'to'
					elif flag == 'from':
						flag = 'left'
					else:
						flag = 'right'	
			else:
				continue			
		else:
			if (random.randint(0, 1) == 0):
				maze_runner.turn_left()
				if flag == 'left':
						flag = 'from'
				elif flag == 'right':
					flag = 'to'
				elif flag == 'from':
					flag = 'right'
				else:
					flag = 'left'	
			else:
				maze_runner.turn_right()
				if flag == 'right':
					flag = 'from'
				elif flag == 'left':
					flag = 'to'
				elif flag == 'from':
					flag = 'left'
				else:
					flag = 'right'	

				
			
		







	
		
		
