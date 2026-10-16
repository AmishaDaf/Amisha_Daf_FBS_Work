class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return f'{self.hr}:{self.min}:{self.sec}'
    def __add__(self, other):
        tsec = self.sec + other.sec
        emin = tsec // 60
        tsec = tsec % 60
        tmin = self.min + other.min + emin
        ehr = tmin // 60
        tmin = tmin % 60
        thr = self.hr + other.hr + ehr
        return Time(thr, tmin, tsec)
        # to = Time(thr, tmin, tsec)
        # return to

x = Time(12, 33, 55)
y = Time(6, 30, 56)
a = x + y
print(a)            # 19:4:51
 