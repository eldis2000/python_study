# 다차원 배열을 다룰때 사용
# 수치계산에 좋다.
# numpy.org
import numpy as np

x = np.arange(15, dtype=np.int64).reshape(3, 5)

x[1:, ::2] = -99



