
"""

5번 : 5 [2, 3, 4] [1, 2, 3] 4
12번 : 5 [1, 2, 3] [2, 3, 4] 4

내 솔루션
"""



def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for m in range(1, n+1):
        if m in lost and m in reserve:
            lost.remove(m)
            reserve.remove(m)        
        elif m in lost and m-1 in reserve:
            lost.remove(m)
            reserve.remove(m-1)
        elif m in lost and m+1 in reserve:
            lost.remove(m)
            reserve.remove(m+1)
        elif m in lost and m in reserve:
            lost.remove(m)
            reserve.remove(m)
    
    return n-len(lost)
  
  
  """
  내가 감탄산 솔루션
  배울점
  1.for문 if문 간략화
 
  
  """
  def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
