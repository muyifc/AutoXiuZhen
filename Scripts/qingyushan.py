import numpy as np

class QingYuShan():
    EnterNames = np.array(["qingyushan.png","qingyushan1.png"])
    # daboss
    # MovePosition = np.array([
    #     [1,0],[1,0],[1,0],
    #     [1,0],[1,0],[1,0],
    #     [1,0],[0,-1],[0,-1],
    #     [-1,0],[-1,0],[-1,0],
    #     [-1,0],[-1,0],[-1,0],
    #     [-1,0],[0,-1],[0,-1],
    #     [1,0],[0,-1],[1,0],
    #     [0,-1],[0,-1],[0,-1],
    #     [0,-1],[0,-1],[0,-1],
    #     [1,0],[1,0],[-1,0],
    #     [0,-1],[0,-1],[0,-1],
    #     [-1,0],[-1,0],[-1,0],
    #     [0,-1],[0,-1],[0,-1],
    #     [1,0],[1,0],[0,-1],
    #     [0,-1],[1,0],[0,1],
    #     [0,1],[1,0],[0,1],
    #     [0,1],[0,1],[1,0],
    #     [0,-1],[0,-1],[0,-1],
    #     [0,-1],[1,0],[0,1],
    #     [1,0],[0,-1],[0,-1],
    #     [1,0],[1,0],[1,0],
    #     [0,1],[0,1],[0,1],
    #     [0,1],[-1,0],[1,0],
    #     [1,0],[-1,0],[0,1],
    #     [0,1],[0,1],[0,1],
    #     [0,1],[0,1],[-1,0],
    #     [0,1],[-1,0],[0,1],
    #     [1,0],[1,0],[0,-1],
    #     [1,0],[1,0],[1,0],
    #     [1,0],[1,0],[0,-1],
    #     [-1,0],[0,-1],[0,-1],
    #     [0,-1],[0,-1],[1,0],
    #     [1,0],[0,-1],[0,-1],
    #     [0,-1],[0,-1],[0,-1],
    #     [0,-1],[1,0],[1,0],
    #     [1,0],[0,1],[-1,0],
    #     [1,0],[0,1],[0,1],
    # ])
    MovePosition = np.array([
        [1,0],[1,0],[1,0],
        [1,0],[1,0],[1,0],
        [1,0],[0,-1],[0,-1],
        [-1,0],[-1,0],[-1,0],
        [-1,0],[-1,0],[-1,0],
        [-1,0],[0,-1],[0,-1],
        [1,0],[0,-1],[1,0],
        [0,-1],[0,-1],[1,0],
        [0,-1],[1,0],[1,0],
        [1,0],[1,0],[1,0],
        [1,0],[0,1],[0,-1],
        [0,-1],[0,1],[1,0],
        [0,-1],[0,-1],[0,-1],
        [0,-1],[0,-1],[0,-1],
        [0,-1],[1,0],[-1,0],
        [-1,0],[1,0],[0,-1],
        [0,-1],[0,-1],[0,-1],
        [-1,0],[-1,0],[-1,0],
        [0,1],[0,1],[-1,0],
        [0,-1],[-1,0],[0,1],
        [0,1],[0,1],[0,1],
        [-1,0],[-1,0],[-1,0],
        [-1,0],[-1,0],[0,-1],
        [0,-1],[0,-1],[1,0],
        [1,0],[0,-1],[0,-1],
        [-1,0],[0,0],[0,0]
    ])

    # bu da boss
    # MovePosition = np.array([
    #     [1,0],[1,0],[1,0],
    #     [1,0],[1,0],[1,0],
    #     [1,0],[0,-1],[0,-1],
    #     [-1,0],[-1,0],[-1,0],
    #     [-1,0],[-1,0],[-1,0],
    #     [-1,0],[0,-1],[0,-1],
    #     [1,0],[0,-1],[1,0],
    #     [0,-1],[0,-1],[1,0],
    #     [0,-1],[1,0],[1,0],
    #     [1,0],[1,0],[1,0],
    #     [1,0],[0,1],[0,-1],
    #     [0,-1],[0,1],[1,0],
    #     [1,0],[1,0],[1,0],
    #     [1,0],[1,0],[0,-1],
    #     [-1,0],[0,-1],[0,-1],
    #     [0,-1],[0,-1],[1,0],
    #     [1,0],[0,-1],[0,-1],
    #     [0,-1],[0,-1],[0,-1],
    #     [0,-1],[1,0],[1,0],
    #     [1,0],[0,1],[-1,0],
    #     [1,0],[0,1],[0,1],
    # ])