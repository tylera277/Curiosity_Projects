

class RungeKutta:

    def __init__(self, y, v_y, dt, c, k, mass, N, resting_length):
        self.y = y
        self.v_y = v_y
        self.dt = dt

        # Systems constants/parameters
        self.c = c
        self.k = k
        self.mass = mass
        self.resting_length = resting_length

        # Number of springs in the system
        self.N = N

    def main(self, n):

        self.y[n] += ((self.dt/6.0) * (self.k1_y(n) + 2*self.k2_y(n) + 2*self.k3_y(n) + self.k4_y(n)))
        self.v_y[n] += ((self.dt/6.0) * (self.k1_vy(n) + 2*self.k2_vy(n) + 2*self.k3_vy(n) + self.k4_vy(n)))

        return self.y[n], self.v_y[n]

    def k1_y(self, i):
        return self.v_y[i]
    def k1_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * self.v_y[i]
        position_term = - (self.k / self.mass) * (self.y[i] - self.resting_length[i])

        return (force_term + velocity_term + position_term)


    def k2_y(self, i):
        return self.v_y[i] + (self.dt / 2.0) * self.k1_vy(i)
    def k2_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + (self.dt/2.0) * self.k1_vy(i))
        position_term = - (self.k / self.mass) * (self.y[i] + (self.dt/2.0) * (self.k1_y(i) - self.resting_length[i]))

        return force_term + velocity_term + position_term


    def k3_y(self, i):
        return self.v_y[i] + (self.dt/2.0) * self.k2_vy(i)
    def k3_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + (self.dt / 2.0) * self.k2_vy(i))
        position_term = - (self.k / self.mass) * (self.y[i] + (self.dt / 2.0) * (self.k2_y(i) - self.resting_length[i]))

        return force_term + velocity_term + position_term


    def k4_y(self, i):
        return self.v_y[i] + self.dt * self.k3_vy(i)
    def k4_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + (self.dt / 2.0) * self.k3_vy(i))
        position_term = - (self.k / self.mass) * (self.y[i] + (self.dt / 2.0) * (self.k3_y(i) - self.resting_length[i]))

        return force_term + velocity_term + position_term


    def force(self, spot):
        return 0#(1.0 / self.mass) * (self.y[spot-1] - self.y[spot+1])

