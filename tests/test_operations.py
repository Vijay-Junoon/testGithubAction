from src.math_ops import add,sub

def test():
  assert add(2,3)==5
  assert add(-1,1) == 0
  assert sub(5,3) == 2
  assert sub(10,-5) == 15
test()