# tiny-chess-01 engine — readable source of main.py (packed by kit `makefun compress`).
# 0x88 board, negamax alpha-beta + iterative deepening, transposition table,
# killer moves, MVV-LVA ordering, quiescence, null-move pruning, repetition
# detection, tapered evaluation. Size cap: packed main.py must stay <= 4096 bytes.
import os,sys,json,random,urllib.request as Ur
F="KKKKKKKKLMMGGMMLLJIKKIJLKKKOOKKKLLMPPMLLMMOQQOMMUUUUUUUUKKKKKKKKACEEEECACGKLLKGCELMNNMLEEKNOONKEELNOONLEEKNMNMKECGKKKKGCACEEEECAGIIIIIIGILKKKKLIIMMMMMMIIKMMMMKIILLMMLLIIKLMMLKIIKKKKKKIGIIIIIIGKKKLLKKKJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJLMMMMMMLKKKKKKKKGIIJJIIGIKLKKKKIILLLLLKIKKLLLLKJJKLLLLKJIKLLLLKIIKKKKKKIGIIJJIIGOQMKKMQOOOKKKKOOIGGGGGGIGEECCEEGECCAACCEECCAACCEECCAACCEECCAACCE"
P=[(ord(c)-75)*5 for c in F]
EK="=?CEEC?=AAKKKKAAGMSUUSMGIOW[[WOIKQY]]YQKKQW[[WQKKOQUUQOKGKMQQMKG"
DK=[(ord(c)-75)*5 for c in EK]
PW=[0,0,1,1,2,4,0]
V=[0,100,320,330,500,900,0]
X=[0]*(13*128)
for i in range(1664):
 p=i//128-6;s=i%128
 if p and not s&136:q=s if p>0 else s^112;a=abs(p);X[i]=(V[a]+P[(a-1)*64+(q>>4)*8+q%8])*(1 if p>0 else-1)
N1=(14,18,31,33,-14,-18,-31,-33);K1=(1,-1,16,-16,15,17,-15,-17);B1=(15,17,-15,-17);R1=(1,-1,16,-16)
Y={4:12,7:14,0:13,116:3,119:11,112:7}
r=random.Random(20261123);R=[r.getrandbits(64)for _ in range(1689)]
B=[0]*128;W=1;C=0;E=-1;Z=0;S=0;G=4;H=116;U=[];D={};K=[0]*512;N=0;L=100000;M=100000;PH=24;RC={};UN=[]
SF="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -"
class A(Exception):pass
def J(f,t,p):return f|t<<7|p<<14
def ev():
 w=(G>>4)*8+G%8;h=H^112;h=(h>>4)*8+h%8;v=S+(DK[w]-DK[h])*(24-PH)//24;return v if W else-v
def T(s,w):
 for d in(-15,-17)if w else(15,17):
  t=s+d
  if not t&136 and B[t]==(1 if w else-1):return 1
 for d in N1:
  t=s+d
  if not t&136 and B[t]==(2 if w else-2):return 1
 for d in K1:
  t=s+d
  if not t&136 and B[t]==(6 if w else-6):return 1
 for d in B1+R1:
  t=s+d
  while not t&136:
   p=B[t]
   if p:
    if p==(5 if w else-5)or p==((3 if w else-3)if d in B1 else(4 if w else-4)):return 1
    break
   t+=d
 return 0
def g(q=0):
 m=[]
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or(p>0)!=W:continue
  v=abs(p)
  if v==1:
   d=16 if W else-16;t=s+d
   if not B[t]:
    z=(t>>4)==(7 if W else 0)
    if z:m+=[J(s,t,x)for x in(5,4,3,2)]
    elif not q:
     m.append(J(s,t,0))
     if(s>>4)==(1 if W else 6)and not B[s+2*d]:m.append(J(s,s+2*d,0))
   for t in(s+d-1,s+d+1):
    if t&136:continue
    if(B[t]and(B[t]>0)!=W)or t==E:
     if(t>>4)==(7 if W else 0):m+=[J(s,t,x)for x in(5,4,3,2)]
     else:m.append(J(s,t,0))
  elif v==2 or v==6:
   for d in N1 if v==2 else K1:
    t=s+d
    if t&136:continue
    if(not q or B[t])and(not B[t]or(B[t]>0)!=W):m.append(J(s,t,0))
  else:
   for d in B1 if v==3 else R1 if v==4 else B1+R1:
    t=s+d
    while not t&136:
     if B[t]:
      if(B[t]>0)!=W:m.append(J(s,t,0))
      break
     if not q:m.append(J(s,t,0))
     t+=d
 if not q:
  for r,k,t,f,a,b,c,s in((1,4,6,7,5,6,5,0),(2,4,2,0,3,2,1,0),(4,116,118,119,117,118,117,1),(8,116,114,112,115,114,113,1)):
   if C&r and not B[a]and not B[b]and not B[c]and B[f]==(4 if s==0 else-4)and not T(k,s)and not T(a,s)and not T(t,s):m.append(J(k,t,0))
 return m
def l(q=0):
 o=[]
 for m in g(q):
  v=W;y(m)
  if not T(G if v else H,not v):o.append(m)
  u(m)
 return o
def nm():
 global W,E,Z
 UN.append((E,Z));Z^=R[1664]
 if E>=0:Z^=R[1681+(E&7)]
 E=-1;W=not W;RC[Z]=RC.get(Z,0)+1
def nu():
 global W,E,Z
 RC[Z]-=1
 E,Z=UN.pop();W=not W
def y(m):
 global W,C,E,Z,S,G,H,PH
 f=m&127;t=m>>7&127;z=m>>14&7;p=B[f];c=B[t];e=t
 if abs(p)==1 and t==E and not c:e=t-(16 if W else-16);c=B[e]
 U.append((c,e,C,E,Z,S,G,H,PH));Z^=R[1664];Z^=R[1665+C]
 if E>=0:Z^=R[1681+(E&7)]
 Z^=R[(p+6)*128+f];S-=X[(p+6)*128+f]
 if c:
  Z^=R[(c+6)*128+e];S-=X[(c+6)*128+e];B[e]=0;PH-=PW[abs(c)]
 B[f]=0;n=(z if W else-z)if z else p;B[t]=n;Z^=R[(n+6)*128+t];S+=X[(n+6)*128+t]
 if z:PH+=PW[z]
 if abs(p)==6 and abs(t-f)==2:
  j,k=(f+3,f+1)if t>f else(f-4,f-1);w=B[j];B[j]=0;B[k]=w;Z^=R[(w+6)*128+j]^R[(w+6)*128+k];S-=X[(w+6)*128+j];S+=X[(w+6)*128+k]
 C&=Y.get(f,15)&Y.get(t,15);E=f+(16 if W else-16)if abs(p)==1 and abs(t-f)==32 else-1;Z^=R[1665+C]
 if E>=0:Z^=R[1681+(E&7)]
 if abs(p)==6:
  if W:G=t
  else:H=t
 W=not W;RC[Z]=RC.get(Z,0)+1
def u(m):
 global W,C,E,Z,S,G,H,PH
 RC[Z]-=1
 c,e,C,E,Z,S,G,H,PH=U.pop();f=m&127;t=m>>7&127;z=m>>14&7;p=B[t];B[t]=0;B[f]=(1 if p>0 else-1)if z else p
 if c:B[e]=c
 if abs(B[f])==6 and abs(t-f)==2:
  j,k=(f+3,f+1)if t>f else(f-4,f-1);B[j]=B[k];B[k]=0
 W=not W
def p(f):
 global W,C,E,Z,S,G,H,B,U,PH
 B=[0]*128;U=[];Z=0;S=0;PH=0;o=f.split()
 for i,x in enumerate(o[0].split("/")):
  b=7-i;h=0
  for ch in x:
   if ch.isdigit():h+=int(ch)
   else:
    v=("PNBRQK".find(ch.upper())+1)*(1 if ch.isupper() else-1);s=b*16+h;B[s]=v;Z^=R[(v+6)*128+s];S+=X[(v+6)*128+s];PH+=PW[abs(v)]
    if abs(v)==6:
     if v>0:G=s
     else:H=s
    h+=1
 W=o[1]=="w";C=sum(1<<"KQkq".find(ch)for ch in o[2]if ch in"KQkq")
 E=-1
 if o[3]!="-":E="abcdefgh".find(o[3][0])+(int(o[3][1])-1)*16
 if not W:Z^=R[1664]
 Z^=R[1665+C]
 if E>=0:Z^=R[1681+(E&7)]
def o(m,t,pl):
 def k(m):
  f=m&127;v=B[(m>>7)&127]
  if not v and abs(B[f])==1 and(m>>7&127)==E:v=1 if B[f]>0 else-1
  s=V[abs(v)]*16-V[abs(B[f])]if v else 0
  if m==t:s+=1000000
  elif not v and(m==K[pl*2]or m==K[pl*2+1]):s+=800
  if m>>14:s+=9000
  return-s
 m.sort(key=k)
def q(a,b,pl):
 global N
 N+=1
 if N&2047==0 and N>L:
  raise A
 if RC.get(Z,0)>=3:return 0
 if T(G if W else H,not W):
  m=g(0);o(m,0,pl);n=0
  for v in m:
   w=W;y(v)
   if T(G if w else H,not w):u(v);continue
   n+=1;s=-q(-b,-a,pl+1);u(v)
   if s>=b:return b
   if s>a:a=s
  return-M+pl if not n else a
 s=ev()
 if s>=b:return b
 if s>a:a=s
 m=g(1);o(m,0,pl)
 for v in m:
  w=W;y(v)
  if T(G if w else H,not w):u(v);continue
  s=-q(-b,-a,pl+1);u(v)
  if s>=b:return b
  if s>a:a=s
 return a
def r(d,a,b,pl):
 global N
 N+=1
 if N&2047==0 and N>L:
  raise A
 if d<=0:return q(a,b,pl)
 if RC.get(Z,0)>=3:return 0
 a0=a;e=D.get(Z);t=e[3]if e else 0
 if e and e[0]>=d:
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=b:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
 if d>=3 and not T(G if W else H,not W)and ev()>=b:
  nm();s=-r(d-3,-b,-b+1,pl+1);nu()
  if s>=b:return b
 m=g();o(m,t,pl);s=-M;v=0;w=a;n=0
 for j in m:
  c=B[j>>7&127]or(abs(B[j&127])==1 and(j>>7&127)==E);h=W;y(j)
  if T(G if h else H,not h):u(j);continue
  n+=1;x=-r(d-1,-b,-w,pl+1);u(j)
  if x>s:s=x;v=j
  if x>w:w=x
  if w>=b:
   if not c:K[pl*2+1]=K[pl*2];K[pl*2]=j
   break
 if not n:return-M+pl if T(G if W else H,not W)else 0
 D[Z]=(d,2 if s<=a0 else(1 if s>=b else 0),s,v)
 return s
def d(m):
 f=m&127;t=m>>7&127;z=m>>14&7
 return"abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)+("  nbrq"[z]if z else"")
def c(fen,lg,mv=None):
 global RC,K
 RC={}
 if mv:
  p(SF);RC[Z]=1
  for u in mv:
   for m in l():
    if d(m)==u:y(m);break
 p(fen)
 if not mv:RC[Z]=1
 m=l()
 if not m:return lg[0]
 if len(m)==1:return d(m[0])
 D.clear();K=[0]*512
 global N
 N=0;v=m[0]
 try:
  for x in range(1,40):
   s=r(x,-M,M,0);e=D.get(Z)
   if e:v=e[3]
   if abs(s)>M-2000:break
 except A:pass
 z=d(v)
 return z if z in lg else lg[0]
V0=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
def h(p,b):
 q=Ur.Request(V0+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with Ur.urlopen(q)as w:return json.load(w)
 except Exception:return None
def main():
 while True:
  g=h("/game",{})
  if g is None:sys.exit(1)
  if g["status"]=="done":break
  while g["status"]=="your_move":
   v=c(g["fen"],g["legal_moves"],g.get("moves"));n=h("/move",{"game":g["game"],"move":v})
   if n is None:
    n=h("/move",{"game":g["game"],"move":g["legal_moves"][0]})
    if n is None:sys.exit(1)
   g=n
  print(g['game'],g['outcome'],g['reason'],file=sys.stderr)
 print(g.get('wins'),g.get('draws'),g.get('losses'),file=sys.stderr)
if __name__=="__main__":main()
