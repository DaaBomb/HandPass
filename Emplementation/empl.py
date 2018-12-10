import os



def dis(A,B):
	return pow(pow(A[0]-B[0],2)+pow(A[1]-B[1],2),0.5)






def disratio(A):
	a=max(A)
	b=[]
	for c in A:
		c=c/a
		b.append(c)
	return b
	
	

def save_password(A):
	path=os.getcwd()
	f=open(path+'/'+'pwd.csv','w')
	dtc=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,20),(20,0),(1,5),(5,9),(9,13),(9,17),(2,6),(6,10),(10,14),(14,18),(3,7),(7,11),(11,15),(15,19),(4,8),(8,12),(12,16),(16,20))
	dist=[]
	mi=0
	for i in dtc:
		f.write(str(i[0])+","+str(i[1])+","+str(A[mi])+"\n")
		mi=mi+1
		
		
		
	f.close()
	
def create_list_distance(A):
	n=len(A)
	dtc=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,20),(20,0),(1,5),(5,9),(9,13),(9,17),(2,6),(6,10),(10,14),(14,18),(3,7),(7,11),(11,15),(15,19),(4,8),(8,12),(12,16),(16,20))
	dist=[]
	for i in dtc:
		if (A[i[0]] is not None) and (A[i[1]] is not None):
			dist.append(dis(A[i[0]],A[i[1]]))
		else:
			dist.append(0)
	dist=disratio(dist)
	save_password(dist)
				
	
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	

	
	
	
	

