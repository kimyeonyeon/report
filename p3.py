# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def f(start_x, start_y):
        from collections import deque
        
        queue = deque([(start_x, start_y, 0)])  
        visited = [[False] * N for _ in range(N)]
        visited[start_x][start_y] = True
        c = None 
        
        while queue:
            x, y, dist = queue.popleft()
            
            if forest[x][y] > 0 and forest[x][y] < bear_size: 
                if c is None or (dist < c[2]) or (dist == c[2] and (x < c[0] or (x == c[0] and y < c[1]))):
                    c = (x, y, dist)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        return c
    
    while True:
        closest_honeycomb = f(bear_x, bear_y)
        
        if closest_honeycomb is None:
            break
        
        honey_x, honey_y, dist = closest_honeycomb
        time += dist
        bear_x, bear_y = honey_x, honey_y
        honeycomb_count += 1
        
        forest[bear_x][bear_y] = 0
        
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0
    
    return time

result = problem3(input)

assert result == 14
print("정답입니다.")
