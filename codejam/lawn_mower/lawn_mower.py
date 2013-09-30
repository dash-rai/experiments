#!/usr/bin/python
#Solution to problem at http://code.google.com/codejam/contest/2270488/dashboard#s=p1

def mow(N,M,pattern):
  rowmaxs=map(max,pattern)
  colmaxs=map(max,[[row[col] for row in pattern] for col in xrange(M)])
  for i in xrange(N):
    for j in xrange(M):
      if pattern[i][j]<rowmaxs[i] and pattern[i][j]<colmaxs[j]:
        #Cannot mow the tile to the height mentioned  moving the mower vertically or horizontally
        return "NO"
  return "YES"



infile=open('lawn_mower_large.in','r')
outfile=open('lawn_mower_large.out','w')

test_cases=int(infile.readline())

lawn_pat=[]
for case_number in xrange(test_cases):
  N,M=map(int,infile.readline().split(' '))
  for i in xrange(0,N):
    lawn_pat.append(map(int,infile.readline().split(' ')))
  outfile.write('Case #%d: %s\n' %(case_number+1,mow(N,M,lawn_pat)))
  lawn_pat=[]              
  
infile.close()
outfile.close()
  
  
  
  
