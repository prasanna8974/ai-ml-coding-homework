import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 7, 8, 9, 10],
    "Marks": [30, 35, 40, 45, 75, 80, 85, 90]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(df[["Hours", "Marks"]])

print(df)

plt.scatter(df["Hours"], df["Marks"], c=df["Cluster"], cmap="viridis")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()