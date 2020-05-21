
# define the bernoulli function

def perfom_bernoulli_trials(n, p):

    """ Perfom n bernoulli trials with success probability P and retun number of successes"""

    # initialixe number of successes
    n_success = 0

    # perfom trials
    for i in range(n):
        # choose a random number between 0 and 1
        random_number = np.random.random()

        # if less than p its a success so add wone to n_success
        if random_number < p:
            n_success +=1

    return n_success
