import numpy as np


class ObsObject(object):
    def __init__(self, x_rel, uvi_rel, x_abs, y_rel, y_abs):
        self.x_rel, self.uvi_rel, self.x_abs, self.y_rel, self.y_abs = x_rel, uvi_rel, x_abs, y_rel, y_abs


class VariableWave(object):
    def __init__(self, amp_range, f_range, off_range, damp_range, n_components=1):
        self.amp_range = amp_range
        self.f_range = f_range
        self.off_range = off_range
        self.damp_range = damp_range
        self.n_components = n_components
        self.randomize()

    def out(self, x):
        y = self.amplitude*np.cos(self.frequency * np.pi * (x-self.offset)) * np.exp(-self.damping*(x-self.offset)**2)
        return y

    def set_values(self, a, f, o, d):
        self.amplitude = a
        self.frequency = f
        self.offset = o
        self.damping = d

    def randomize(self, print_vals=False):
        self.amplitude = np.random.uniform(low=self.amp_range[0], high=self.amp_range[1]/self.n_components)
        self.frequency = np.random.uniform(low=self.f_range[0], high=self.f_range[1])
        self.offset = np.random.uniform(low=self.off_range[0], high=self.off_range[1])
        self.damping = np.random.uniform(low=self.damp_range[0], high=self.damp_range[1])
        if print_vals:
            self.print_values()

    def print_values(self):
        print "a: {0:.2f}, f: {1:.2f}, o: {2:.2f}, d: {3:.2f}".format(self.amplitude, self.frequency, self.offset, self.damping)

def damped_wave(x):
    y = np.cos(6 * np.pi * (x - 0.5)) * np.exp(-10 * (x - 0.5) ** 2)
    return y

def multi_peak(x):
    y = np.cos(6 * np.pi * (x - 0.5))
    return y

def basic_sine(x):
    y = (np.sin(x*2*np.pi + np.pi/4))/1.2
    return y


def zero_fun(x):
    return 0*x

def data1():
    x_rel = np.array([[0.6], [0.7]])
    uvi_rel = np.array([[0, 1], [1, 0]], dtype='int')
    uv_rel = x_rel[uvi_rel][:,:,0]
    y_rel = np.array([[1], [1]], dtype='int')
    fuv_rel = np.array([[-0.1, 0.1], [-0.1, 0.1]])

    x_abs = np.array([[0.2]])
    y_abs = np.array([[0.5]])
    mu_abs = np.array([[0.0]])

    return x_rel, uvi_rel, uv_rel, y_rel, fuv_rel, x_abs, y_abs, mu_abs
