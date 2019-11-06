import numpy as np

def nhan_hang(A):
    for i in range(5):
        end = i+5
        temp = np.sum(A[i:end])
        if temp == 5 or temp == -5:
            return True
            # return False
    return False
        
def nhan_duong_cheo_chinh(A, i_row, i_col, W):
    for i in range(5):
        row_start = i_row - i
        col_start = i_col - i
        row_end = row_start + 5
        col_end = col_start + 5
        temp = np.sum(A[row_start:row_end, col_start:col_end]*W)
        if temp == 5 or temp == -5:
            return True
    return False


def nhan_duong_cheo_phu(A, i_row, i_col, W):
    for i in range(5):
        row_start = i_row + i - 4
        col_start = i_col - i
        row_end = row_start + 5
        col_end = col_start + 5
        temp = np.sum(A[row_start:row_end, col_start:col_end]*W)
        if temp == 5 or temp == -5:
            return True
    return False


def dk_thang(A, i_row, i_col):
    W3 = np.eye(5, 5)
    W4 = np.array([[0, 0, 0, 0, 1],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0]], dtype=np.uint8)

    A_pad = np.pad(A, 4)
    i_row = i_row+4
    i_col = i_col+4
    if nhan_hang(A_pad[i_row-4:i_row+5, i_col]):
        return True
    elif nhan_hang(A_pad[i_row, i_col-4:i_col+5]):
        return True
    elif nhan_duong_cheo_chinh(A_pad, i_row, i_col, W3):
        return True
    elif nhan_duong_cheo_phu(A_pad, i_row, i_col, W4):
        return True
    return False

def my_coro():
    max_map = 15
    A = np.zeros((max_map, max_map))
    print(A)
    turn = 1
    woner = 1
    while True:
        row = 0
        col = 0
        while True:
            row = np.uint8(input('row: '))
            col = np.uint8(input('col: '))
            if row-1 < 0 or col-1 < 0 or row-1 > max_map or col-1 > max_map or A[row-1, col-1] != 0:
                print('ban nhap qua ban co, vui long nhap lai')                
            else:
                A[row-1, col-1] = turn
                print(A)
                turn = -np.sign(turn)
                break
        if dk_thang(A, row-1, col-1):
            woner = -turn
            print(woner, ' thang')
            break

my_coro()
