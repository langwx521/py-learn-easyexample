# *args, *kwargs
# 
# 
def foo(*args,**kwargs):
	print('args=', args)
	print('kwargs=', kwargs)

if __name__ == '__main__':
	foo(1,2,3)	
	print('\n')
	foo(a=1,b=2,c=3)
	print('\n')
	foo(1,2,3,a=1,b=2,c=3)
	print('\n')
	foo(1,'b','c',a=1,b='b',c='c')