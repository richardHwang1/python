import turtle as t
import random as r
import time
#2-1벽돌 클래스
class Brick():
    def __init__(self):
        self.y=0
        self.x=6
        self.color=r.randint(1,6)

def draw_grid(block, grid):
    block.clear()#2-4벽돌이 지우면서 내려가기
    top=250
    left=-150
    colors=['black','red','blue','orange','yellow','green','purple','white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x=left+(x*22) #1.(x*20)
            sc_y=top-(y*22)  #1.(y*20)
            block.goto(sc_x,sc_y)
            block.color(colors[grid[y][x]])
            block.stamp()

if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False) #화면 한번에 보이기 움직이기
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    grid = [[0] * 12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0, 7) #처음 자리에
        grid[i].append(7) #끝에
    grid.append([7] * 14) #맨 끝 라인
    # 아래 3줄 기본 채우기
    for y in range(23,20,-1):
        for x in range(1,13):
            grid[y][x]=r.randint(1,6)

    block = t.Turtle()
    block.penup() #주석처리후 확인
    block.speed(0)
    #1.block.shape("turtle")
    block.shape("square")
    block.color("red")
    block.setundobuffer(None)  # 2-5벽돌의 속도가 점점 늦어지므로 버퍼비우기
    #1.block.goto(-200,200) #강제 이동
    #draw_grid(block, grid)
    # 2-2벽돌 출력
    brick=Brick()
    grid[brick.y][brick.x]=brick.color
    draw_grid(block, grid)

    while True:
        sc.update() #2-3.스크린 업데이트
        if grid[brick.y+1][brick.x]==0:#2-6 0이라고 입력된것만 지우기
            grid[brick.y][brick.x]=0
            brick.y+=1
            grid[brick.y][brick.x]=brick.color
        else:#2-7 벽돌 다시 나타나기
            brick=Brick()
        for x in grid:
            print(x)
        print()
        draw_grid(block, grid)
        time.sleep(0.05) #2-5.while문 속도

    for x in grid:
        print(x)
    draw_grid(block, grid)

    sc.mainloop()