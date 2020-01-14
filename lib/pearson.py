
# define function pearson

def pearson_r(x,y):
    """Compute Pearson correlation coefficient between two arrays."""

    # compute the correlation matrix
    corr_mat = np.corrcoef(x,y)

    # return entry [0 1]
    return corr_mat[0,1]
    
