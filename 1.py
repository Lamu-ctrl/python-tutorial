# ======================================
# # 1.Output
# ======================================

# print('Hi, my name is Simon')
# print('Hi, my name is', 'Simon')
# 註解 

# ======================================
# # 2.變數
# ======================================


# iv = 10
# fv = 12.3
# cv = 3 + 5j
# sv = 'hello python'
# bv = True
# nv = None

# print(iv, fv, cv, sv, bv)
# print(type(iv))
# print(type(fv))
# print(type(cv))
# print(type(sv))
# print(type(bv))
# print(nv)
# print(isinstance(sv, str))
# # note : 遇到看不懂的東西怎麼做

# ======================================
# # 3.User Input
# ======================================


# name = input('Hello, what is your name?  ')
# print('Hi, ', name)

# ======================================
# # 4. 數學運算子 Arithmatic Operator (+-*/%)
# ======================================



# # 運算子	功能
# # x + y	    X加Y
# # x - y	    X減Y
# # x * y	    X乘Y
# # x / y	    X除以Y
# # x // y	X除以Y，只取整數解 
# # x % y	    求X除以Y的餘數 modulo
# # x ** y	X的Y次方

# print( 5 / 3 )
# print( 5 // 3 )
# print( 5 % 3 )

# # 補充: 餘數應用  小費馬定理  
# # https://ithelp.ithome.com.tw/articles/10205727
# # https://ithelp.ithome.com.tw/articles/10205906

# ======================================
# # 5.IF else 
# ======================================

# grade = 90

# if grade >= 90:
#     print('Excellent!')
# elif grade >= 60:
#     print('Good enough!')
# else:
#     print('Loser!')

# # 解釋縮排 tab

# ======================================
# 6. 比較運算子  
# ======================================

# 運算子	效果
# x < y	X是否小於Y
# x <= y	X是否小於等於Y
# x > y	X是否大於Y
# x >= y	X是否大於等於Y
# x == y	X是否等於Y
# x != y	X是否不等於

# ======================================
# 7. 邏輯運算子 Logical Operator  || or  and  not 
# ======================================



# h = 180
# w = 85
# grade = 80

# # 身高超過175或是體重超過80，看起來就很大隻
# if h > 175 or w > 80:
#     print('big dude')

# # 成績高於70但是不高於90，就是個普通學生
# if grade > 70 and grade < 90:
#     print('noraml')
