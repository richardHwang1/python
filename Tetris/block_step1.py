import turtle as t
import random as r


def draw_grid(block, grid):
    top=250
    left=-150
    #3.color=['black','red','blue','orange','yellow','green','purple','white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x=left+(x*22) #1.(x*20)
            sc_y=top-(y*22)  #1.(y*20)
            block.goto(sc_x,sc_y)
            #3.block.color(color[grid[y][x]])
            block.stamp()

if __name__ == "__main__":
    sc = t.Screen()
    #sc.tracer(False)
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    grid = [[0] * 12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0, 7) #처음 자리에
        grid[i].append(7) #끝에
    grid.append([7] * 14) #맨 끝 라인

    block = t.Turtle()
    block.penup() #주석처리후 확인
    block.speed(0)
    #1.block.shape("turtle")
    block.shape("square")
    block.color("red")
    #1.block.goto(-200,200) #강제 이동
    draw_grid(block, grid)

    for x in grid:
        print(x)

    sc.mainloop()