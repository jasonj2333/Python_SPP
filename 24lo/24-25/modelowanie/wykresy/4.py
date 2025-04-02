import matplotlib.pyplot as plt

trump = 276
harris = 219
reszta = 538 - trump - harris

labels = ['Trump', 'Harris', 'Nierozstrzygnięte']
votes = [trump, harris, reszta]

fig, ax = plt.subplots()
ax.pie(votes, labels=labels, autopct='%1.1f%%')

plt.show()