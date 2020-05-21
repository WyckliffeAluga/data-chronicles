
# define the function
def successive_poisson(tau1, tau2, size) :

    """ Compute time for arrival of 2 successive poisson processes."""

    # draw samples for first exponential distribution
    t1 = np.random.exponential(tau1, size)

    # draw samples for second exponential distribution
    t2 = np.random.exponential(tau2, size)

    return t1 + t2
    
