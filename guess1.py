#coding=utf-8
import random
glist=[1,2,0]
replist=["石头","剪刀","布"]
while True:
	robot=random.randint(0,2)
	man=int(input("请输入对应的数字,\n0--石头,1--剪刀,2--布\n你的选择:"))
	print("你出的是{}，电脑出的是{}".format(replist[man],replist[robot]))
	if glist[robot]==man:
		print("你输了\n")
	elif glist[man]==robot:
		print("你赢了\n")
	else:
		print("打平了\n")