a=3000                         #total bananas
l=1000                          #max banana carried
s=0
while(a>l):
    n=(a/l)*2-1              #no. of trips
    x=l//n                       #distance of check post trips
    s=s+x                        #storing no of bananas consumed
    a=a-l                         #next load of banana
distanceLeft=a-s
bananasNeeded=distanceLeft
bananasLeft=a-bananasNeeded
print(bananasLeft)
