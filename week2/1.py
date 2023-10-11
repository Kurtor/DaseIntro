# （1）2001拆解成667个3相乘
# （2）根据基本不等式的多维展开，可以从数学层面易得当拆解的数字为自然对数e的时候，这一列数的乘积最大。则在正整数力应当拆解为3，若不能完全拆解为3，则用2补齐。
# （3）如下
x = int(input())
i = x % 3
if i == 0:
    print(f"{x} divided into 3**{(int)(x/3)} ")
if i == 1:
    print(f"{x} divided into (3**{(int)(x / 3)-1})*2*2 ")
if i == 2:
    print(f"{x} divided into (3**{(int)(x / 3)})*2 ")
