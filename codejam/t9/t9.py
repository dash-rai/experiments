#!/usr/bin/python
#Solution to problem at https://code.google.com/codejam/contest/351101/dashboard#s=p2
import sys
infile=open('t9-large.in','r')# or sys.exit 
outfile=open('t9-large.out','w')
key_map = {'1':[1,1],' ':[0,1],'a':[2,1],'b':[2,2],'c':[2,3],'2':[2,4],\
             '3':[3,4],'d':[3,1],'e':[3,2],'f':[3,3],'g':[4,1],'h':[4,2],\
             'i':[4,3],'4':[4,4],'j':[5,1],'k':[5,2],'l':[5,3],'5':[5,4],\
             'm':[6,1],'n':[6,2],'o':[6,3],'6':[6,4],'p':[7,1],'q':[7,2],\
             'r':[7,3],'s':[7,4],'7':[7,5],'t':[8,1],'u':[8,2],'v':[8,3],\
             '8':[8,4],'w':[9,1],'x':[9,2],'y':[9,3],'z':[9,4],'9':[9,5],\
             '0':[0,2]}
test_cases=int(infile.readline())
numoflastchar=-1#remember the button of last character
t9_nums=''

for case_count in range(1,test_cases+1):
  line_chars=infile.readline().rstrip('\n')#get rid of '\n' at the end of line
  for ch in line_chars:
    if numoflastchar==key_map[ch][0]:
      t9_nums+=' '
    t9_nums+=str(key_map[ch][0])*key_map[ch][1]
    numoflastchar=key_map[ch][0]
  numoflastchar=-1
  outfile.write('Case #%d: %s\n'%(case_count,t9_nums))
  t9_nums=''
  
  
  
