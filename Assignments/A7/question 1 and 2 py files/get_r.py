import numpy as np

def get_r(K, L, alpha, Z, delta):
    if type(K) is float and K <= 0:
        raise ValueError("K must be positive")
    if type(K) is np.array:
        if sum(K <= 0) > 0 :
            raise ValueError("K must be positive")
    if type(L) is float and L <= 0:
        raise ValueError("L must be positive")
    if type(L) is np.array:
        if sum(L <= 0) > 0 :
            raise ValueError("L must be positive")
    if Z <= 0:
        raise ValueError("Z must be positive")
    #assert alpha > 0 and alpha < 1
    if alpha < 0 or alpha > 1:
        raise ValueError("alpha must be within 0 and 1")
    if delta < 0 or delta > 1:
        raise ValueError("delta must be within 0 and 1")
    
    r = alpha * Z * ((L / K) ** (1 - alpha)) - delta 
    if type(K) is float and type(L) is float and type(r) is not float:
        raise TypeError("If K and L are scalers, r should also be a scaler")
    if type(K) is np.ndarray and type(L) is np.ndarray and type(r) is not np.ndarray:
        raise TypeError("If K and L are scalers, r should also be a scaler")
           
    return r