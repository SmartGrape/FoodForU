import psycopg2
import random

try:
    conn = psycopg2.connect("dbname='postgres' user='tester' host='localhost' password='hardpass'")
    print ("connect")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()


for j in range(5000):
	name = "name" + str(j)
	time = random.randint(1,120)
	kcal = random.randint(1, 10000)
	kitchen = random.randint(0,20)
	challange = random.randint(0,3)
	exotic = random.choice([True,False])
	smallCost = random.choice([True,False])

	eqip = []
	parameter = []
	typeDish = []
	meal = 0 
	for i in range(4): eqip.append(random.choice([True,False]))
	for i in range(4): parameter.append(random.choice([True,False]))
	for i in range(4): typeDish.append(random.choice([True,False]))
	for i in range(4): meal += 2**i * random.randint(0,1)

	components = []
	massComp = []
	for i in range(random.randint(3,15)):
		components.append(random.randint(0,1000))
		massComp.append(random.randint(1,1000))


	cur.execute("""
			INSERT INTO testbd (name, kcal, time, kitchen, meal, typeDish, parameter, challange, exotic, smallCost, eqip, components, massComp) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
			""",
			(name, kcal, time, kitchen, meal, typeDish, parameter, challange, exotic, smallCost, eqip, components, massComp))



conn.commit()
cur.close()
conn.close()
print('completed')




