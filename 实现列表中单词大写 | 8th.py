## 比用return语句的列表节省空间，也提高效率

def capital(listB):
  for i in range(len(listB)):
    listB[i]=listB[i].capitalize()
listA=['hope','is','a','good','thing','.']
listA_backup=listA[:]
capital(listA)
print(listA)
