# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KYZJNnPqDtSuuwiI1K6LdGLuWaa5Z6tQ
"""

#libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart_attack_dataset.csv')

#investigando os dados
print(df.info())

missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

#gráfico distribuição de idade
plt.figure(figsize=(12, 6))

sns.histplot(df["Age"], bins=20, kde=True, color="royalblue", edgecolor="black", alpha=0.7)

plt.title("distribuição de idade", fontsize=16, fontweight='bold')
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()

"""
*  A linha KDE (curva azul) indica a tendência geral da distribuição."""

#gráfico distribuição de gênero
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%',
        colors=["lightcoral", "cornflowerblue"], startangle=90,
        wedgeprops={'edgecolor': 'black'})

plt.title("distribuição de gênero", fontsize=14, fontweight="bold")

plt.show()

#gráfico BMI
plt.figure(figsize=(10, 6))

sns.histplot(df["BMI"], bins=25, kde=True, color="purple", edgecolor="black", alpha=0.7)

plt.title("Distribuição do Índice de Massa Corporal (BMI)", fontsize=14, fontweight="bold")
plt.xlabel("BMI", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

"""* BMI = body mass index"""

# Contagem de fumantes e não fumantes
smoking_count = df["Smoker"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(smoking_count, labels=smoking_count.index, autopct='%1.1f%%',
        colors=["lightgreen", "red"], startangle=90,
        wedgeprops={'edgecolor': 'black'})

plt.title("Distribuição de Fumantes e Não Fumantes", fontsize=14, fontweight="bold")

plt.show()

#ataque cardíaco x não
outcome_count = df["Outcome"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(outcome_count, labels=["Sem Ataque Cardíaco", "Com Ataque Cardíaco"],
        autopct='%1.1f%%', colors=["dodgerblue", "orange"], startangle=90,
        wedgeprops={'edgecolor': 'black'})

plt.title("Distribuição dos Desfechos de Ataque Cardíaco", fontsize=14, fontweight="bold")


plt.show()

plt.figure(figsize=(10, 6))

sns.histplot(df["BloodPressure"], bins=20, kde=True, color="coral", edgecolor="black", alpha=0.7)

plt.title("Distribuição da Pressão Arterial", fontsize=14, fontweight="bold")
plt.xlabel("Pressão Arterial (mmHg)", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

print(df["AlcoholConsumption"].value_counts())  # Verifica as categorias existentes
print(df["AlcoholConsumption"].unique())

"""* Correção dos valores"""

mapeamento = {0: "Não Bebe", 1: "Bebe (Moderado)", 2: "Bebe (Social)", 3: "Bebe (Frequente)", 4: "Bebe (Alcoólatra)"}

df["AlcoholConsumption_Clean"] = df["AlcoholConsumption"].replace(mapeamento)

alcohol_count = df["AlcoholConsumption_Clean"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(alcohol_count, labels=alcohol_count.index, autopct='%1.1f%%',
        colors=["lightgray", "lightblue", "dodgerblue", "darkblue", "darkred"],
        startangle=90, wedgeprops={'edgecolor': 'black'})

plt.title("Distribuição do Consumo de Álcool", fontsize=14, fontweight="bold")

plt.show()

#Contagem dos níveis de atividade física
activity_count = df["PhysicalActivity"].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=activity_count.index, y=activity_count.values, palette="viridis", hue=None, width=0.6)

for i, value in enumerate(activity_count.values):
    plt.text(i, value + 500, str(value), ha='center', fontsize=12, fontweight='bold', color='black')

plt.title("Nível de Atividade Física", fontsize=16, fontweight="bold")
plt.xlabel("Nível de Atividade", fontsize=14)
plt.ylabel("Contagem", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

"""

* Eixo X (horizontal) → Representa os diferentes níveis de atividade física.
* Eixo Y (vertical) → Mostra a quantidade de ocorrências de cada nível de atividade.
Cada barra do gráfico indica quantas pessoas (ou registros) pertencem a um determinado nível de atividade.




"""

#Contagem do histórico familiar
family_history_count = df["FamilyHistory"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(family_history_count, labels=family_history_count.index, autopct='%1.1f%%',
        colors=["purple", "lightblue"], startangle=90, wedgeprops={'edgecolor': 'black'})

plt.title("Histórico Familiar de Doença Cardíaca", fontsize=14, fontweight="bold")

plt.show()