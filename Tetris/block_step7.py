import turtle as t
import random as r
import time

dy = [-1, 0, 1, 0] #행
dx = [0, 1, 0, -1] #열

#2-1벽돌 클래스
class Brick():
    def __init__(self):
        self.y=0
        self.x=6
        self.color=r.randint(1,6)
 # 3-1 벽돌 움직이기 왼쪽 오른쪽
    def move_left(self, grid):
        if grid[self.y][self.x - 1] == 0 and grid[self.y + 1][self.x - 1] ==0:
            grid[self.y][self.x] = 0
            self.x -= 1

    def move_right(self, grid):
        if grid[self.y][self.x + 1] == 0 and grid[self.y + 1][self.x + 1] ==0:
            grid[self.y][self.x] = 0
            self.x += 1

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
            # 6-2: game over line 15행에 빨간색 표시
            if y == 15 and grid[y][x] == 7: #7이된 벽만 빨간색으로 표시
                block.color("red")
            else:
                block.color(colors[grid[y][x]])
            block.stamp()
#4-2 같은 색일때 카운트
def DFS(y, x, grid, color):
    global ch, blank
    ch[y][x] = 1 #벽돌이 떨어진 현 위치에 다시 방문하지 않도록 1로 설정
    blank.append((y, x)) #같은 색깔일때 추가됨
    for i in range(4):
        #상하좌우 탐지
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 < yy < 24 and 0 < xx < 13:
            if grid[yy][xx] == color and ch[yy][xx] == 0 : #같은 색깔이고 한번도 간적이 없는 곳
                DFS(yy, xx, grid, color) #재귀함수
#5-4_1:벽돌이 있는 곳까지만 접근
def max_height(grid):
    for y in range(1, 24): #행
        for x in range(1, 13): #열
            if grid[y][x] != 0: #빈공간이 아니면
                return y

#5-2: 4개 이상일때 같은색 0으로 초기화
def grid_update(grid, blank):
    for y, x in blank:
        grid[y][x] = 0
    #5-3:중력작용 구현
    # 5-4_2 0일때까지 도는건 비효율적이므로 함수 구현
    height = max_height(grid)
    # 5-3 :행 탐색
    #for y in range(23, 0, -1):
    for y in range(23, height, -1): # 5-4_3:벽돌이 있는 곳까지마 컴파일되도록 함
        for x in range(1, 13): #열 탐색
            if grid[y][x] == 0:
                tmp_y = y #처음 0이 발견되 y좌표 기억
                # 빈공간 현위치에서 위로 올라가면서 비워있지 않을 때까지 하나씩 탐색
                while grid[tmp_y - 1][x] == 0 and tmp_y - 1 > 0:
                    tmp_y -= 1 #행 인덱스를 하나씩 줄여줌
                grid[y][x] = grid[tmp_y - 1][x] #원래 좌표에 행인덱스 위(하나줄인 인덱스) 벽돌을 복사해주고
                grid[tmp_y - 1][x] = 0 #빈공간으로 구현
#7-2 : 4개이상이면서 색이 같은 벽돌이 여러개 일때 모두 지우기
def continual_remove():
    global blank, ch
    while True:
        flag = 1
        for y in range(23, 15, -1): #행
            for x in range(1, 13): #열
                if grid[y][x] != 0: #비워있지 않으면
                    ch = [[0] * 14 for _ in range(25)]
                    blank = []
                    DFS(y, x, grid, grid[y][x]) #현재 좌표의 색깔 번호
                    if len(blank) >= 4:
                        grid_update(grid, blank)#중력 구현
                        flag = 0
        draw_grid(block, grid)
        if flag == 1:
            break

#6-3: game over 함수 텍스트 구현
def game_over():
    pen.up() #펜 객체 이동시 pen.up을 해서 이동해야 라인이 안생김
    pen.goto(-120, 100) #글씨가 쓰여질 좌표
    pen.write("Game Over", font=("courier", 30))

#6-6:you win 함수 텍스트 구현
def you_win():
    pen.up()#펜 객체 이동시 pen.up을 해서 이동해야 라인이 안생김
    pen.goto(-100, 100)
    pen.write("You Win", font=("courier", 30))


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

    #6-1:펜 객체 생성
    pen = t.Turtle()
    pen.ht() #모양이 보이지 않게 숨김
    pen.goto(-80, 290) #좌표
    pen.color("white") #펜색
    pen.write("Block Game", font=('courier', 20, 'normal')) #폰트속성으로 글자생성

    #3-2 : 키보드 이벤트
    sc.onkeypress(lambda: brick.move_left(grid), "Left")
    sc.onkeypress(lambda: brick.move_right(grid), "Right")
    sc.listen()#3-3 :이벤트 활성화

    while True:
        sc.update() #2-3.스크린 업데이트
        if grid[brick.y+1][brick.x]==0:#2-6 0이라고 입력된것만 지우기
            grid[brick.y][brick.x]=0
            brick.y+=1
            grid[brick.y][brick.x]=brick.color
        else:
            #4-1 그리드 탐색
            ch = [[0] * 14 for _ in range(25)]
            blank = []#체크를 위한 리스트 생성
            DFS(brick.y, brick.x, grid, brick.color) #벽돌의 위치와 컬러
            print(len(blank))
            # 2-7 벽돌 다시 나타나기
            brick=Brick()
            #5-1 4개이상이면 지우기
            if len(blank) >= 4:#벽돌이 4개 이상이면
                grid_update(grid, blank)#지우기
                #7-1:일차적으로 지운후 연속적으로 상하좌우 그리드 다시 탐색
                continual_remove()

            #6-4:game 종료 구현
            height = max_height(grid) #현재 벽돌의 위치
            if height <= 15:#현 위치가 15행이면
                game_over()#함수 호출
                break #게임 종료
            #6-5:기본 벽돌이 두줄 남아 있을때 you_win 구현
            elif height >= 22:
                draw_grid(block, grid)  #6-7: 화면에 두줄이 화면에 그려주고 표현
                you_win()
                break
            #     continual_remove()
            #
            # height = max_height(grid)

        # for x in grid:
        #     print(x)
        # print()
        draw_grid(block, grid)
        time.sleep(0.05) #2-5.while문 속도

    # for x in grid:
    #     print(x)
    # draw_grid(block, grid)

    sc.mainloop()