

import binascii

# s = "龚伟".encode()
# t1 = binascii.b2a_hex(s)
# t2 = binascii.b2a_hex(s)[2:-1]
# t3 = binascii.hexlify(s)
# print(t1)
# print(t2)
# print(t3)

s = b"worker"

print(s)
for i in "worker":
    print(ord(i))
print(binascii.b2a_hex(s))
print(binascii.hexlify(s))
print(binascii.hexlify(s)[2:-1])


print(hex(10))
# 将二进制数据字符串转换为十六进制编码。
print(binascii.b2a_hex(b"10"))
