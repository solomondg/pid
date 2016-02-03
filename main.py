

class pidcontrol():  # PID controller class

    def __init__(self, kp, ki, kd, target=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target = target
        self.values = []
        self.targets = []
        self.correction = 0.0

    def set_start(self, value):
        self.value = value
        self.values.append(self.value)

    def set_target(self, target):
        self.target = target
        self.targets.append(target)

    def reset(self):
        self.values = 0

    def calc_p(self):
        try:
            self.error = (self.target - self.values[-2]) * self.kp
            return self.error
        except IndexError:
            return 0

    def update_value(self):
        self.value += self.calc_p()
        self.values.append(self.value)
        self.targets.append(self.target)

    def round_list(self, l):
        for x in range(0, len(l)):
            l[x] = round(l[x], 2)

    def cohese_list(self):
        self.csvlist = []
        for x in range(0, len(self.values)):
            self.csvlist.append([x, self.targets[x], self.values[x]])


fubar = pidcontrol(.5, 0, 0)
fubar.set_start(0)
fubar.set_target(50)

for x in range(0, 20):
    fubar.update_value()

fubar.set_target(100)

for x in range(0, 20):
    fubar.update_value()

fubar.set_target(75)

for x in range(0, 20):
    fubar.update_value()

fubar.set_target(0)

for x in range(0, 20):
    fubar.update_value()

fubar.round_list(fubar.values)
print (fubar.values)
print (fubar.targets)
