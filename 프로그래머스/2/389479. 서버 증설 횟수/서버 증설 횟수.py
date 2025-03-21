def solution(players, m, k):
    answer = 0 # 서버증설횟수
    serverTime = []
    
    for player in players:
        nowServer = len(serverTime)
        needServer = player // m
        if nowServer < needServer:
            newServer = needServer - nowServer
            nowServer += newServer
            answer += newServer
            for i in range(newServer):
                serverTime.append(k)
        # k시간동안만 유효한 서버
        for i, s in enumerate(serverTime):
            s -= 1
            serverTime[i] = s
            #if s < 0:
            #   del serverTime[i]
        while (0 in serverTime):
            del serverTime[serverTime.index(0)]
            
    
    return answer