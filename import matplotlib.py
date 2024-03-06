import matplotlib.pyplot as plt
dias = [1,2,3,4,5,]
cresc = [1,4,8,16,32]
plt.bar(dias,cresc, color = '#6600cc')
plt.title('Intel UHD Graphics')
plt.xlabel('dias')
plt.ylabel('crescimeto')
plt.grid(True)


labels = 'Nina', 'Guilherme','Tavares', 'Raiane'
sizes = [0.5, 30, 50,15] 

fig,ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.title('veteranos dahora')
plt.figure(facecolor = 'purple')
plt.show()