import numpy as np

class MotionGraph:
    def __init__(self, initial_position, initial_velocity, acceleration):
        self.x0 = initial_position
        self.v0 = initial_velocity
        self.a = acceleration
        self.positions = []
        self.velocities = []
        self.times = []

    def simulate(self, t_max, dt=0.01):
        t = 0
        x = self.x0
        v = self.v0
        while t <= t_max:
            self.times.append(t)
            self.positions.append(x)
            self.velocities.append(v)
            v = self.v0 + self.a * t
            x = self.x0 + self.v0 * t + 0.5 * self.a * t ** 2
            t += dt

    def get_accelerations(self):
        return [self.a] * len(self.times)
