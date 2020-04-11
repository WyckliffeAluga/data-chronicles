
from scipy.cluster.hierarchy import linkage
import pandas as pd
import random , timeit

points = 100

df = pd.DataFrame({"x": random.sample(range(0, points), points),
                   "y": random.sample(range(0, points), points)})

%timeit linkage(df[["x","y"]], method="ward", metric='euclidean')           
