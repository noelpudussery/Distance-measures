import math

# Jaccard Distance function
def jaccard(s1, s2) : 
	size_s1 = len(s1)
	size_s2 = len(s2)
	intersect = s1&s2

	size_in = len(intersect)
	jaccard_in = size_in / (size_s1 + size_s2 - size_in)
	print("Jaccard Index=",jaccard_in)
	jaccard_dist = 1 - jaccard_in

	return jaccard_dist

# Hamming Distance function
def hamming_distance(string1, string2): 
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1

    return distance 

# Cosine Distance function
def cosine_dist(l1,l2):
	x,y,xy=0,0,0
	for i in range(len(l1)):
		xy+=l1[i]*l2[i]
		x+=l1[i]*l1[i]
		y+=l2[i]*l2[i]

	x=float(math.sqrt(x))
	y=float(math.sqrt(y))
	dist=float(xy/(x*y))
	return dist

# Edit Distance function
def edit_dist(str1,str2):
	a=len(str1)
	b=len(str2)
	count=lcs(str1,str2,a,b)
	dist=a+b-(2*count)
	return dist

def lcs(str1,str2,m,n): 
    if m == 0 or n == 0: 
       return 0; 
    elif str1[m-1] == str2[n-1]: 
       return 1 + lcs(str1, str2, m-1, n-1); 
    else: 
       return max(lcs(str1, str2, m, n-1), lcs(str1, str2, m-1, n)); 
  


s1 = set(); 
s1.add(1); 
s1.add(2); 
s1.add(3); 
s1.add(4); 
s1.add(5); 

s2 = set(); 
s2.add(4); 
s2.add(5); 
s2.add(6); 
s2.add(7); 
s2.add(8); 
 
#Jaccard
print("Set 1 is ",s1)
print("Set 2 is ",s2)
jaccardDistance = jaccard(s1, s2)
print("Jaccard distance = ",jaccardDistance) 

#Hamming
ham_dist = hamming_distance("Helps", "Hello")
print("\nHamming distance between 'Helps' and 'Hello' is ",ham_dist)

#Cosine
l1=[3,0,2,0,1,1,0,1,0,1]
l2=[5,0,3,0,2,0,0,2,0,0]
cos_dist=cosine_dist(l1,l2)
print("\nl1 =",l1)
print("l2= ",l2)
print("The cosine distance is",cos_dist)

#Edit
str1="China"
str2="India"
print("\nString 1 is: ",str1)
print("String 2 is: ",str2)
edit_distance=edit_dist(str1,str2)
print("The edit distance is: ",edit_distance)
	

