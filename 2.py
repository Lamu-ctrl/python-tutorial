# ======================================
# 1.List  (小火車)
# ======================================

# 程式語言中 以0為起點

# arr1 = [1, 2, 3]
# arr2 = [10, 'hello world', 8.7]


# print(type(arr1))  # 檢查形式
# print(arr1)
# arr1[0] = [1, 2, 3]
# print(arr2[1])# 可以操作某一個元
# print(arr1)
# print(arr2)  # 每節車廂可以不同data type

# # 補充 : List 操作參考資料 https://www.learncodewithmike.com/2019/12/python-list.html
# # a.宣告
# arr1 = [1, 2, 3, 4]
# # b.存取
# print(arr1[0])  #第一個
# print(arr1[1])  #第二個
# print(arr1[-1]) #最後一個
# print(arr1[1:])  # 第二個到最後一個
# print(" arr1[0:3] : ", arr1[0:3])  # 0~2 不包含尾巴 [1, 2, 3]
# print(arr1[:2])  # 0~1 不包含2
# print(arr1[:])  # 全

# # c.新增串列元素的方法

# # append() 附加
# arr1 = [1, 2, 3, 4]
# print(arr1)
# arr1.append(5)
# print(arr1)

# # insert() 插入
# arr1 = [1, 2, 3 , 4 ]
# print(arr1)
# arr1.insert(1,5) # 原先陣列 [1, 2, 3 , 4 ] 插入至第1位置 [1,"5", 2, 3 , 4 ]
# print(arr1)

# ======================================
# # 2.for迴圈 (for loop)
# ======================================


names = ["Mary", "Bob", "Jim", "Rere"]
w = ["40", "20", "50", "80"]
print("for x in names: \n")
# for x in names:
#     print(x)
# 原理逐個取出names中的元素

# for name in names:
#     print(name)
# # 我們更喜歡這樣寫，讓變數名稱有意義，未來看程式碼會比較好懂


# print("for i in range(10): \n")
# for i in range(10):
#     print(i)

print("names[i] \n")
for i in range(1, 4):
    print(names[i], " ", w[i])

# ======================================
# # 3. Range
# ======================================

# # Range(stop)
# #     stop：停止點
# # Range(start, stop)
# #     start：起始點
# #     stop：停止點
# # Range(start, stop, step)
# #     start：起始點
# #     stop：停止點
# #     step：間隔

# r1 = range(5, 10)
# r2 = range(5, 50, 5)

# ======================================
# 練習
# ======================================
# # 2a
# # insert
# # 題目敘述:有一升冪數列，今有一數字需放入其中，並且結束後仍須為升冪數列
# x = input("插入一數字 : ")
# List1 = [1, 5, 8, 12, 20, 200]

# print("原數列", List1)
# print("插入", x)

# ======================================

# 2b reverse
# 有一數列，請倒置這數列
# 說明  [ 1 , 5 , 8 ]  reverse後為 [8,5,1]
# 第一個變最後一個，最後一個變第一個
List1 = [1, 5, 8, 12, 20, 200]
# a. 請放到 List2 給我

# ======================================
# 2c 奇數判斷
# 找出 0~20 中的奇數 放到一個list中

# for i in range(21):
#     pass
# ======================================
# 2d 質數判斷
# 找出 0~20 中的質數 放到一個list中
# ======================================
# 2e
# 第一個陣列包含0~20中的偶數
# 另一個包含0~20中的奇數

# 然後請用一個for迴圈印出以下結果：
# 1 <---> 2
# 3 <---> 4
# 5 <---> 6
# 7 <---> 8
# 9 <---> 10
# 11 <---> 12
# 13 <---> 14
# 15 <---> 16
# 17 <---> 18
# 19 <---> 20
