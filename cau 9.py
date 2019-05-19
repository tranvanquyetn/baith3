#Chương trình máy tính thực hiện các phép tính đơn giản
#Hàm cộng hai số
def add(x,y):
    return x + y
#Hàm trừ hai số
def subtract(x,y):
    return x - y
#Hàm nhân hai số
def multiply(x,y):
    return x*y
#Hàm chia hai số
def divide(x,y):
    return x / y
print("Chọn thao tác.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#Lấy đầu vào
choice = input("Nhập lựa chọn(1/2/3/4): ")
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else: print("Đầu vào không hợp lệ")