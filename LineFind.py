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
	eqip = []
	typeDish = []
	parameter = []

	for i in range(4): eqip.append(random.choice([True,False]))
	for i in range(4): typeDish.append(random.choice([True,False]))
	for i in range(4): parameter.append(random.choice([True,False])) 

	return [random.randint(5,120), #time
	random.randint(-1,20), #kichen
	random.randint(-1,2), #meal
	random.randint(-1,3), #challange
	random.choice([-1,True,False]), #smallCost
	random.choice([-1,True,False]), #exotic
	eqip,
	typeDish,
	parameter]

def lineReqestPars(reqest): #make string sql-command
	s = ""
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
		s+= "challange = " + str(reqest[3])
	if(reqest[4]!=-1):
		if s: s+= " and "
		s+= "smallCost"
	if(reqest[5]!=-1):
		if s: s+= " and "
		s+= "exotic"

	if(reqest[6][0]):
		if s: s+= " and "
		s+= "eqip[0]"
	if(reqest[6][1]):
		if s: s+= " and "
		s+= "eqip[1]"
	if(reqest[6][2]):
		if s: s+= " and "
		s+= "eqip[2]"
	if(reqest[6][3]):
		if s: s+= " and "
		s+= "eqip[3]"

	if(reqest[7][0]):
		if s: s+= " and "
		s+= "typeDish[0]"
	if(reqest[7][1]):
		if s: s+= " and "
		s+= "typeDish[1]"
	if(reqest[7][2]):
		if s: s+= " and "
		s+= "typeDish[2]"
	if(reqest[7][3]):
		if s: s+= " and "
		s+= "typeDish[3]"

	if(reqest[8][0]):
		if s: s+= " and "
		s+= "parameter[0]"
	if(reqest[8][1]):
		if s: s+= " and "
		s+= "parameter[1]"
	if(reqest[8][2]):
		if s: s+= " and "
		s+= "parameter[2]"
	if(reqest[8][3]):
		if s: s+= " and "
		s+= "parameter[3]"


	return s 

def lineFind(s): #(0.002 - 0.003)
	if s: cur.execute("select name from testbd where " + s + ";")
	else: cur.execute("select name from testbd;")
	

#check test reqest
someReqest = []
for i in range(10):
	print("")
	someReqest.append(randomList()) 
	print(someReqest[i])

	start = time.time()
	s = lineReqestPars(someReqest[i])
	print("%.10f" % (time.time()-start)) #pars time

	start = time.time()
	lineFind(s)
	print("%.10f" % (time.time()-start)) #find time 

	base = cur.fetchall()
	for j in base: print(j)

cur.close()
conn.close()