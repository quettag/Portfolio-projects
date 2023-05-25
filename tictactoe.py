def win(q,w,e):
  x = q,w,e
  lst = []
  new = []
  newlst = []
  ini = -1
  mid = 2
  endin = 5
  t1 = "XXX"
  t2 = "OOO"
  for i in x:
    n = "".join(i)
    new.append(n)
    for j in i:
      lst.append(j) 
  for p in range(3):
    ini += 1
    mid += 1
    endin += 1
    j = lst[ini] + lst[mid] + lst[endin]
    newlst.append(j)
  if t1 in new:
    return("X wins")
  elif t2 in new:
    return("O wins")
  if t1 in newlst:
    return("X wins")
  elif t2 in newlst:
    return("O wins")
  elif t1 in (lst[0]+lst[4]+lst[8]) or t1 in (lst[2]+lst[4]+lst[6]):
    return("X wins")
  elif t2 in (lst[0]+lst[4]+lst[8]) or t1 in (lst[2]+lst[4]+lst[6]):
    return("O wins")
  if t1 not in (new + newlst + [(lst[0]+lst[4]+lst[8])] +[(lst[2]+lst[4]+lst[6])]) and t2 not in (new + newlst + [(lst[0]+lst[4]+lst[8])] +[(lst[2]+lst[4]+lst[6])]):
    return("Draw")
