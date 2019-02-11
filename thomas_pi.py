import math
#tthis is a comment


def estimate_pi():
    
    k=0
    increment=0
    est_pi = 0
    
    while abs(est_pi-math.pi)>=1e-2000:
        increment = increment + (math.factorial(4*k)*(1103+26390*k))/((math.factorial(k)**4)*396**(4*k))
        est_pi = 1/((2*math.sqrt(2)/9801)*increment)
        print(est_pi)
        k=k+1

estimate_pi()
