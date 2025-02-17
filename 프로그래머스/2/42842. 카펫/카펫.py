def solution(brown, yellow):
    area = brown + yellow
    
    for h in range(1, int(area**0.5) + 1):
        if area % h == 0:
            w = area // h
            if 2 * w + 2 * h - 4 == brown:
                return [w, h]