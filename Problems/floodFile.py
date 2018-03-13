

def floodFill(image, sr, sc, new_color):
	
	color = image[sr][sc]

	def change_color(i, j, color, new_color):
		if i >= len(image) or i < 0 or j >= len(image[0]) or j < 0 or image[i][j] != color:
			return
		print image[i][j]
		image[i][j] = new_color
		print image

		change_color(i + 1, j, color, new_color)
		change_color(i - 1, j, color, new_color)
		change_color(i, j + 1, color, new_color)
		change_color(i, j - 1, color, new_color)
	if color != new_color:
		change_color(sr, sc, color, new_color)

	return image






image = [[0,0,0],[0,1,1]]
# image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
new_color = 1

print floodFill(image, sr, sc, new_color)



# out [[2,2,2],[2,2,0],[2,0,1]]