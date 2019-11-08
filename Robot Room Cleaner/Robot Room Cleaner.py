# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

def dfs(robot, x, y, prev_direction, visited):
    robot.clean()
    visited.add((x, y))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for index in range(4):
        direction = (prev_direction + index) % 4
        dx, dy = directions[direction]
        if (x + dx, y + dy) not in visited and robot.move():
            dfs(robot, x + dx, y + dy, direction, visited)
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        robot.turnLeft()


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dfs(robot, 0, 0, 0, set())
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            