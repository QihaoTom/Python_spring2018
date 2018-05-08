## 在字符串前加上序号
f=open('companies.txt','r+')
# 全部行从头到尾读一遍
lines=f.readlines()
# 
for i in range(len(lines)):
    lines[i]=str(i+1)+''+lines[i]
# 再从尾到头
f.seek(0)
f.writelines(lines)
f.close()

# 在另一个文件里，在字符串前加上序号
f1=open('companies.txt')
lines=f1.readlines()
f1.close()
for i in range(len(lines)):
    #相当于把序号，str(i+1),加在每一行，lines[i]
    lines[i]=str(i+1)+''+lines[i]
f2=open('scompanies.txt','w')
f2.writelines(lines)
f2.close()