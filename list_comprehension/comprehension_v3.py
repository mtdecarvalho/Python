generator = (i ** 2 for i in range(10) if i % 2 == 0) # só gerará quando i for par, ou seja, 0 ** 2, 2 ** 2, etc..
print(next(generator)) # 0
print(next(generator)) # 4
print(next(generator)) # 16
print(next(generator)) # 36
print(next(generator)) # 64
# print(next(generator)) # erro
