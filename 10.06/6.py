def rotate_by(lt, num):
    for i in range(num):
        lt.insert(0, lt.pop())
