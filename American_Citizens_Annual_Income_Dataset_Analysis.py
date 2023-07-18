import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv(r".\income.csv")
# print(dataset)


# histogram podziału wiekowego
sns.histplot(data=dataset, x="age", bins=20, kde=True)
plt.xlabel("Wiek")
plt.ylabel("Ilość")
plt.title("Podział wiekowy")
plt.show()

# countplot zarobki względem płci
sns.countplot(data=dataset, x="income", hue="sex")
plt.xticks(rotation=90)
plt.xlabel("Sex")
plt.ylabel("Count")
plt.title("Podział zarobków względem płci")
plt.show()

# countplot podział zarobków względem poziomu wykształcenia
sns.countplot(data=dataset, x="education", hue="income")
plt.xticks(rotation=45)
plt.xlabel("Wyksztłcenie")
plt.ylabel("Ilość")
plt.title("Podział zarobków względem poziomu wykształcenia")
plt.legend(title="Zarobki", loc="upper right")
plt.show()

# Dystrybucja zarobków względem poziomu wykształcenia oraz stanu cywilnego
dataset_grouped = dataset.groupby(["education", "marital.status"])["income"].value_counts().unstack()
dataset_grouped.plot(kind="area", stacked=True)
plt.xticks(rotation=10)
plt.xlabel("Wyksztacenie oraz stan cywilny")
plt.ylabel("Ilość")
plt.title("Dystrybucja zarobków względem poziomu wykształcenia oraz stanu cywilnego")
plt.legend(title="Zarobki")
plt.show()

#Stosunek wieku do profesji
sns.violinplot(data=dataset, x="occupation", y="age")
plt.xticks(rotation=15)
plt.xlabel("Zawód")
plt.ylabel("Wiek")
plt.title("Stosunek wieku do profesji")
plt.show()
