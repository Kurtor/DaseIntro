# 参考了网络资料
import re
id_card = str(input())
pattern = r'^([1-6][1-9]|50)\d{4}(19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[0-9X]$'

if re.match(pattern, id_card) :
    print("legal!")
else:
    print("illegal")
