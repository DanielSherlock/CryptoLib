
class Grid(object):
    '''A Grid of strings,
    that can be seen as an alternative form of a Text
    '''
    def __init__(self, grid):
        self.grid = grid
    
    def switch_axes(self):
        '''Return Type: Grid
        Switched the axes of the grid, so that
        rows become columns, and columns become rows
        '''
        result = []
        j = 0
        while j < len(self.grid[0]):
            row = []
            i = 0
            while i < len(self.grid):
                row.append(self.grid[i][j])
                i += 1
            result.append(row)
            j += 1
        return Grid(result)

    def rows(self):
        '''Return Type: Data/Text
        Condenses the grid into a list of rows
        '''
        result = []
        for i in self.grid:
            result.append(''.join(i))
        return result

    def columns(self):
        '''Return Type: Data/Text
        Condenses the grid into a list of columns
        '''
        return self.switch_axes().rows()

    def __repr__(self):
        return "[['" + "'],\n ['".join(["','".join(i) for i in self.grid]) + "']]"

    def __str__(self):
        return '\n'.join([''.join(i) for i in self.grid])
