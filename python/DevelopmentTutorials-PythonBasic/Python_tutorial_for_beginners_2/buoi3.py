



# if (dieu kien):
#     (cau lenh)


# age = int(input("Nhap vao so tuoi cua ban "))

# if age < 18:
#     print("con la tre con ")
# if age >= 18:
#     print(" da truong thanh ")

# if 14 > 19:
#     print(" no dung la nhu vay")


# if age < 18:
#     print("con la tre con ")
# else:
#     print(" da truong thanh ")

# neu tuoi < 18 thi in ra con la tre con
# nguoc lai thi in ra da truong thanh


# day = input("hom nay la thu may : ")

# if day == "2":
#     print(" chao thu 2  ")
# elif day == "3":
#     print(" chao thu 3 ")
# elif day == "4":
#     print(" chao thu 4 ")
# elif day == "5":
#     print(" chao thu 5 ")
# elif day == "6":
#     print(" chao thu 6 ")
# elif day == "7":
#     print(" chao thu 7 ")
# elif day == "CN":
#     print(" chao CN ")
# else:
#     print(" Khong hop le")



age = int(input("Nhap vao so tuoi cua ban "))

# ( - vo cung ; 18)

if age < 18: # ( - vo cung ; 18)
    if age < 16:  #( - vo cung ; 16)
        print(" tre chua  thanh nien")
    else: #[16 - 18)
        print(" tre vi thanh nien ")
else: # [18; + vo cung)
    if age < 25: # [18;25)
        print(" thanh nien ")
    elif age < 40: #[25;40)
        print(" trung nien")
    else: # [40;+ vo cung]
        print(" nguoi gia ")





''' nhap vao so tuoi tu ban phim

    neu age < 18 thi  thi la hoc sinh 
    neu 18 >= age <= 25 thi la sinh vien
    neu age > 25 thi la nguoi di lam


'''