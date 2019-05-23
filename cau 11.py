def benefit(t, n, k):
    #Tiền lãi
    s = n * (t / 100) * k
    print("Tiền lãi: ", s)
    #Tiền nhận được
    S = n + s
    print("Số tiền nhận được: ", S)

t = int(input("Lãi suất theo tháng = "))
n = int(input("Số tiền ban đầu = "))
k = int(input("Số tháng gửi = "))
benefit(t, n, k)