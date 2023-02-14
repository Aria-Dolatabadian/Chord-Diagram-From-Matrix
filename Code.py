#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos
import pandas as pd

# Create matrix dataframe (3 x 6)
row_names = ["A1", "A2", "A3","A4", "A5","A6","A7","A8","A9","A10"]
col_names = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
matrix_data = [
    [40, 14, 13, 17, 5, 2,12,6,5],
    [7, 1, 6, 8, 12, 15,12,11,12],
    [9, 10, 13, 66, 11, 18,12,14,10],
    [9, 10, 3, 16, 11, 18,12,12,14],
    [9, 10, 3, 16, 11, 18,12,18,15],
    [9, 10, 23, 16, 11, 18,12,12,12],
    [9, 10, 3, 16, 11, 58,11,11,15],
    [9, 10, 3, 16, 11, 18,12,14,15],
    [9, 10, 3, 16, 11, 18,16,15,14],
    [9, 10, 3, 16, 11, 18,10,10,14],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    start=-265,
    end=95,
    space=1,
    r_lim=(93, 100),
    cmap="tab10",
    label_kws=dict(r=94, size=12, color="white"),
    link_kws=dict(ec="black", lw=0.5),
)

print(matrix_df)
fig = circos.plotfig()

plt.show()

