# n is row counts, m is col counts
def blur(img, rows, cols):
    for j in range(cols):
        for i in range(rows):
            if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                if i == 0:
                    if j == 0:
                        new_val = (img[i][j] + img[i][j+1] + img[i+1][j])/3
                    elif j == cols-1:
                        new_val = (img[i][j] + img[i][j-1] + img[i+1][j])/3
                    else:
                        new_val = (img[i][j] + img[i][j-1] + img[i][j+1] + img[i+1][j])/4
                elif i == rows-1:
                    if j == 0:
                        new_val = (img[i][j] + img[i][j+1] + img[i-1][j])/3
                    elif j == cols-1:
                        new_val = (img[i][j] + img[i][j-1] + img[i-1][j])/3
                    else:
                        new_val = (img[i][j] + img[i-1][j] + img[i][j+1] + img[i][j-1])/4

                if j == 0 and i != 0 and i != rows-1:
                    new_val = (img[i][j]+img[i+1][j]+img[i-1][j]+img[i][j+1])/4
                elif j == cols-1 and i != 0 and i != rows-1:
                    new_val = (img[i][j]+img[i+1][j]+img[i-1][j]+img[i][j-1])/4
            else:
                new_val = (img[i][j]+img[i+1][j]+img[i-1][j]+img[i][j-1]+img[i][j+1])/5
            img[i][j] = int(round(new_val,0))
        
    return img

import sys
if __name__ == "__main__":
    x = sys.stdin.readline().strip()
    n, m = [int(xi) for xi in x.split(' ')]
    img = []
    for i in range(n):
        row = sys.stdin.readline().strip()
        line_array = [int(x) for x in row.split(' ')]
        img.append(line_array)
    # n, m = 3, 3
    # img = [[12, 23, 34], [45, 56, 67], [78, 89, 90]]
    # print (img)
    blur_img = blur(img, n, m)

    for i in range(n):
        row_str = ""
        for j in range(m):
            row_str += str(blur_img[i][j]) + " "
        print (row_str)
