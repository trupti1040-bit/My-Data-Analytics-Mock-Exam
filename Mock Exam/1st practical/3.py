import pandas as pd
df = pd.DataFrame(
    {
    "stu_id":[101,102,103,104,105,106],
    "Name":["Trupti", "Kunal", "Sneha", "Isha", "Vedu", "Bhavesh"],
    "Age": [24,55,40,35,20,30],
    "Marks":[96,78,25,45,50,35],   
    }
)
print("Original Data:\n",df)
print("\nSubset (Marks)>30:\n",df[df["Marks"]>30])
print("\nSorted by marks(Ascending):\n",df.sort_values("Marks"))
print("\nSorted by marks(Desecnding):\n",df.sort_values("Marks",ascending=False))
print("\nGrouped(Average Marks by name):\n",df.groupby("Name")["Marks"].mean())
print("\nMean=",df["Marks"].mean())
print("\nMedian=",df["Marks"].median())
print("\nMode=")
print(df["Marks"].mode())