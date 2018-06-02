#/usr/bin/env python3

fname = str(input('enter filename:'))
try:
	f = open(fname,'r')
except:
	print('no such file')
	import sys
	sys.exit()
qw = f.read()
f = qw.replace('\n','')
final = []
substr = " "
def tokenize(str):
	return str.replace('(',' ( ').replace(')',' ) ').split()

def parse(f):
	return read_from_tokens(tokenize(f))

def read_from_tokens(f):
	token = f.pop(0)
	if token =='(':
		l =[]
		while(f[0]!=')'):
			l.append(read_from_tokens(f))
		f.pop(0)
		return l
	else :
		return atomize(token)

def atomize(token):
	try:
		return int(token)
	except Exception as e:
		try:
			return float(token)
		except Exception as e:
			return token
def divide(f):
	counter =0
	str1 =""
	final =[]
	for i in range(0,len(f)):
		if f[i] == '(':
			counter+=1
			str1+=f[i]
		elif f[i] == ')':
			counter-=1
			str1+=f[i]
			if counter == 0:
				final.append(str1)
				str1 = ''
		else:
			str1+=(f[i])
	return final
def eval(lis):
	if atomize(str(lis)) in dict1:
		try:
			return str(dict1(lis))
		except:
			return dict1[lis]
	elif type(lis)!= list:
		try:
			return int(lis)
		except:
			try:
				return float(lis)
			except:
				return lis
	else:
		for i in range(0 , len(lis)):
			if type(lis[i]) == list:
				lis[i] = eval(lis[i])
			if lis[i] == '*':
				return eval(lis[i+1]) * eval(lis[i+2])
			elif lis[i] == '+':
				return eval(lis[i+1]) + eval(lis[i+2])
			elif lis[i] == '-':
				return eval(lis[i+1]) - eval(lis[i+2])
			elif lis[i] == '/':
				return eval(lis[i+1]) / eval(lis[i+2])
			elif lis[i] == 'add1':
				return eval(lis[i+1])+1
			elif lis[i] == 'sub1':
				return eval(lis[i+1])-1
			elif lis[i] == 'expt':
				return eval(lis[i+1]) ** eval(lis[i+2])
			else:
				try:
					return int(lis[i])
				except:
					try:
						return float(lis[i])
					except:
						return lis[i]
def check_cond(lis):
	if lis[0] == '=' or lis[0] == 'equal?':
		if lis[1] in dict1 and lis[2] not in dict1:
			if dict1[lis[1]] == atomize(lis[2]):
				return True
			else : return False
		if lis[1] not in dict1 and lis[2] in dict1:
			if dict1[lis[2]] == atomize(lis[1]):
				return True
			else: return False
		if lis[1] in dict1 and lis[2] in dict1:
			if dict1[lis[1]] == dict1[lis[2]]: 
				return True
			else: return False
		if lis[1] not in dict1 and lis[2] not in dict1:
			if atomize(lis[1]) == atomize(lis[2]):
				return True
			else: return False
	if lis[0] == '>':
		if lis[1] in dict1 and lis[2] not in dict1:
			if dict1[lis[1]] > atomize(lis[2]):
				return True
			else : return False
		if lis[1] not in dict1 and lis[2] in dict1:
			if atomize(lis[1]) > dict1[lis[2]]:
				return True
			else: return False
		if lis[1] in dict1 and lis[2] in dict1:
			if dict1[lis[1]] > dict1[lis[2]]: 
				return True
			else: return False
		if lis[1] not in dict1 and lis[2] not in dict1:
			if atomize(lis[1]) > atomize(lis[2]):
				return True
			else: return False
	if lis[0] == '<':
		if lis[1] in dict1 and lis[2] not in dict1:
			if dict1[lis[1]] < atomize(lis[2]):
				return True
			else : return False
		if lis[1] not in dict1 and lis[2] in dict1:
			if atomize(lis[1]) < dict1[lis[2]]:
				return True
			else: return False
		if lis[1] in dict1 and lis[2] in dict1:
			if dict1[lis[1]] < dict1[lis[2]]: 
				return True
			else: return False
		if lis[1] not in dict1 and lis[2] not in dict1:
			if atomize(lis[1]) < atomize(lis[2]):
				return True
			else: return False
	if lis[0] == '>=':
		if lis[1] in dict1 and lis[2] not in dict1:
			if dict1[lis[1]] >= atomize(lis[2]):
				return True
			else : return False
		if lis[1] not in dict1 and lis[2] in dict1:
			if atomize(lis[1]) >= dict1[lis[2]]:
				return True
			else: return False
		if lis[1] in dict1 and lis[2] in dict1:
			if dict1[lis[1]] >= dict1[lis[2]]: 
				return True
			else: return False
		if lis[1] not in dict1 and lis[2] not in dict1:
			if atomize(lis[1]) >= atomize(lis[2]):
				return True
			else: return False
	if lis[0] == '<=':
		if lis[1] in dict1 and lis[2] not in dict1:
			if dict1[lis[1]] <= atomize(lis[2]):
				return True
			else : return False
		if lis[1] not in dict1 and lis[2] in dict1:
			if atomize(lis[1]) <= dict1[lis[2]]:
				return True
			else: return False
		if lis[1] in dict1 and lis[2] in dict1:
			if dict1[lis[1]] <= dict1[lis[2]]: 
				return True
			else: return False
		if lis[1] not in dict1 and lis[2] not in dict1:
			if atomize(lis[1]) <= atomize(lis[2]):
				return True
			else: return False


def replace(fdict1,lis,fdict,fparam):
	for i in range(1,len(lis)):
		try:
			fdict1[lis[0]][fparam[i-1]] = lis[i]
		except:
			pass
def replaceit(templis,fdict1,lis):
	for i in range(0,len(templis)):
		if type(templis[i]) == list:
			replaceit(templis[i],fdict1,lis)
		elif str(templis[i]) in fdict1[lis[0]]:
			templis[i] = fdict1[lis[0]][templis[i]]	


def replacel(fdict1,fmethod1,dict1,lis):
	for i in range(0,len(fmethod1[lis[0]])):
		if type(fmethod1[lis[0]][i]) == list:
			replaceit(fmethod1[lis[0]][i],fdict1,lis)
		elif fmethod1[lis[0]][i] in fdict1[lis[0]]:
			fmethod1[lis[0]][i] = fdict1[lis[0]][fmethod1[lis[0]][i]]
		
def dictionary(list123):
	dic = {}
	for i in range(0,len(list123)):
		dic[list123[i]] = None
	return dic
def funcmapit(lis,dict1,fdict1,fmethod1,fdict,fmethod,fparam,fmethod2):
	#print(fdict1[lis[0]],'#')
	fdict1[lis[0]] = dictionary(fparam)
	replace(fdict1,lis,fdict,fparam)
	#print(fdict1[lis[0]],'#')
	replacel(fdict1,fmethod1,dict1,lis)
	mapit(fmethod1[lis[0]],dict1,fdict,fmethod,fdict1,fmethod1,fparam,fmethod2)
	import ast
	try:
		fmethod1 = ast.literal_eval(fmethod2)
	except:
		fmethod1 = fmethod

def mapit(lis,dict1,fdict,fmethod,fdict1,fmethod1,fparam,fmethod2):
	if lis[0] == 'println' or lis[0]=='print':
		if str(lis[1]) not in dict1:
			print(eval(lis[1]))
		else:
			print(dict1[lis[1]])
	if lis[0] == 'define':
		if ['read'] not in lis and ['read-line'] not in lis:
			if type(lis[1])!=list:
				if lis[2]!='\'':
					dict1[lis[1]] = lis[2]
				else:
					dict1[lis[1]] = lis[3]
			else:
				fparam += lis[1][1:]
				fdict[lis[1][0]] = lis[1][1:]
				fmethod[lis[1][0]] = lis[2]
				fmethod2=str(fmethod)
		else:
			if ['read'] in lis:
				temp = input()
				try:
					dict1[lis[1]] = int(temp)
				except:
					try:
						dict1[lis[1]] = float(temp)
					except:
						dict1[lis[1]] = temp
			elif ['read-line'] in lis:
				temp = input()
				dict1[lis[1]] = temp


	if str(lis[0]) in fdict:
		fmethod1 = fmethod
		fdict1 = fdict
		funcmapit(lis,dict1,fdict1,fmethod1,fdict,fmethod,fparam,fmethod2)
	if lis[0] == r'set!':
		if lis[1] not in dict1:
			print("not predefined !!!",lis[1])
			import sys
			sys.exit()
		else:
			dict1[lis[1]] = eval(lis[2])	
	if lis[0] == 'if':
		if check_cond(lis[1]):
			mapit(lis[2],dict1,fdict,fmethod,fdict1,fmethod1,fparam,fmethod2)
		else:
			mapit(lis[3],dict1,fdict,fmethod,fdict1,fmethod1,fparam,fmethod2)
	#if lis[0] == 'for':


ln = divide(qw.replace('\n',' ')[12:])
dict1 = {}
fdict = {}
fmethod = {}
fdict1 = {}
fmethod1 = {}
fmethod2 = ""
fparam = []
for i in range(0,len(ln)):
	mapit(parse(ln[i]),dict1,fdict,fmethod,fdict1,fmethod1,fparam,fmethod2)
	#print(parse(ln[i]))
