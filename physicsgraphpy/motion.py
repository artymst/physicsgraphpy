import math

class ProjectileMotion:
    def __init__(self, v0, angle_deg, g=9.8):
        self.v0 = v0
        self.angle = math.radians(angle_deg)
        self.g = g
        self.times = []
        self.xs = []
        self.ys = []

    def simulate(self, t_max, dt=0.01):
        t = 0
        while t <= t_max:
            self.times.append(t)
            x = self.v0 * math.cos(self.angle) * t
            y = self.v0 * math.sin(self.angle) * t - 0.5 * self.g * t**2
            self.xs.append(x)
            self.ys.append(y)
            t += dt

    def max_height(self):
        return (self.v0 ** 2) * (math.sin(self.angle) ** 2) / (2 * self.g)

    def time_of_flight(self):
        return 2 * self.v0 * math.sin(self.angle) / self.g

    def range(self):
        return (self.v0 ** 2) * math.sin(2 * self.angle) / self.g
