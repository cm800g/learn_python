#coding=utf-8
#石头剪刀布游戏试写
import random
class Guess:
	def __init__(self,n):
		if 0==n:
			self.next=1
		elif 1==n:
			self.next=2
		else:
			self.next=0
glist=['石头','剪刀','布']
while True:
	robot=random.randint(0,2)
	man=input("竞猜开始\n输入88结束游戏\n0--石头, 1--剪刀, 2--布\n你想出什么？:")
	if man.isdigit():
		man=int(man)
		if 88==man:
			print("游戏结束，欢迎下次再来")
			break
		elif man>2:
			print("输入错误，请重新输入\n")
			continue
	else:
		print("输入错误，请重新输入\n")
		continue
	if Guess(man).next==robot:
		print("我出的是{},你出的是{},我赢了\n".format(glist[man],glist[robot]))
	elif Guess(robot).next==man:
		print("我出的是{},你出的是{},我输了\n".format(glist[man],glist[robot]))
	else:
		print("我出的是{},你出的是{},打平了\n".format(glist[man],glist[robot]))
