from multiprocessing import Pool,freeze_support
import time
def t(n):
    r=1
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            r=0
            break
    if r: return n
    else: return 2
if __name__ == '__main__':
    freeze_support()
    print('Prime0 Generator V6 by:\nOscar Bullen\nLeo Sokulluoglu\n\nContributors:\nThomas Walsh\nMatthew Teare\n\n(performing a keyboard interrupt will give you what you have already generated)\n\nA SAVE FILE MUST BE READY PRIOR TO STARTING COMPUTATION!')
    s=int(input('Start:'))
    e=int(input('End:'))
    q=0
    q2=0
    if s<3:q=1
    if s<6:q2=1
    if s<2:s=3
    if not s%2:s+=1
    c=int(input('Cores:'))
    r=str(input('Save File Name:'))
    x=time.time()
    with Pool(8) as p:
        try:
            t=p.map(t,[j for j in range(s,e,2) if j%5])
        except:print('Interrupted!')
        t=list(dict.fromkeys(t))
        if q2:t.insert(1,5)
        print('Completed In:',time.time()-x,'Seconds')
    with open(r, 'w') as f:
        f.write(str(t))
    z=input('Saved File\nHit ENTER to ESCAPE')
    exit()