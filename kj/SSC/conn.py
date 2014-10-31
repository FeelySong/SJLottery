# coding=utf-8

import mysql.connector
from datetime import datetime

cnx=mysql.connector.connect(user='root',password='shl850325',host='54.254.174.234',database='shijue',charset='utf8')

cursor=cnx.cursor()

query='select * from ssc_set where lid=1'

cursor.execute(query)

result=cursor.fetchone()

print result

def  kjdata(t2,cid,t1,t3):
        if(t2!=""):
            t4=','.join(t2)
            print t4
            n1=t4[0]
            n2=t4[2]
            n3=t4[4]
            if(cid!=5 and cid!=9):
                n4=t4[6]
                n5=t4[8]
        n1=int(n1)
        n2=int(n2)
        n3=int(n3)
        n4=int(n4)
        n5=int(n5)
        # echo Get_lottery($cid)."第".$t1."期:".$t2."<br>";
        sql = 'select * from ssc_data where cid=%s and issue=%s'
        print sql
        #echo $sql."<br>";
        cursor.execute(sql,(cid,t1))
        rowa = cursor.fetchone()
        print rowa
        tts = 0
        if(cid==1 or cid==2 or cid==3 or cid==4):
            if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts = 1
            if (n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
                tts=1
        elif(cid==5):
            if (n1=="0" and n2=="0" and n3=="0"):
                tts=1
            if (n1>9 or n2>9 or n3>9):
                tts=1
        elif(cid==6 or cid==7 or cid==8 or cid==11):
            if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts=1
            if (n1>11 or n2>11 or n3>11 or n4>11 or n5>11):
                tts=1
        elif(cid==9):
            if(n1=="0" and n2=="0" and n3=="0"):
                tts=1
            if(n1>9 or n2>9 or n3>9):
                tts=1
        elif(cid==10):
            if(n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts=1
            if(n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
                tts=1
        name='重庆时时彩'
        print cid,name,t1,t2
        #tmp='set cid='+cid+' name='+Get_lottery(cid), issue=t1, code='".$t2."', n1='".$n1."', n2='".$n2."', n3='".$n3."', n4='".$n4."', n5='".$n5."',opentime='".$t3."', addtime='".date("Y-m-d H:i:s")."'";
        if(rowa is None):
            if(tts==0):
                sql='INSERT INTO ssc_data(cid,name,issue,code,n1,n2,n3,n4,n5,opentime,addtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                pra=(cid,name,t1,t2,n1,n2,n3,n4,n5,t3,datetime.now())
                cursor.execute(sql,pra)
                t1=t1[2:]
                print n1,n2,n3,n4,n5,cid,t1
                php()
        else:
            if(rowa[10]!='1'):
                if(rowa[13]>5):
                    pass
                else:
					sqls='update ssc_data set sign=sign+1 where id ='+str(rowa[0])
					cursor.execute(sqls)
        return t1

import subprocess
import os
def php(code):
  # open process
  p = subprocess.Popen(['php'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

  # read output
  o = p.communicate(code)[0]

  # kill process
  try:
    os.kill(p.pid, os.signal.SIGTERM)
  except:
    pass

  # return
  return o

#autokj($n1,$n2,$n3,$n4,$n5,$cid,$t1,1);
# p2='58199'
# p1='140701089'
# p3=datetime.now()
#
# kjdata(t2=p2,cid='1',t1=p1,t3=p3)