class Elevator:
    def __init__(self,f):
        self.floor = f
        pass
    def choice(self):
        pass


class Person:
    def __init__(self, start, aim, weigth):
        self.start = start
        self.aim = aim
        self.weigth = weigth

class AdvanceElevator(Elevator):
    def __init__(self,f = 10):
        Elevator.__init__(self,f)
        self.stay = 0
        self.sw = 0
        self.n = 1
    def run(self):
        self.choice(self.n)
        self.c = int(input())
        self.getPerson(self.c)

    def getPerson(self, choice):
        if choice == 1:
            self.num = int(input('请输入本次乘坐的人数：'))
            plist = []
            inlist = []
            outlist = []
            for i in range(self.num):
                s,a,w = int(input('请输入第{0}位乘客所在楼层、目标楼层和体重：'.format(i + 1)))
                plist[i] = Person(s,a,w)
                inlist[i] = s
                outlist[i] = a
            inlist.sort()
            outlist.sort()
            for i in range(self.num):
                if inlist[i] == self.n:
                    self.stay += 1
            j = 0
            k = 0
            for i in range(0,self.floor):
                if(inlist[j] == i+1):
                    if inlist[j] == self.n:
                        print('有%d位乘客上电梯了' % self.stay)
                        j += 1
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw+plist[q].weigth
                    else:
                        print('现在电梯内人数为：',self.stay)
                        self.up(self.n,i+1)
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw+plist[q].weigth
                        if self.sw >= 200:
                            print('电梯已超载')
                            self.stay -= 1
                            k += 1
                            for q in range(self.num):
                                if plist[q].start == self.n:
                                    self.sw = self.sw - plist[q].weigth
                            print('有一位乘客下去了')
                        j += 1
                        self.stay += 1
                        self.n = i+1
                if(outlist[k] == i+1):
                    print('现在电梯内人数为：',self.stay)
                    self.up(self.n,i+1)
                    for q in range(self.num):
                        if plist[q].start == self.n:
                            self.sw = self.sw - plist[q].weigth
                    k += 1
                    self.stay -= 1
                    self.n = i+1
            choice(self.n)
            self.c = int(input())
            self.getPerson(self.c)
        if choice == 2:
            self.num = int(input('请输入本次乘坐的人数：'))
            plist = []
            inlist = []
            outlist = []
            for i in range(self.num):
                s, a, w = int(input('请输入第{0}位乘客所在楼层、目标楼层和体重：'.format(i + 1)))
                plist[i] = Person(s, a, w)
                inlist[i] = s
                outlist[i] = a
            inlist.sort()
            outlist.sort()
            for i in range(self.num):
                if inlist[i] == self.n:
                    self.stay += 1
            j = self.num - 1
            k = self.num - 1
            for i in range(self.n,0,-1):
                if(i == inlist[j]):
                    if inlist[i] == self.n:
                        print('有%d位乘客上电梯了' % self.stay)
                        j -= 1
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                    else:
                        print('现在电梯内人数为：', self.stay)
                        self.dowm(self.n, i)
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                        if self.sw >= 200:
                            print('电梯已超载')
                            self.stay -= 1
                            k -= 1
                            for q in range(self.num):
                                if plist[q].start == self.n:
                                    self.sw = self.sw - plist[q].weigth
                            print('有一位乘客下去了')
                        j -= 1
                        self.stay += 1
                        self.n = i
                if (outlist[k] == i + 1):
                    print('现在电梯内人数为：', self.stay)
                    self.down(self.n, i)
                    for q in range(self.num):
                        if plist[q].start == self.n:
                            self.sw = self.sw - plist[q].weigth
                    k -= 1
                    self.stay -= 1
                    self.n = i
            choice(self.n)
            self.c = int(input())
            self.getPerson(self.c)
        if choice == 3:
            exit(0)
        else:
            self.c = int(input('请输入正确的指令！'))
            self.getPerson(self.c)




































