import jieba

n = input()
words = jieba.lcut(n)
words.reverse()
s = ""
for i in words:
    s += i
print(s)