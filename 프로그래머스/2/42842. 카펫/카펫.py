def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(3, total):  # 최소 높이는 3 (테두리 때문에)
        if total % height == 0:
            width = total // height
            if width >= height:
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]
