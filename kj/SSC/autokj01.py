# coding=utf-8
import conn
import mysql.connector
from datetime import datetime

cnx=mysql.connector.connect(user='root',password='shl850325',host='54.254.174.234',database='shijue',charset='utf8')

cursor=cnx.cursor()

query='select * from ssc_set where lid=1'

cursor.execute(query)

result=cursor.fetchone()

print result

na=''
nb=''

def  autokj(n1,n2,n3,n4,n5,lid,issue,sign):
    if(sign==1):
        signa=1
        signb=2
    else:
        signa=0
        signb=0

    if(lid==1 or lid==2 or lid==3 or lid==4 or lid==10):
        kjcode=n1+n2+n3+n4+n5
    elif (lid==5 or lid==9):
        kjcode=n1.n2.n3
    elif (lid==6 or lid==7 or lid==8 or lid==11):
        kjcode=n1+" "+n2+" "+n3+" "+n4+" "+n5

    na[0]=n1
    na[1]=n2
    na[2]=n3
    na[3]=n4
    na[4]=n5

    nb[0]=n1
    nb[1]=n2
    nb[2]=n3
    nb[3]=n4
    nb[4]=n5

    for i in range(0,5):
        for j in range (4,j>i,-1):
            if (nb[j]<nb[j-1]):
                temp0=nb[j]
                nb[j]=nb[j-1]
                nb[j-1] =temp0
    sql='select * from ssc_bills where lotteryid='+lid+' and issue='+issue+' and zt=0 order by id asc'
    conn.cursor.execute (sql)
    #此处注意是赋值，还是比较
    row = conn.cursor.fetchall()
    while (row):
        uid_fx=row['uid']
        regup_fx=row['regup']
        mid=row['mid']
        if (row['mode']=='1'):
            modes=1
        elif (row['mode']=='2'):
            modes=0.1
        elif (row['mode']=="3"):
            modes=0.01
        #五星
        if(mid=="400" or mid=="420" or mid=="440" or mid=="460"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==5):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
				conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前四
        elif (mid=="401" or mid=="421" or mid=="441" or mid=="461"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==4):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
				conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后四
        elif (mid=="402" or mid=="422" or mid=="442" or mid=="462"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==4):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三
        elif(mid=="403" or mid=="423" or mid=="443" or mid=="463"):
            #中三单式
            if(row['type']=="input"):
                cs=n2+n3+n4
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            #中三复式
            elif (row['type']=="digital"):
                stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==4):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三和值
        elif (mid=="404" or mid=="424" or mid=="444" or mid=="464"):
            zt=2
            cs=n2+n3+n4
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中组三
        elif (mid=="405" or mid=="425" or mid=="445" or mid=="465"):
            nums=0
            if(n2==n3 or n2==n4 or n3==n4):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n2 or stra[i]==n3 or stra[i]==n4):
                        nums=nums+1
            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中组六
        elif(mid=="406" or mid=="426" or mid=="446" or mid=="466"):
            nums=0
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==n2 or stra[i]==n3 or stra[i]==n4):
                    nums=nums+1
            if(nums>=3):
				conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三组选，混合 inputok 168时时乐混合组选 298 3d 326p3
        elif (mid=="407" or mid=="427" or mid=="447" or mid=="467"):
            zt=2
            if (row['codes'].find(n2+n3+n4)==-1 and row['codes'].find(n2+n4+n3)==-1 and row['codes'].find(n3+n2+n4)==-1 and row['codes'].find(n3+n4+n2)==-1 and row['codes'].find(n4+n2+n3)==-1 and row['codes'].find(n4+n3+n2)==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split('')
                #组三
                if(n2==n3 or n2==n4 or n3==n4):
					conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str((rates[0]*modes))+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str(rates[1]*modes)+"*times where id="+row['id'])
        #中三组合值
        elif(mid=="408" or mid=="428" or mid=="448" or mid=="468"):
            zt=2
            cs=n2+n3+n4
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                rates=Get_rate(mid).split('&')
                #组3
                if(n2==n3 or n2==n4 or n3==n4):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str((rates[0]*modes))+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str(rates[1]*modes)+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #百家乐
        elif (mid=="409" or mid=="429" or mid=="449" or mid=="469"):
            na1a="zzz"
            na2a="zzz"
            na3a="zzz"
            na4a="zzz"
            na1b="zzz"
            na2b="zzz"
            na3b="zzz"
            na4b="zzz"

            if(n1+n2>n4+n5):
                na1a="庄闲"
            if(n1+n2<n4+n5):
                na1b="庄闲"

            if(n1==n2):
                na2a="对子"
            if(n4==n5):
                na2b="对子"

            if(n1==n2 and n1==n3):
                na3a="豹子"
            if(n3==n4 and n4==n5):
                na3b="豹子"

            if(n1+n2==8 or n1+n2==9):
                na4a="天王"
            if(n4+n5==8 or n4+n5==9):
                na4b="天王"

            stra=row['codes'].split('|')
            numa=0
            strb=stra[0].split('&')
            rates=Get_rate(mid).split("")

            for ii in range(0,len(strb)):
                if(strb[ii]==na1a):
                    numa=numa+rates[0]
                elif (strb[ii]==na2a):
                    numa=numa+rates[1]
                elif(strb[ii]==na3a):
                    numa=numa+rates[2]
                elif(strb[ii]==na4a):
                    numa=numa+rates[3]

            strb=stra[1].split("&")
            for ii in range(0,len((strb))):
                if(strb[ii]==na1b):
                    numa=numa+rates[0]
                elif(strb[ii]==na2b):
                    numa=numa+rates[1]
                elif(strb[ii]==na3b):
                    numa=numa+rates[2]
                elif(strb[ii]==na4b):
                    numa=numa+rates[3]

            if(numa>0):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+numa*modes+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #任三
        elif(mid=="410" or mid=="430" or mid=="450" or mid=="470"):
            stra=row['codes'].split("|")
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split("&")
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #任二
        elif(mid=="411" or mid=="431" or mid=="451" or mid=="471"):
            stra=row['codes'].split("|")
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split("&")
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1

            if(nums==2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前三直选ok164时时乐2943d 322p3
        elif(mid=="14" or mid=="52" or mid=="90" or mid=="128" or mid=="164" or mid=="294" or mid=="322"):
            #单式
            if(row['type']=="input"):
                cs=n1.n2.n3
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
             #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split("|")
                nums=0

                for i in range(0,len(stra)):
                strb=stra[i].split("&")
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1

                if(nums==3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前三和值ok165时时乐直选合值 295 3d 323p3
        elif(mid=="15" or mid=="53" or mid=="91" or mid=="129" or mid=="165" or mid=="295" or mid=="323"):
            zt=2
            cs=n1+n2+n3
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break


            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三直选
        elif(mid=="16" or mid=="54" or mid=="92" or mid=="130"):
            #单式
            if(row['type']=="input"):
                cs=n3.n4.n5
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split("|")
                nums=0
                for i in range(0,len(stra)):
                    strb=stra[i].split("&")
                    for ii in range(0,len(strb)):
                        if(strb[ii]==na[i+2]):
                            nums=nums+1

                if(nums==3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三和
        elif(mid=="17" or mid=="55" or mid=="93" or mid=="131"):
            zt=2
            cs=n3+n4+n5
            stra=stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break

            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前组三ok 166时时乐组3 296 3d 324 p3
        elif(mid=="18" or mid=="56" or mid=="94" or mid=="132" or mid=="166" or mid=="296" or mid=="324"):
            nums=0
            if(n1==n2 or n1==n3 or n2==n3):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):
                        nums=nums+1

            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前组六ok 167时时乐组6 297 3d 325 p3
        elif(mid=="19" or mid=="57" or mid=="95" or mid=="133" or mid=="167" or mid=="297" or mid=="325"):
            nums=0
            if(n1!=n2 and n1!=n3 and n2!=n3):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):
                        nums=nums+1

            if(nums>=3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
         #前三组选，混合 inputok 168时时乐混合组选 298 3d
        elif(mid=="20" or mid=="58" or mid=="96" or mid=="134" or mid=="168" or mid=="298" or mid=="326"):
            zt=2
            if((n1+n2+n3).find(row['codes'])==-1 and (n1+n3+n2).find(row['codes'])==-1 && (n2+n1+n3).find(row['codes'])==-1 and (n2+n3+n1).find(row['codes'])==-1 and (n3+n1+n2).find(row['codes'])==-1 and (n3+n2+n1).find(row['codes'])==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split("")
                #组三
                if(n1==n2 or n1==n3 or n2==n3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

        #前三组合值ok 169时时乐组合值 299 3d 327 p3
        elif(mid=="21" or mid=="59" or mid=="97" or mid=="135" or mid=="169" or mid=="299" or mid=="327"):
            zt=2
            cs=n1+n2+n3
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break

            if(zt=="1"):
                rates=Get_rate(mid).split("")
                #组3
                if(n1==n2 or n1==n3 or n2==n3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组三
        elif(mid=="22" or mid=="60" or mid=="98" or mid=="136"):
            nums=0
            if(n3==n4 or n3==n5 or n4==n5):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                        nums=nums+1
            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组6
        elif(mid=="23" or mid=="61" or mid=="99" or mid=="137"):
            nums=0
            #if(n3!=n4 and n3!=n5 and n4!=n5):
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1
            if(nums>=3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组混合
        elif(mid=="24" or mid=="62" or mid=="100" or mid=="138"):
            zt=2
            if((n3+n4+n5).find(row['codes'])==-1 and (n3+n5+n4).find(row['codes'])==-1 and (n4+n3+n5).find(row['codes'])==-1 and (n4+n5+n3).find(row['codes'])==-1 and (n5+n3+n4).find(row['codes'])==-1 and (n1+n2+n3).find(row['codes'])==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split("")
                #组三
                if(n3==n4 or n3==n5 or n4==n5):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])


        #后三组合值
        elif(mid=="25" or mid=="63" or mid=="101" or mid=="139"):
            zt=2
            cs=n3+n4+n5
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                rates=Get_rate(mid).split("")
                #组3
                if(n3==n4 or n3==n5 or n4==n5):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

        #一码不定位ok
        elif(mid=="26" or mid=="64" or mid=="102" or mid=="140"):
            nums=0
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1

            if(nums>=1):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*nums"+" where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #二码不定位ok
        elif(mid=="27" or mid=="65" or mid=="103" or mid=="141"):
            nums=0
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1

            if(nums==2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*nums"+" where id="+row['id'])
            elif(nums==3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*3"+" where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前二直选 172时时乐前2直 302 3d 330p3
        elif(mid=="28" or mid=="66" or mid=="104" or mid=="142" or mid=="172" or mid=="302" or mid=="330"):
            #单式
            if(row['type']=="input"):
                cs=n1+n2
                #pos= strpos(row['codes'],cs)
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times"+" where id="+row['id'])
            #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split('&')
                nums=0
                for i in range(0,len(stra)):
                    strb=stra[i].split('&')
                    for ii in range(0,len(strb)):
                        if(strb[ii]==na[i]):
                            nums=nums+1

                if(nums==2):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times"+" where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
				
					
		else if(mid=="29" or mid=="67" or mid=="105" or mid=="143" or mid=="331")://后二直选 331p3
			if(row['type']=="input")://单式
				cs=n4.n5
				if(strpos(row['codes'],cs)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				
			else if(row['type']=="digital")://复式
				stra=explode("|",row['codes'])
				nums=0
				for (i=0 i<count(stra) i++) :
					strb=explode("&",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==na[i+3]):nums=nums+1
					
				
				if(nums==2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
					
		else if(mid=="30" or mid=="68" or mid=="106" or mid=="144" or mid=="174" or mid=="304" or mid=="332")://前二组选 174时时乐前二组 304 3d 332p3
			if(row['type']=="input")://单式
				if(strpos(row['codes'],n1.n2)===false && strpos(row['codes'],n2.n1)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")					
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==n1 or stra[i]==n2):nums=nums+1
				
				if(nums>=2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="31" or mid=="69" or mid=="107" or mid=="145" or mid=="333")://后二组选 333p3
			if(row['type']=="input")://单式
				if(strpos(row['codes'],n4.n5)===false && strpos(row['codes'],n5.n4)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")					
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
							
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==n4 or stra[i]==n5):nums=nums+1
				
				if(nums>=2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="32" or mid=="33" or mid=="34" or mid=="35" or mid=="36" or mid=="70" or mid=="71" or mid=="72" or mid=="73" or mid=="74" or mid=="108" or mid=="109" or mid=="110" or mid=="111" or mid=="112" or mid=="146" or mid=="147" or mid=="148" or mid=="149" or mid=="150" or mid=="176" or mid=="177" or mid=="178" or mid=="306" or mid=="307" or mid=="308" or mid=="334" or mid=="335" or mid=="336" or mid=="337" or mid=="338")://定位胆ok 176时时乐 306 3d 334 p3
//			stra=explode("|",row['codes'])
//			nums=0
//			for (i=0 i<count(stra) i++) :
//				strb=explode("&",stra[i])
//				for (ii=0 ii<count(strb) ii++) :
//					if(strb[ii]==na[i]):nums=nums+1
//				
//			
//			
			
			
			//xc添加
			if(mid=="32" or mid=="70" or mid=="108" or mid=="146" or mid==334)://万位
				nums=0
				strb=explode("&",row['codes'])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==na[0]):nums=nums+1
				
			else if(mid=="33" or mid=="71" or mid=="109" or mid=="147" or mid==335)://千位
				nums=0
				strb=explode("&",row['codes'])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==na[1]):nums=nums+1
				
			else if(mid=="34" or mid=="72" or mid=="110" or mid=="148" or mid==336 or mid==176 or mid==306)://百位
				nums=0
				strb=explode("&",row['codes'])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==na[2]):nums=nums+1
				
			else if(mid=="35" or mid=="73" or mid=="111" or mid=="149" or mid==337 or mid==177 or mid==307)://十位
				nums=0
				strb=explode("&",row['codes'])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==na[3]):nums=nums+1
				
			else if(mid=="36" or mid=="74" or mid=="112" or mid=="150" or mid==338 or mid==178 or mid==308)://个位
				nums=0
				strb=explode("&",row['codes'])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==na[4]):nums=nums+1
				
			
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="37" or mid=="75" or mid=="113" or mid=="151" or mid=="179" or mid=="309" or mid=="335")://前二大小单双 179时时乐 309 3d 335 p3
			if(n1>4):na1a="大"else:na1a="小"
			if (n1%2==1):na1b="单"else:na1b="双"
			if(n2>4):na2a="大"else:na2a="小"
			if (n2%2==1):na2b="单"else:na2b="双"
			stra=explode("|",row['codes'])
			numa=0
			numb=0
			strb=explode("&",stra[0])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na1a or strb[ii]==na1b):numa=numa+1
			
			strb=explode("&",stra[1])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na2a or strb[ii]==na2b):numb=numb+1
			
//			echo row['codes'].numb."<br>"
			nums=numa*numb
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="38" or mid=="76" or mid=="114" or mid=="152" or mid=="336")://后二大小单双ok 336 p3
			if(n4>4):na1a="大"else:na1a="小"
			if (n4%2==1):na1b="单"else:na1b="双"
			if(n5>4):na2a="大"else:na2a="小"
			if (n5%2==1):na2b="单"else:na2b="双"
			stra=explode("|",row['codes'])
			numa=0
			numb=0
			strb=explode("&",stra[0])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na1a or strb[ii]==na1b):numa=numa+1
			
			strb=explode("&",stra[1])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na2a or strb[ii]==na2b):numb=numb+1
			
//			echo numa.row['codes'].numb."<br>"
			
			nums=numa*numb
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		/////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
		else if(mid=="170" or mid=="300" or mid=="328")://时时乐一码不定位ok 300 3d 328 p3
			nums=0
			stra=explode("&",row['codes'])
			for (i=0 i<count(stra) i++) :
				if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):nums=nums+1
			
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="171" or mid=="301" or mid=="329")://时时乐二码不定位ok 301 3d 329 p3
			nums=0
			stra=explode("&",row['codes'])
			for (i=0 i<count(stra) i++) :
				if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):nums=nums+1
			
			if(nums==2):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
			else if(nums==3):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*3 where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="173" or mid=="303")://时时乐后二直选 303 3d
			if(row['type']=="input")://单式
				cs=n2.n3
				if(strpos(row['codes'],cs)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				
			else if(row['type']=="digital")://复式
				stra=explode("|",row['codes'])
				nums=0
				for (i=0 i<count(stra) i++) :
					strb=explode("&",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==na[i+1]):nums=nums+1
					
				
				if(nums==2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
							
		else if(mid=="175" or mid=="305")://时时乐后二组选 305 3d
			if(row['type']=="input")://单式
				if(strpos(row['codes'],n2.n3)===false && strpos(row['codes'],n3.n2)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")					
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
							
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==n2 or stra[i]==n3):nums=nums+1
				
				if(nums>=2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="180" or mid=="310")://时时乐后二大小单双ok	310 3d
			if(n2>4):na1a="大"else:na1a="小"
			if (n2%2==1):na1b="单"else:na1b="双"
			if(n3>4):na2a="大"else:na2a="小"
			if (n3%2==1):na2b="单"else:na2b="双"
			stra=explode("|",row['codes'])
			numa=0
			numb=0
			strb=explode("&",stra[0])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na1a or strb[ii]==na1b):numa=numa+1
			
			strb=explode("&",stra[1])
			for (ii=0 ii<count(strb) ii++) :
				if(strb[ii]==na2a or strb[ii]==na2b):numb=numb+1
			
//			echo numa.row['codes'].numb."<br>"
			
			nums=numa*numb
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
						
			///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		else if(mid=="197" or mid=="231" or mid=="265" or mid=="357")://115前三直选
			if(row['type']=="input")://单式
				cs=sprintf("%02d",n1)." ".sprintf("%02d",n2)." ".sprintf("%02d",n3)
				pos= strpos(row['codes'],cs)
				if(strpos(row['codes'],cs)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				
			else if(row['type']=="digital")://复式
				stra=explode("|",row['codes'])
				nums=0
				for (i=0 i<count(stra) i++) :
					strb=explode("&",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==sprintf("%02d",na[i])):nums=nums+1
					
				
				if(nums==3):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="198" or mid=="232" or mid=="266" or mid=="358")://115前三组选
			if(row['type']=="input")://单式
				zt=2
				if(strpos(row['codes'],sprintf("%02d",n1)." ".sprintf("%02d",n2)." ".sprintf("%02d",n3))===false && strpos(row['codes'],sprintf("%02d",n1)." ".sprintf("%02d",n3)." ".sprintf("%02d",n2))===false && strpos(row['codes'],sprintf("%02d",n2)." ".sprintf("%02d",n1)." ".sprintf("%02d",n3))===false && strpos(row['codes'],sprintf("%02d",n2)." ".sprintf("%02d",n3)." ".sprintf("%02d",n1))===false && strpos(row['codes'],sprintf("%02d",n3)." ".sprintf("%02d",n1)." ".sprintf("%02d",n2))===false && strpos(row['codes'],sprintf("%02d",n3)." ".sprintf("%02d",n2)." ".sprintf("%02d",n1))===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")					
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")										
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3)):nums=nums+1
				
				if(nums>=3):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="199" or mid=="233" or mid=="267" or mid=="359")://115前二直选
			if(row['type']=="input")://单式
				cs=sprintf("%02d",n1)." ".sprintf("%02d",n2)
				if(strpos(row['codes'],cs)===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				
			else if(row['type']=="digital")://复式
				stra=explode("|",row['codes'])
				nums=0
				for (i=0 i<count(stra) i++) :
					strb=explode("&",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==sprintf("%02d",na[i])):nums=nums+1
					
				
				if(nums==2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="200" or mid=="234" or mid=="268" or mid=="360")://115前二组选
			if(row['type']=="input")://单式
				if(strpos(row['codes'],sprintf("%02d",n1)." ".sprintf("%02d",n2))===false && strpos(row['codes'],sprintf("%02d",n2)." ".sprintf("%02d",n1))===false):
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")					
				else:
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2)):nums=nums+1
				
				if(nums>=2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="201" or mid=="235" or mid=="269" or mid=="361")://115前三不定位ok
			nums=0
			stra=explode("&",row['codes'])
			for (i=0 i<count(stra) i++) :
				if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3)):nums=nums+1
			
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="202" or mid=="236" or mid=="270" or mid=="362")://定位胆ok 
			stra=explode("|",row['codes'])
			nums=0
			for (i=0 i<count(stra) i++) :
				strb=explode("&",stra[i])
				for (ii=0 ii<count(strb) ii++) :
					if(strb[ii]==sprintf("%02d",na[i])):nums=nums+1
				
			
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="205" or mid=="239" or mid=="273" or mid=="365")://定单双
			numa=0
			if (n1%2==0):numa=numa+1
			if (n2%2==0):numa=numa+1
			if (n3%2==0):numa=numa+1
			if (n4%2==0):numa=numa+1
			if (n5%2==0):numa=numa+1
			numstr=(5-numa)."单".numa."双"
			rates=explode("",Get_rate(mid))
			if(strpos(row['codes'],numstr)===false):
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
			else:
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=".(rates[numa]*modes)."*times where id='".row['id']."'")
			
		else if(mid=="206" or mid=="240" or mid=="274" or mid=="367")://猜中位
			rates=explode("",Get_rate(mid))
			nums=nb[2]
			if(strpos(row['codes'],strval(nums))===false)://字符类型转换
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
			else:
				if(nums>6):
					nums=12-nums
				
//			echo nums
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=".(rates[nums-3]*modes)."*times where id='".row['id']."'")
			
//			echo nb[2]
		else if(mid=="207" or mid=="241" or mid=="275" or mid=="368")://任选1中1
			nums=0
			stra=explode("&",row['codes'])
			for (i=0 i<count(stra) i++) :
				if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5)):nums=nums+1
			
			if(nums>=1):
				conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
			else:
				conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
			
		else if(mid=="208" or mid=="242" or mid=="276" or mid=="369")://任选2中2
			if(row['type']=="input")://单式
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					numa=0
					strb=explode(" ",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==sprintf("%02d",n1) or strb[ii]==sprintf("%02d",n2) or strb[ii]==sprintf("%02d",n3) or strb[ii]==sprintf("%02d",n4) or strb[ii]==sprintf("%02d",n5)):numa=numa+1
					
					if(numa>=2):nums=nums+1
				
				if(nums>=1):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5)):nums=nums+1
				
				if(nums>=2):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".(nums*(nums-1)/2)." where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="209" or mid=="243" or mid=="277" or mid=="370")://任选3中3
			if(row['type']=="input")://单式
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					numa=0
					strb=explode(" ",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==sprintf("%02d",n1) or strb[ii]==sprintf("%02d",n2) or strb[ii]==sprintf("%02d",n3) or strb[ii]==sprintf("%02d",n4) or strb[ii]==sprintf("%02d",n5)):numa=numa+1
					
					if(numa>=3):nums=nums+1
				
				if(nums>=1):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5)):nums=nums+1
				
				if(nums>=3):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".(nums*(nums-1)*(nums-2)/6)." where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="210" or mid=="244" or mid=="278" or mid=="371")://任选4中4
			if(row['type']=="input")://单式
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					numa=0
					strb=explode(" ",stra[i])
					for (ii=0 ii<count(strb) ii++) :
						if(strb[ii]==sprintf("%02d",n1) or strb[ii]==sprintf("%02d",n2) or strb[ii]==sprintf("%02d",n3) or strb[ii]==sprintf("%02d",n4) or strb[ii]==sprintf("%02d",n5)):numa=numa+1
					
					if(numa>=4):nums=nums+1
				
				if(nums>=1):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")						
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++) :
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5)):nums=nums+1
				
				if(nums>=4):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".(nums*(nums-1)*(nums-2)*(nums-3)/24)." where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")		
				
			
		else if(mid=="211" or mid=="245" or mid=="279" or mid=="372")://任选5中5
			if(row['type']=="input")://单式
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++):
					numa=0
					strb=explode(" ",stra[i])
					for (ii=0 ii<count(strb) ii++):
						if(strb[ii]==sprintf("%02d",n1) or strb[ii]==sprintf("%02d",n2) or strb[ii]==sprintf("%02d",n3) or strb[ii]==sprintf("%02d",n4) or strb[ii]==sprintf("%02d",n5))
                            numa=numa+1
					if(numa>=5)
                        nums=nums+1
				if(nums>=1):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")				
		        else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++):
					if(stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5))
                        nums=nums+1
				if(nums>=5):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
			
        #任选6中5 75 85    
		else if(mid=="212" or mid=="213" or mid=="214" or mid=="246" or mid=="247" or mid=="248" or mid=="280" or mid=="281" or mid=="282" or mid=="373" or mid=="374" or mid=="375"):
			#单式
			if(row['type']=="input"):
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++):
					numa=0
					strb=explode(" ",stra[i])
					for (ii=0 ii<count(strb) ii++):
						if(strb[ii]==sprintf("%02d",n1) or strb[ii]==sprintf("%02d",n2) or strb[ii]==sprintf("%02d",n3) or strb[ii]==sprintf("%02d",n4) or strb[ii]==sprintf("%02d",n5)):
                            numa=numa+1
					if(numa>=5):
                            nums=nums+1
				if(nums>=1):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times*".nums." where id='".row['id']."'")				
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")
			else:
				nums=0
				stra=explode("&",row['codes'])
				for (i=0 i<count(stra) i++):
					if (stra[i]==sprintf("%02d",n1) or stra[i]==sprintf("%02d",n2) or stra[i]==sprintf("%02d",n3) or stra[i]==sprintf("%02d",n4) or stra[i]==sprintf("%02d",n5)):
                        nums=nums+1
				if(nums>=5):
					conn.cursor.execute("update ssc_bills set zt=".signa.",prize=rates*times where id='".row['id']."'")
				else:
					conn.cursor.execute("update ssc_bills set zt=".signb.",prize=0 where id='".row['id']."'")

		
		
		if(sign==1):
			sqls="update ssc_bills set kjcode='".kjcode."' where id ='".row['id']."'"
			rss=conn.cursor.execute(sqls) or  die("数据库修改出错1".mysql_error())
			
			sqls="select * from ssc_bills where id ='".row['id']."'"
			rss=conn.cursor.execute(sqls) or  die("数据库修改出错1".mysql_error())
			rows = mysql_fetch_array(rss)
			if(rows['zt']==1):	
				sqla = "select * from ssc_record order by id desc limit 1"
				rsa = conn.cursor.execute(sqla)
				rowa = mysql_fetch_array(rsa)
				dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))
				lmoney = Get_mmoney(rows['uid'])+rows['prize']
				sqla="insert into ssc_record set lotteryid='".rows['lotteryid']."', lottery='".rows['lottery']."', dan='".dan1."', dan1='".rows['dan']."', dan2='".rows['dan1']."', uid='".rows['uid']."', username='".rows['username']."', issue='".rows['issue']."', types='12', mid='".rows['mid']."', mode='".rows['mode']."', smoney=".rows['prize'].",leftmoney=".lmoney.", cont='".rows['cont']."', regtop='".rows['regtop']."', regup='".rows['regup']."', regfrom='".rows['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
				exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
				
				sqla="update ssc_member set leftmoney=".lmoney." where id='".rows['uid']."'" 
				exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
				
				if(rows['dan1']!=""):
					sqla = "update ssc_zbills set prize=prize+".rows['prize'].", zjnums=zjnums+1 where dan='".rows['dan1']."'"
					rsa = conn.cursor.execute(sqla)
                    
				#多余转结
				if(rows['autostop']=="yes"):
					sqla="select sum(money) as tmoney,count(*) as cnums from ssc_zdetail where zt=0 and dan='".rows['dan1']."'"
					rsa = conn.cursor.execute(sqla)
					rowa = mysql_fetch_array(rsa)
					ttm=rowa['tmoney']
					if(ttm>0):
						sqla = "update ssc_zbills set cnums=cnums+".rowa['cnums'].", cmoney=cmoney+".ttm." where dan='".rows['dan1']."'"
						rsa = conn.cursor.execute(sqla)

						sqla = "select * from ssc_record order by id desc limit 1"
						rsa = conn.cursor.execute(sqla)
						rowa = mysql_fetch_array(rsa)
						dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))//追号返款
						sqla="insert into ssc_record set lotteryid='".rows['lotteryid']."', lottery='".rows['lottery']."', dan='".dan1."', dan2='".rows['dan']."', uid='".rows['uid']."', username='".rows['username']."', issue='".rows['issue']."', types='10', mid='".rows['mid']."', mode='".rows['mode']."', smoney=".ttm.",leftmoney=".(lmoney+ttm).", cont='".rows['cont']."', regtop='".rows['regtop']."', regup='".rows['regup']."', regfrom='".rows['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
						exe=conn.cursor.execute(sqla) or  die("数据库修改出错9!!!".mysql_error())

						sqla="update ssc_member set leftmoney=".(lmoney+ttm)." where id='".rows['uid']."'" 
						exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
					
					sqla="update ssc_zdetail set zt=2 where dan='".rows['dan1']."' and zt=0" 
					exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
	
    
	if(sign==0):
		sqlb="select SUM(IF(types = 1, smoney, 0)) as t1,SUM(IF(types = 2, zmoney, 0)) as t2,SUM(IF(types = 3, smoney, 0)) as t3,SUM(IF(types = 7, zmoney, 0)) as t7,SUM(IF(types = 11, smoney, 0)) as t11,SUM(IF(types = 12, smoney, 0)) as t12,SUM(IF(types = 13, smoney, 0)) as t13,SUM(IF(types = 15, zmoney, 0)) as t15,SUM(IF(types = 16, zmoney, 0)) as t16,SUM(IF(types = 32, smoney, 0)) as t32,SUM(IF(types = 40, smoney, 0)) as t40 from ssc_record where lotteryid='".lid."' and issue='".issue."'"
		rsb = conn.cursor.execute(sqlb)
		rowb = mysql_fetch_array(rsb)
		sqlc="select SUM(prize) as zj from ssc_bills where lotteryid='".lid."' and issue='".issue."'"
		rsc = conn.cursor.execute(sqlc)
		rowc = mysql_fetch_array(rsc)
		sqld="insert into ssc_info set lotteryid='".lid."', lottery='".Get_lottery(lid)."', issue='".issue."', tz='".(rowb['t7']-rowb['t13'])."', fd='".(rowb['t11']-rowb['t15'])."', zj='".rowc['zj']."', adddate='".date("Y-m-d H:i:s")."'"
		exe=conn.cursor.execute(sqld) or  die("数据库修改出错!!!".mysql_error())
	#计分红 zh
	else if(sign==1):
		issueb=intval(issue)+1
		sqlb="select * from ssc_zdetail where lotteryid='".lid."' and issue='".issueb."' and zt=0"
		rsb = conn.cursor.execute(sqlb)
		while (rowb = mysql_fetch_array(rsb)):
			sqla = "update ssc_zbills set fnums=fnums+1, fmoney=fmoney+".rowb['money']." where dan='".rowb['dan']."'"
			rsa = conn.cursor.execute(sqla)
		
			sql = "select * from ssc_member where username='" . rowb['username'] . "'"
			rs = conn.cursor.execute(sql)
			row = mysql_fetch_array(rs)
			lmoney=row['leftmoney']
		    # point处理
			if(rowb['mid']=="20" or rowb['mid']=="21" or rowb['mid']=="24" or rowb['mid']=="25" or rowb['mid']=="58" or rowb['mid']=="59" or rowb['mid']=="62" or rowb['mid']=="63" or rowb['mid']=="96" or rowb['mid']=="97" or rowb['mid']=="100" or rowb['mid']=="101" or rowb['mid']=="134" or rowb['mid']=="135" or rowb['mid']=="138" or rowb['mid']=="139" or rowb['mid']=="168" or rowb['mid']=="169" or rowb['mid']=="205" or rowb['mid']=="206" or rowb['mid']=="239" or rowb['mid']=="240" or rowb['mid']=="273" or rowb['mid']=="274" or rowb['mid']=="298" or rowb['mid']=="299" or rowb['mid']=="326" or rowb['mid']=="327" or rowb['mid']=="366" or rowb['mid']=="367"):
				sstra=explode("",row['rebate'])
				sstrb=explode(",",sstra[sstri-1])
				spoint=sstrb[1]/100
			else:
				spoint=rowb['point']
		
			sqla = "select * from ssc_record order by id desc limit 1"
			rsa = conn.cursor.execute(sqla)
			rowa = mysql_fetch_array(rsa)
			dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))//追号返款
			sqla="insert into ssc_record set lotteryid='".rowb['lotteryid']."', lottery='".rowb['lottery']."', dan='".dan1."', dan2='".rowb['dan']."', uid='".rowb['uid']."', username='".rowb['username']."', issue='".rowb['issue']."', types='10', mid='".rowb['mid']."', mode='".rowb['mode']."', smoney=".rowb['money'].",leftmoney=".(lmoney+rowb['money']).", cont='".rowb['cont']."', regtop='".rowb['regtop']."', regup='".rowb['regup']."', regfrom='".rowb['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
			exe=conn.cursor.execute(sqla) or  die("数据库修改出错9!!!".mysql_error())

			sqla = "select * from ssc_bills order by id desc limit 1"
			rsa = conn.cursor.execute(sqla)
			rowa = mysql_fetch_array(rsa)
			dan2 = sprintf("%06s",strtoupper(base_convert(rowa['id']+1,10,36)))//转注单
						
			sqla="INSERT INTO ssc_bills set lotteryid='".rowb['lotteryid']."', lottery='".rowb['lottery']."', dan='".dan2."', dan1='".rowb['dan']."', uid='".rowb['uid']."', username='".rowb['username']."', issue='".rowb['issue']."', type='".rowb['type']."', mid='".rowb['mid']."', codes='".rowb['codes']."', nums='".rowb['nums']."', times='".rowb['times']."', money='".rowb['money']."', mode='".rowb['mode']."', rates='".rowb['rates']."', point='".rowb['point']."', cont='".rowb['cont']."', regtop='".rowb['regtop']."', regup='".rowb['regup']."', regfrom='".rowb['regfrom']."', userip='".rowb['userip']."', adddate='".date("Y-m-d H:i:s")."', canceldead='".rowb['canceldead']."', autostop='".rowb['autostop']."'"
			exe=conn.cursor.execute(sqla) or  die("数据库修改出错10!!!!".mysql_error())
			
			sqla = "update ssc_zdetail set danb='".dan2."', zt=1 where id='".rowb['id']."'"
			rsa = conn.cursor.execute(sqla)
						
			sqla = "select * from ssc_record order by id desc limit 1"
			rsa = conn.cursor.execute(sqla)
			rowa = mysql_fetch_array(rsa)
			dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))//投注扣款
			sqla="insert into ssc_record set lotteryid='".rowb['lotteryid']."', lottery='".rowb['lottery']."', dan='".dan1."', dan1='".dan2."', dan2='".rowb['dan']."', uid='".rowb['uid']."', username='".rowb['username']."', issue='".rowb['issue']."', types='7', mid='".rowb['mid']."', mode='".rowb['mode']."', zmoney=".rowb['money'].",leftmoney=".lmoney.", cont='".rowb['cont']."', regtop='".rowb['regtop']."', regup='".rowb['regup']."', regfrom='".rowb['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
			exe=conn.cursor.execute(sqla) or  die("数据库修改出错11!!!".mysql_error())
			
			if(spoint!="0"):
				sstrp=spoint*100
				sqla = "select * from ssc_record order by id desc limit 1"
				rsa = conn.cursor.execute(sqla)
				rowa = mysql_fetch_array(rsa)
				dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))
				sqla="insert into ssc_record set lotteryid='".rowb['lotteryid']."', lottery='".rowb['lottery']."', dan='".dan1."', dan1='".dan2."', dan2='".rowb['dan']."', uid='".rowb['uid']."', username='".rowb['username']."', issue='".rowb['issue']."', types='11', mid='".rowb['mid']."', mode='".rowb['mode']."', smoney=".rowb['money']*spoint.",leftmoney=".(lmoney+rowb['money']*spoint).", cont='".rowb['cont']."', regtop='".rowb['regtop']."', regup='".rowb['regup']."', regfrom='".rowb['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
				exe=conn.cursor.execute(sqla) or  die("数据库修改出错4!!!".mysql_error())

				sqla="update ssc_member set leftmoney=".(lmoney+rowb['money']*spoint)." where username='".rowb['username']."'" 
				exe=conn.cursor.execute(sqla) or  die("数据库修改出错12!!!".mysql_error())
							//上级返点
							
				if(rowb['regfrom']!=""):
					regfrom=explode("&&",rowb['regfrom'])
					for (ia=0 ia<count(regfrom) ia++):
									
						susername=str_replace("&","",regfrom[ia])
						sqla = "select * from ssc_member where username='".susername."'"
						rsa = conn.cursor.execute(sqla)
						rowa = mysql_fetch_array(rsa)
						sstra=explode("",rowa['rebate'])
									
						sstrb=explode(",",sstra[sstri-1])
						sstrc=explode("_",rstrb[0])
						if((sstrb[1]-sstrp)>0):
							sstrp=sstrb[1]

							sqla = "select * from ssc_record order by id desc limit 1"
							rsa = conn.cursor.execute(sqla)
							rowa = mysql_fetch_array(rsa)
							dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))
							sqla="insert into ssc_record set lotteryid='".rowb['lotteryid']."', lottery='".rowb['lottery']."', dan='".dan1."', dan1='".dan2."', dan2='".rowb['dan']."', uid='".Get_memid(susername)."', username='".susername."', issue='".rowb['issue']."', types='11', mid='".rowb['mid']."', mode='".rowb['mode']."', smoney=".(rowb['money']*(sstrb[1]-sstrp)/100).",leftmoney=".(Get_mmoney(susername)+rowb['money']*(sstrb[1]-sstrp)/100).", cont='".rowb['cont']."', regtop='".rowb['regtop']."', regup='".rowb['regup']."', regfrom='".rowb['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
							exe=conn.cursor.execute(sqla) or  die("数据库修改出错4!!!".mysql_error())
			
							sqla="update ssc_member set leftmoney=leftmoney+".(rowb['money']*(sstrb[1]-sstrp)/100)." where username='".susername."'" 
							exe=conn.cursor.execute(sqla) or  die("数据库修改出错12!!!".mysql_error())
		
		sqla="select * from ssc_zbills where lotteryid='".lid."' and zt='0'"
		rsa = conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
		while (rowa = mysql_fetch_array(rsa)):
			sqlb="select * from ssc_zdetail where dan='".rowa['dan']."' and zt='0'"
			rsb = conn.cursor.execute(sqlb) or  die("数据库修改出错!!!".mysql_error())
			total = mysql_num_rows(rsb)
			if(total==0):
				sqlb="update ssc_zbills set zt='1' where dan='".rowa['dan']."'"
				exe=conn.cursor.execute(sqlb) or  die("数据库修改出错!!!".mysql_error())
		
		
# 投注佣金返利开始
sql_jc = "select * from ssc_huodong where id=1"
rs_jc = conn.cursor.execute(sql_jc)
row_jc = mysql_fetch_array(rs_jc)
if(row_jc['kg']==1):
#每日领取一次
sql_jc1 = "select * from ssc_record where uid_xj='uid_fx' and types='70' and  adddate like '%".date("Y-m-d")."%'"	
rs_jc1 = conn.cursor.execute(sql_jc1)
row_jc1 = mysql_fetch_array(rs_jc1)

sql_jc2 = "select sum(zmoney) sum_tj from ssc_record where uid='uid_fx' and types='7' and  adddate like '%".date("Y-m-d")."%'"	
rs_jc2 = conn.cursor.execute(sql_jc2)
row_jc2 = mysql_fetch_array(rs_jc2)
	if (!isset(row_jc1['id']) && row_jc2['sum_tj']>=500):
		sqla = "select * from ssc_member WHERE username='" . regup_fx . "'"
		rsa = conn.cursor.execute(sqla)
		rowa = mysql_fetch_array(rsa)
		leftmoney=rowa['leftmoney']
        #帐变
		sqlc = "select * from ssc_record order by id desc limit 1" 
		rsc = conn.cursor.execute(sqlc)
		rowc = mysql_fetch_array(rsc)
		dan1 = sprintf("%07s",strtoupper(base_convert(rowc['id']+1,10,36)))
			lmoney=row_jc['jieguo']
			leftmoney=rowa['leftmoney']+lmoney
		
			sqla="insert into ssc_record set dan='".dan1."', uid='".rowa['id']."', username='".rowa['username']."', types='70', smoney=".lmoney.",leftmoney=".leftmoney.", regtop='".rowa['regtop']."', regup='".rowa['regup']."', regfrom='".rowa['regfrom']."', adddate='".date("Y-m-d H:i:s")."',uid_xj='uid_fx'"
			exe=conn.cursor.execute(sqla) or  die("数据库修改出错6!!!".mysql_error())
			sqlb="insert into ssc_savelist set uid='".rowa['id']."', username='".rowa['username']."', bank='投注佣金返利', bankid='0', cardno='', money=".lmoney.", sxmoney='0', rmoney=".lmoney.", adddate='".date("Y-m-d H:i:s")."',zt='1',types='70'"
			exe=conn.cursor.execute(sqlb) or  die("数据库修改出错6!!!".mysql_error())
			sql="update ssc_member set leftmoney =(leftmoney+".lmoney."),totalmoney=(totalmoney+".lmoney.") where id ='".rowa['id']."'"
			exe=conn.cursor.execute(sql) or  die("数据库修改出错6!!!".mysql_error())
		
//投注佣金返利结束
		
# //分红
# //sqlb="select regtop, SUM(IF(types = 1, smoney, 0)) as t1,SUM(IF(types = 2, zmoney, 0)) as t2,SUM(IF(types = 3, smoney, 0)) as t3,SUM(IF(types = 7, zmoney, 0)) as t7,SUM(IF(types = 11, smoney, 0)) as t11,SUM(IF(types = 12, smoney, 0)) as t12,SUM(IF(types = 13, smoney, 0)) as t13,SUM(IF(types = 15, zmoney, 0)) as t15,SUM(IF(types = 16, zmoney, 0)) as t16,SUM(IF(types = 32, smoney, 0)) as t32,SUM(IF(types = 40, smoney, 0)) as t40 from ssc_record where lotteryid='".lid."' and issue='".issue."' group by regtop"
# //rsb = conn.cursor.execute(sqlb)
# //		while (rowb = mysql_fetch_array(rsb)):
# //			if(rowb['regtop']!=""):
# //				sqls="select * from ssc_member where username ='".rowb['regtop']."'"
# //				rss=conn.cursor.execute(sqls) or  die("数据库修改出错1".mysql_error())
# //				rows = mysql_fetch_array(rss)
# //				zmoney = rows['zc']*(row['t7']-row['t11']-row['t12']-row['t13']+row['t15']+row['t16'])/100
# //				lmoney = rows['leftmoney']+zmoney
# //			
# //				sqla = "select * from ssc_record order by id desc limit 1"
# //				rsa = conn.cursor.execute(sqla)
# //				rowa = mysql_fetch_array(rsa)
# //				dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))
# //			
# //				sqla="insert into ssc_record set lotteryid='".lid."', lottery='".Get_lottery(lid)."', dan='".dan1."', uid='".rows['uid']."', username='".rowb['regtop']."', issue='".issue."', types='40', smoney=".zmoney.",leftmoney=".lmoney.", adddate='".date("Y-m-d H:i:s")."'"
# //				exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
# //				
# //				sqla="update ssc_member set leftmoney=".lmoney." where username='".rowb['regtop']."'" 
# //				exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
# //			
# //				
	
def Get_rate(rrr):
    result=conn.cursor.execute('Select * from ssc_class where mid='+rrr)
    raa=conn.cursor.fetchall(result)
    return raa['rates']