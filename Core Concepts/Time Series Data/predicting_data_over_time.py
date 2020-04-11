import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('datasets/mimas01.xlsx', index_col=0)

clean_df = df[["Feed Scale (g)", "Temperature (C)", "Base Scale (g)" , "EFT (hours)"]]
clean_df.reset_index()
clean_df.set_index("EFT (hours)")

clean_df.plot.scatter(x="EFT (hours)", y="Base Scale (g)")
plt.show()
