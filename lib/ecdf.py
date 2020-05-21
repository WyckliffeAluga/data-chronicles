
# definbe the function

def ecdf(data):
        """Compute ECDF for a one-dimensional array of measurements."""

        # number of points
        n = len(data)

        # x-data
        x = np.sort(data)

        # y-data
        y = np.arange(1, n+1) / n

        return x, y
