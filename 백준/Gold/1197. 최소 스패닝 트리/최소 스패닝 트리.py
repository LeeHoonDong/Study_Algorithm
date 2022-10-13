def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

if __name__=="__main__":
    edges=[]
    answer=0
    N,M=map(int,input().split())
    parent = [0 for _ in range(N+1)]
    for j in range(N+1):
        parent[j]=j
    for j in range(M):
       a,b,cost=map(int,input().split())
       edges.append((cost,a,b))
    edges.sort()
    for cost,a,b in edges:
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            answer+=cost
    print(answer)
