
class myTime:

    def __init__(self, h = 0, mins = 0, s = 0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.hours = h
        self.minutes = mins
        self.seconds = s

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
            if self.hours == 24:
                self.hours = 0   
    
    def __str__(self):
        return "{}hrs : {}mins : {}secs".format(self.hours, self.minutes, self.seconds)
    
#pure funcftion
#It does not modify any obj 
def addTime(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    if s >= 60:
        s = 0
        m += 1
    if m >= 60:
        m = 0
        h += 1
    
    sum_t = myTime(h, m, s)
    #return a reference to the new obj is sum_t
    return sum_t

# time1 = myTime(10, 20, 56)
# print(time1)

current_time  = myTime(23, 25, 42)
# bread_time    = myTime(3, 44, 18)

# done_time = addTime(current_time, bread_time)
# print(done_time)

current_time.increment(18)
print(current_time)