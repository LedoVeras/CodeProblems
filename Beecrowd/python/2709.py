
ANSWERS = ["Bad boy! I’ll hit you." , "You’re a coastal aircraft, Robbie, a large silver aircraft."]

def checkPrime(num):
    if (num != 2 and num % 2 == 0) or num == 1:
        return False

    raiz = int(num ** 0.5)
    for i in range(3, raiz + 1, 2):
        if num % i == 0:
            return False
    
    return True
		
"""
slower function

def checkPrime(number):
    toRt = False

    if number == 1:
        return False
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                toRt = True
                break
            
    return not toRt
"""

while(True):
    try: 
        coins = int(input())
    except EOFError as e:
        break

    values = []
    for i in range(coins):
        values.append(int(input()))
        
    jump = int(input())
    
    coin_total_value = 0
    
    for i in range(coins - 1, -1, -jump):
        coin_total_value += values[i]
    
    print(ANSWERS[1] if checkPrime(coin_total_value) else ANSWERS[0])
        

