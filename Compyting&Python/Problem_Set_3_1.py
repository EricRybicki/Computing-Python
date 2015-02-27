def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
    
def radiationExposure(start, stop, step):  
        test = start
        count = 0
        while test < stop:
            count += f(test)*step
            test+=step
        return(count)    