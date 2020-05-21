
# define bootstrap analysisc

def bootstrap_analysis(data, size):
    # does boostrap analysis and plots the ecdf

    for i in range(size):

        # Generate a boostrap sample
        bs_sample = np.random.choice(data, size=len(data))

        # Compute and plot ECDF from boostramp sample
        x, y = ecdf(bs_sample)

        _=plot(x,y, marker='.', linestyle='none', color='lightgray, alpha=0.1)

    # compute and plot ECDF from original data
    x, y = ecdf(data)
    _=plt.plot(x,y, marker='.')

    # make margins
    plt.margins(0.02)
    _=plt.xlabel('original data')
    _=plt.ylabel('ECDF')

    # show the plot s
    plt.show()
