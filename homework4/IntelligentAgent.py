import random
from BaseAI import BaseAI

MIN_INTEGER = float('-inf')
MAX_INTEGER = float('inf')

class IntelligentAgent(BaseAI):
	def getMove(self, grid):
		return self.decision(grid)

	def decision(self, grid):
		grid = (None, grid)
		depth = 0
		(child, utility) = self.minimize(grid, MIN_INTEGER, MAX_INTEGER, depth)
		if child == None:
			return None

		return child[0]

	def minimize(self, grid, alpha, beta, depth):
		depth += 1

		moves = grid[1].getAvailableMoves()
		
		if self.terminal_test(depth):
				return (grid[0], self.eval(grid[1]))

		(minChild, minUtility) = (None, MAX_INTEGER)

		for child in moves:
			(__, utility) = self.expectimax(child, alpha, beta, depth)

			if utility < minUtility:
				(minChild, minUtility) = (child, utility)

			if minUtility <= alpha:
				break

			if minUtility < beta:
				beta = minUtility

		return (minChild, minUtility)

	def expectimax(self, grid, alpha, beta, depth):
		depth += 1

		if self.terminal_test(depth):
				return (grid[0], self.eval(grid[1]))

		(maxChild, maxUtility) = (None, MIN_INTEGER)

		for cell in grid[1].getAvailableCells():
			grid_2 = (None, grid[1].clone())
			grid_2[1].setCellValue(cell, 2)
			grid_4 = (None, grid[1].clone())
			grid_4[1].setCellValue(cell, 4)
			(child_2, util_2) = self.minimize(grid_2, alpha, beta, depth)
			(child_4, util_4) = self.minimize(grid_4, alpha, beta, depth)

			if util_4 > util_2:
				child = child_4
			else:
				child = child_2
			
			utility = util_2*0.9 + util_4*0.1

			if utility > maxUtility:
				(maxChild, maxUtility) = (child, utility)

			if maxUtility >= beta:
				break

			if maxUtility > alpha:
				alpha = maxUtility

		return (maxChild, maxUtility)

	def terminal_test(self, depth):
		return depth == 4

	def eval(self, grid):
		return 1*self.monotonocity(grid) + 30*self.smoothness(grid) - 1*self.free_tiles(grid) - grid.getMaxTile()

	def free_tiles(self, grid):
		return len(grid.getAvailableCells())

	def monotonocity(self, grid):
		value = 0
		for row in range(4):
			if grid.getCellValue((row, 0)) > grid.getCellValue((row, 1)):
				value += 1
			if grid.getCellValue((row, 1)) > grid.getCellValue((row, 2)):
				value += 1
			if grid.getCellValue((row, 2)) > grid.getCellValue((row, 3)):
				value += 1

		for col in range(4):
			if grid.getCellValue((3, col)) > grid.getCellValue((2, col)):
				value += 1
			if grid.getCellValue((2, col)) > grid.getCellValue((1, col)):
				value += 1
			if grid.getCellValue((1, col)) > grid.getCellValue((0, col)):
				value += 1

		return value

	def smoothness(self, grid):
		value = 0
		#top left corner
		if grid.getCellValue((0, 0)) != 0:
			value += abs(grid.getCellValue((0, 1)) - grid.getCellValue((0, 0)))
			value += abs(grid.getCellValue((1, 0)) - grid.getCellValue((0, 0)))
		#top right corner
		if grid.getCellValue((0, 3)) != 0:
			value += abs(grid.getCellValue((0, 2)) - grid.getCellValue((0, 3)))
			value += abs(grid.getCellValue((1, 3)) - grid.getCellValue((0, 3)))
	   	#bottom left corner
		if grid.getCellValue((3, 0)) != 0:
			value += abs(grid.getCellValue((2, 0)) - grid.getCellValue((3, 0)))
			value += abs(grid.getCellValue((3, 1)) - grid.getCellValue((3, 0)))
	    #bottom right corner
		if grid.getCellValue((3, 3)) != 0:
			value += abs(grid.getCellValue((2, 3)) - grid.getCellValue((3, 3)))
			value += abs(grid.getCellValue((3, 2)) - grid.getCellValue((3, 3)))

	    # top edges
		if grid.getCellValue((0, 1)) != 0:
			value += abs(grid.getCellValue((0, 0)) - grid.getCellValue((0, 1)))
			value += abs(grid.getCellValue((1, 1)) - grid.getCellValue((0, 1)))
			value += abs(grid.getCellValue((0, 2)) - grid.getCellValue((0, 1)))

		if grid.getCellValue((0, 2)) != 0:
			value += abs(grid.getCellValue((0, 1)) - grid.getCellValue((0, 2)))
			value += abs(grid.getCellValue((1, 2)) - grid.getCellValue((0, 2)))
			value += abs(grid.getCellValue((0, 3)) - grid.getCellValue((0, 2)))

	   	# left edges
		if grid.getCellValue((1, 0)) != 0:
			value += abs(grid.getCellValue((0, 0)) - grid.getCellValue((1, 0)))
			value += abs(grid.getCellValue((2, 0)) - grid.getCellValue((1, 0)))
			value += abs(grid.getCellValue((1, 1)) - grid.getCellValue((1, 0)))

		if grid.getCellValue((2, 0)) != 0:
			value += abs(grid.getCellValue((2, 1)) - grid.getCellValue((2, 0)))
			value += abs(grid.getCellValue((1, 0)) - grid.getCellValue((2, 0)))
			value += abs(grid.getCellValue((3, 0)) - grid.getCellValue((2, 0)))

	    # right edges
		if grid.getCellValue((1, 3)) != 0:
			value += abs(grid.getCellValue((0, 3)) - grid.getCellValue((1, 3)))
			value += abs(grid.getCellValue((1, 2)) - grid.getCellValue((1, 3)))
			value += abs(grid.getCellValue((2, 3)) - grid.getCellValue((1, 3)))

		if grid.getCellValue((2, 3)) != 0:
			value += abs(grid.getCellValue((1, 3)) - grid.getCellValue((2, 3)))
			value += abs(grid.getCellValue((2, 2)) - grid.getCellValue((2, 3)))
			value += abs(grid.getCellValue((3, 3)) - grid.getCellValue((2, 3)))

	    # bottom edges
		if grid.getCellValue((3, 1)) != 0:
			value += abs(grid.getCellValue((3, 0)) - grid.getCellValue((3, 1)))
			value += abs(grid.getCellValue((3, 2)) - grid.getCellValue((3, 1)))
			value += abs(grid.getCellValue((2, 1)) - grid.getCellValue((3, 1)))

		if grid.getCellValue((3, 2)) != 0:
			value += abs(grid.getCellValue((3, 1)) - grid.getCellValue((3, 2)))
			value += abs(grid.getCellValue((3, 3)) - grid.getCellValue((3, 2)))
			value += abs(grid.getCellValue((2, 2)) - grid.getCellValue((3, 2)))

	    # top-inner left
		if grid.getCellValue((1, 1)) != 0:
			value += abs(grid.getCellValue((0, 1)) - grid.getCellValue((1, 1)))
			value += abs(grid.getCellValue((1, 0)) - grid.getCellValue((1, 1)))
			value += abs(grid.getCellValue((1, 2)) - grid.getCellValue((1, 1)))
			value += abs(grid.getCellValue((2, 1)) - grid.getCellValue((1, 1)))

	    # top-inner right
		if grid.getCellValue((1, 2)) != 0:
			value += abs(grid.getCellValue((1, 1)) - grid.getCellValue((1, 2)))
			value += abs(grid.getCellValue((0, 2)) - grid.getCellValue((1, 2)))
			value += abs(grid.getCellValue((1, 3)) - grid.getCellValue((1, 2)))
			value += abs(grid.getCellValue((2, 2)) - grid.getCellValue((1, 2)))

	    # bottom-inner left
		if grid.getCellValue((2, 1)) != 0:
			value += abs(grid.getCellValue((1, 1)) - grid.getCellValue((2, 1)))
			value += abs(grid.getCellValue((2, 0)) - grid.getCellValue((2, 1)))
			value += abs(grid.getCellValue((2, 2)) - grid.getCellValue((2, 1)))
			value += abs(grid.getCellValue((3, 1)) - grid.getCellValue((2, 1)))

	    # bottom-inner right
		if grid.getCellValue((2, 2)) != 0:
			value += abs(grid.getCellValue((1, 2)) - grid.getCellValue((2, 2)))
			value += abs(grid.getCellValue((2, 1)) - grid.getCellValue((2, 2)))
			value += abs(grid.getCellValue((2, 3)) - grid.getCellValue((2, 2)))
			value += abs(grid.getCellValue((3, 2)) - grid.getCellValue((2, 2)))

		return value