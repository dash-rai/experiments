#!/usr/bin/python
#Solution to Problem at https://code.google.com/codejam/contest/351101/dashboard#s=p0
def shop(credit,item_prices_list):
  for i in xrange(0,len(item_prices_list)-1):
    for j in xrange(i+1,len(item_prices_list)):
      print item_prices_list[i]+item_prices_list[j]
      print credit
      if item_prices_list[i]+item_prices_list[j]==credit:
        return [i,j]
      
infile = open('store-small.in','r')
outfile= open('store-small.out','w')
test_cases = int (infile.readline())

for i in xrange(0,test_cases):
  credit=int(infile.readline())
  item_count=int(infile.readline())
  item_prices_list=infile.readline().split(' ')
  item_prices_list=[int(x) for x in item_prices_list]
  print item_prices_list
  p=shop(credit,item_prices_list)
  print p
  outfile.write("Case #%d: %d %d\n" %(i+1,p[0]+1,p[1]+1))#The results parser starts indices with 1 apparently
  
infile.close()
outfile.close()


