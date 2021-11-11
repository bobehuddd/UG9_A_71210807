print("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")
order_1=int(input("IKAN BAKAR       Rp 25.000,00    : "))
order_2=int(input("ES DOGER         Rp 6.000,00     : "))
order_3=int(input("RUJAK CINGUR     Rp 8.000,00     : "))
print("=====TOTAL=====")
totalorder_1=order_1*25000
totalorder_2=order_2*6000
totalorder_3=order_3*8000
print("TOTAL IKAN BAKAR     : Rp",totalorder_1)
print("TOTAL ES DOGER       : Rp",totalorder_2)
print("TOTAL RUJAK CINGUR   : Rp",totalorder_3)
print("Jumlah total biaya yang harus dibayar adalah Rp",totalorder_1+totalorder_2+totalorder_3)
