import math
import numpy as np

def base_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    s = 1 / (1+math.exp(-x))
    print("使用math.exp：")
    print("sigmoid("+str(x)+") = " + str(s))
    return s
def numpy_sigmoid():
    '''
    因为math.exp只接受实数，而深度学习一般使用的是向量和矩阵
    '''
    x=np.array([1,2,3])
    s=1 / (1+np.exp(-x))
    print("使用np.exp：")
    print("sigmoid("+str(x)+") = " + str(s))

if __name__ == "__main__":
    base_sigmoid(3)
    numpy_sigmoid()