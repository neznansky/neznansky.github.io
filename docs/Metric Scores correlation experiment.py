import pandas as pd
import numpy as np

# The two metrics' scores
A = pd.Series(np.random.randn(100000))
B = pd.Series(np.random.randn(100000))

# Data points that score high on both metrics
High = pd.Series(A>1.5) & (B>1.3)
num_High = sum(High)
df = pd.DataFrame({"A":A,"B":B,"H":High})

# Sampling our two groups
lowsample = df[df.H == False].sample(n=80)
highsample = df[df.H == True].sample(n=80)
combined = pd.concat([lowsample, highsample])

def ABcorr(df):
    return df.corr().loc["A","B"]

print("A: mean = {} and standard deviation = {}".format(A.mean(), A.std()))
print("B: mean = {} and standard deviation = {}".format(B.mean(), B.std()))
print('{} of the 100000 data points are "high scorers"'.format(num_High))
print()
print("Correlation of A and B in the combined sampling is {}".format(ABcorr(combined)))
print("Within the low-score group the correlation is {}".format(ABcorr(lowsample)))
print("Within the high-score group the correlation is {}".format(ABcorr(highsample)))
print("Within the \"entire population\" (n = 100000) the correlation is {}".format(ABcorr(df)))
