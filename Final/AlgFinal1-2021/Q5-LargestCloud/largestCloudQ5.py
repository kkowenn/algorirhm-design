''''
[10 Marks] Largest Cloud

As a part of environmental management and local weather forecast, an array of cameras is
placed around the city to keep track of the sky image.

At each fixed interval, a snapshot of the camera will be processed by the information
extraction program. One of the required features is to detect the size of the largest cloud in
the snapshot image. Given that the image is already processed into a matrix of black/white
pixels. The program is required to report the number of pixels occupied by the largest cloud
in the image.

A pixel is considered connected to an adjacent pixel only in one of the 4 directions, which are
up, down, left, and right.

Write the program that report the size of the largest cloud in the given image.

INPUT:
1st line: The number of rows, 𝑀≤500, and the number of columns, 𝑁 ≤1000, of the image.
Each of the following 𝑀 lines list rows of the image from top to bottom. Each row consists
of 𝑁 pixels ordered by column. Each pixel is either 0 (sky) or 1 (cloud).

OUTPUT: The size, in number of pixels, of the largest cloud in the image

EXAMPLE

INPUT
4 6
0 1 0 0 0 0
1 1 1 0 0 0
0 0 1 0 1 1
0 0 1 0 1 0
OUTPUT
6

Note: The largest cloud consists of the bold pixels.

'''


row, column = list(map(int, input().split()))
pic = []

for i in range(row):
    inp = list(map(int, input().split()))
    pic.append(inp)

masterPic = pic.copy()

def cloud(r, c):
    global pic, row, column

    if r < 0 :
        return 0
    if r > row-1:
        return 0
    if c < 0:
        return 0
    if c > column-1:
        return 0

    if pic[r][c] == 0:
        return 0
    else:

        pic[r][c] = 0
        return 1 + cloud(r, c-1) + cloud(r, c+1) + cloud(r-1, c) + cloud(r+1, c)

result = []
for i in range(row):
    for j in range(column):
        pic = masterPic.copy()
        result.append(cloud(i,j))

print(max(result))
