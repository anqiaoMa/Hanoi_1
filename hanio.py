def hanoi(n, a, b, c):
    '''
    :param n: 表示总共有几个盘子
    :param A: 表示第一个柱子，开始的柱子
    :param B: 表示中间的过渡柱子
    :param C: 表示第三根柱子，也是要转移到的柱子
    :return:
    '''
    global i
    if n==1:
        i +=1
        print('移动第',i,'次',a,'-->',c)
        return None
    #把n-1个盘子，从a柱借助于c柱转移到b柱子上
    hanoi(n-1,a,c,b)
    #把最下面一个盘从a柱转移到c柱上去
    hanoi(1,a,b,c)
    #把n-1个盘子，从b柱借助于a柱转移到c柱子上
    hanoi(n-1,b,a,c)
i = 0
hanoi(3,'A','B','C')
