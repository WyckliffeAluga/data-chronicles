import numpy as np
import matplolib.pyplot as plt


class Boostrap :

    # initialize the calss
    def __init__ (self, data, func, size=1) :
        self.data = data
        self.func = func
        self.size = size

    def boostrap_replicate_1d(self):
        return self.func(np.random.choice(self.data, size=len(self.data)))

    def draw_bs_replicates(self):

        """ Draw boostrap replicates """

        # initialize array of replicates
        bs_replicates = np.empty(self.size)

        # generate replicates
        for i in range(self.size):
            bs_replicates[i] = boostrap_replicate_1d()

        return bs_replicates
