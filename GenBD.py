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
	typeDish = random.randint(0,3)
	parameter = random.randint(0,4)
	challange = random.randint(0,3)
	exotic = random.choice([True,False])
	smallCost = random.choice([True,False])

	eqip = []
	meal = 0 
	for i in range(4):
		eqip.append(random.randint(0,1))
		meal += 2**i * random.randint(0,1)

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






	#name
	#uint time (1,120)
	#uint kcal (1,10000)
	#kitchen -  индекс 20
	#meal - индекс 3
	#typeDish - индекс *(гарнир/основное/выпечка/напиток..) 4
	#parameter - индекс *(жарянное/жирное/острое..) 5
	#eqip - индекс 4
	#components - отсортированный массив индексов ингредиентов 0
	#грамовки
	#bool exotic 2
	#цена - индекс 3
	#сложность - индекс 4