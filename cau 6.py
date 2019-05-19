# viết chương trình sau và giải thích việc truyền tham só cho hàm
def get_sum(*num):
    tmp = 0
    # duyệt các tham số
    for i in num:
        tmp += i
    return tmp


result = get_sum(1, 2, 3, 4, 5)
print(result)