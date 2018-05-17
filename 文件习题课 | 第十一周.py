# 判断两个文件内容是否一样
with open("a.txt") as fp1:
    fp1_content=fp1.read()
with open('b.txt') as fp2:
    fp2_content=fp2.read()
if fp1_content==fp2_content:
    print('OK!')
else:
    print('NO!')


# 读取文件
with open(r'Desktop/companies.txt') as fp1:
    a=fp1.read(5)
    b=fp1.read()
    

# 是否在通讯簿中有其人，有其人在输出电话号码
with open('contacts.txt') as fp:
    lines=fp.readlines()
found=False
name=input("input your name:")
for eachline in lines:
    c_name,phone_num =eachline.split(',')
    if name==c_name:
        print(eachline)
        found=True
        break
if not found:
    print('not found!')
    

# 采用行程长度压缩方法RLC，并将结果写入另一个文件
def RLC(s):
    t=''
    count=1
    t=t+s[0]
    # 相等就加1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
        count+=1
    else:
        t+=str(count)
        t+=s[i]
        # 这里是对count重新初始化
        count=1
    t+=str(count)
    return t
with open('file1.txt','r') as fp1:
    sp1.read()
t = RLC(s)
with open('file2.txt', 'w') as fp2:
fp2.write(t)


# 如何插入文本
with open("blowing in the wind.ext",'r+') as fp:
    lines=fp.readlines()
    lines.insert(0,'blowin' in the wind\n')
    lines.insert(1,'Bob Dylan\n')
    lines.append("1962 by Warner Bros. Inc.\n")
    fp.seek(0)
    fp.writelines(lines)
    
# 
with open('T"\\socre.txt','r') as f:
    a=f.readlines()
del a[0]
ids=[]
for line in a:
    # 去掉换行符，用strip命令即可去掉
    line=line.strip()
    t=line.split()
    # 把t(0),即为id，放到ids里面去，把t(1)即为scores，放到scores里
    ids.append(t[0])
    scores.append(t[1])
maxid=scores.index(max(scores))
minid=scores.index(min(scores))
print("最高分为：" + scores[maxid] + "分，该学生学号为：" + ids[maxid])
print("最低分为：" + scores[minid] + "分，该学生学号为：" + ids[minid])    











