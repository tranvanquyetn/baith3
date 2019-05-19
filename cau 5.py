# viết chương trình sau và coi sự thay đổi của biến
a="hello guy!"
def say():
    global a
    a="vinh university"
    print(a)
say()
print(a)