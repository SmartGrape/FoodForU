import psycopg2
import time
import random

try:
    conn = psycopg2.connect("dbname='postgres' user='tester' host='localhost' password='hardpass'")
    print ("connect")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()


def randomList(): #for test (-1 = null, without tag)
	eqip = [];
	for i in range(4): eqip.append(random.randint(0,1)) 

	return [random.randint(5,120), #time
	random.randint(-1,20), #kichen
	random.randint(0,2), #meal
	random.randint(-1,3), #typeDish
	random.randint(-1,4), #parameter
	random.randint(-1,3), #challange
	random.choice([-1,True,False]), #smallCost
	random.choice([-1,True,False]), #exotic
	eqip ]

def reqestPars(reqest): #make string sql-command
	s = ""
	#print(reqest)
	if(reqest[0]!=-1):
		s+= "time <= " + str(reqest[0])
	if(reqest[1]!=-1):
		if s: s+= " and "
		s+= "kitchen = " + str(reqest[1])
	if(reqest[2]!=-1):
		if s: s+= " and "
		s+= "(meal >> " + str(reqest[2]) + " & 1) = 1"

	if(reqest[3]!=-1):
		if s: s+= " and "
		s+= "typeDish = " + str(reqest[3])
	if(reqest[4]!=-1):
		if s: s+= " and "
		s+= "parameter = " + str(reqest[4])
	if(reqest[5]!=-1):
		if s: s+= " and "
		s+= "challange = " + str(reqest[4])
	if(reqest[6]!=-1):
		if s: s+= " and "
		s+= "smallCost"
	if(reqest[7]!=-1):
		if s: s+= " and "
		s+= "exotic"

	if(reqest[8][0] == 1): s+= " and eqip[0] = 1"
	if(reqest[8][1] == 1): s+= " and eqip[1] = 1"
	if(reqest[8][2] == 1): s+= " and eqip[2] = 1"
	if(reqest[8][3] == 1): s+= " and eqip[3] = 1"

	return s 

def lineFind(s):
	if s: cur.execute("select name from testbd where " + s + ";")
	else: cur.execute("select name from testbd;")
	

#check test reqest
someReqest = []
for i in range(10):
	print("")
	someReqest.append(randomList()) 
	print(someReqest[i])

	start = time.time()
	s = reqestPars(someReqest[i])
	print("%.10f" % (time.time()-start)) #pars time

	start = time.time()
	lineFind(s)
	print("%.10f" % (time.time()-start)) #find time

	base = cur.fetchall()
	for j in base: print(j)