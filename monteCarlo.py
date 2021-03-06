# Group 5_07
# APMA 3100 
# Tim Han, Vinh Do, John Burkher, Elias Haddad
import numpy as np

def generateNextRandomNumber(x_i):
    x_i = (a*x_i + c) % K
    u_i = x_i / K
    return x_i, u_i

def inverse(u): #randomVariableGenerator
    return -12 * np.log(1-u)

def simulate(x_i):
    W = 0
    calls = 0
    while calls < 4:
        calls+=1
        W += 6
        x_i, u_i = generateNextRandomNumber(x_i)
        
        if (u_i >= 0 and u_i < .2): #busy
            W += 3
        elif (u_i >= .2 and u_i < .5): #unavailable
            W += 25
        elif (u_i >= .5 and u_i <=1): #available
            x_i, u_i = generateNextRandomNumber(x_i)
            pickup_time = inverse(u_i)
            if (pickup_time >= 0 and pickup_time <= 25):
                W += pickup_time
                break
            else:
                W += 25
        W += 1
    return W, x_i

if __name__ == "__main__":
    
    x_i = 1000
    a = 24693
    c = 3517
    K = 2**15
    
    call_times = []
    mean = 0
    current = 0
    
    #'''
    for n in range(1, 1001):
        W, x_i = simulate(x_i)
        mean += W
        call_times.append(W)
    
    call_times.sort()
    mean = mean / n
    median = (call_times[499] + call_times[500] ) / 2
    first_quartile = ( call_times[249] + call_times[250] ) / 2
    third_quartile = ( call_times[749] + call_times[750] ) / 2
    min = call_times[0]
    max = call_times[999]
    
    print(mean, first_quartile, median, third_quartile, min, max)
    
    for n in range(1, 10001):
        if call_times[n] > 15:
            print("<15", n/1000)
            break
    for n in range(1, 10001):
        if call_times[n] > 20:
            print("<20", n/1000)
            break
    for n in range(1, 10001):
        if call_times[n] > 30:
            print("<30", n/1000)
            break
    for n in range(1, 10001):
        if call_times[n] > 40:
            print(">40", (1000-n)/1000)
            break
    
    for n in range(1, 10001):
        if call_times[n] > 65:
            print(">65", (1000-n)/1000)
            break
    for n in range(1, 10001):
        if call_times[n] > 90:
            print(">90", (1000-n)/1000)
            break
    for n in range(1, 10001):
        if call_times[n] > 115:
            print(">115", (1000-n)/1000)
            break
    
    
    #'''
    x_i = 1000
    for n in range(1, 1001):
        x_i, u_i = generateNextRandomNumber(x_i)
        if (n == 1) or (n == 2) or (n == 3) or (n == 51) or (n == 52) or (n == 53):
            print(u_i)
        #print(simulate(x_i/K))
    #'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    