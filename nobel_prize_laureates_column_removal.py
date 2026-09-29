#removing unneccesary columns from nobel-prize-laureates
import pandas as pd

nobel_df = pd.read_csv("nobel-prize-laureates.csv")

nobel_df = nobel_df[["awardYear", "category", "name"]]
print(nobel_df)

nobel_df.to_csv("nobel-prize-laureates.csv")