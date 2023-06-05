import pandas as pd
import matplotlib.pyplot as plt
import csv

# Load data from CSV file
df = pd.read_csv("tkhfacebook.csv")

# Group data by reaction type and calculate the total number of reactions
reaction_counts = df.groupby("reactions")["reaction_count"].sum()

# Group data by post ID and calculate the total number of comments
comment_counts = df.groupby("id")["comment_count"].sum()

# Create a bar chart to compare the number of reactions and comments
fig, ax = plt.subplots()
reaction_counts.plot(kind="bar", ax=ax, color="blue", label="Reactions")
comment_counts.plot(kind="bar", ax=ax, color="green", label="Comments")
ax.set_xlabel("Reaction/ID")
ax.set_ylabel("Count")
ax.set_title("Comparison of Facebook Reactions and Comments")
ax.legend()

# Show the plot
plt.show()
