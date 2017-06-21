#python practice
#json对实例对象的转换
import json
class Student:
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score

s=Student("wang",23,88)
print(json.dumps(s,default=lambda x:x.__dict__))
aa=json.dumps(s,default=lambda x:x.__dict__)

def dict2stu(xx):
	return Student(xx['name'],xx['age'],xx['score'])

print(json.loads(aa,object_hook=dict2stu))

bb=json.loads(aa,object_hook=dict2stu)

print(bb.name, bb.age, bb.score)
