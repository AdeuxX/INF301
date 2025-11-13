import time
def mesure_time (func):
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        result = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} exécutée en {fin - debut:.6f} s")
        return result
    return wrapper 
