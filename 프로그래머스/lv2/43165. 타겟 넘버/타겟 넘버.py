def solution(numbers, target):
    global cnt
    cnt = 0
    # 최초 시작
    dfs(0, 0, numbers, target)
    
    return cnt

def dfs(i, sum_n, numbers, target):
    # i 현재 인덱스, sum_n 합산 값
    global cnt
    
    if i == len(numbers):
        if sum_n == target:
            cnt += 1
        return
    
    dfs(i+1, sum_n+numbers[i], numbers, target)
    dfs(i+1, sum_n-numbers[i], numbers, target)
    
    return
