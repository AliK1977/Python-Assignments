evens = []
odds = []

for n in range(100) :
    
    if n % 2 == 0 :
        evens.append(n)
    else :
        odds.append(n)
        
print("evens : ", evens)
print("odds : ", odds)
