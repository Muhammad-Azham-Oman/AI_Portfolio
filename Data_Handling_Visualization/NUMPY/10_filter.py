import numpy as np

a = np.arange(1,11)
even_number = a[a%2 == 0]
print(even_number)

# Filter with mask

mask = a>5
print(a[mask])