import time

def measure(func):
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()

        result = func(*args, **kargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f'{func.__name__}() -> {execution_time}[s]')
        return result
    return wrapper
@measure
def sun_angle(time):
    #replace this for solution
    t = [str for str in time if str.isdigit()]
    t1 = int(''.join(t[:2]))
    t2 = int(''.join(t[2:]))
    unit = 180.0/ 12.0
    sumTime = t1 +t2/60 -6
    time = sumTime *unit
    if time < 0 or time > 180:
        time = "I don't see the sun!"
    return time
@measure
def sun_angle2(time):
    time = time.split(':')
    t1 = int(time[0])
    t2 = int(time[1])
    unit = 180.0/ 12.0
    sumTime = t1 +t2/60 -6
    time = sumTime *unit
    if time < 0 or time > 180:
        time = "I don't see the sun!"
    return time

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle2("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
