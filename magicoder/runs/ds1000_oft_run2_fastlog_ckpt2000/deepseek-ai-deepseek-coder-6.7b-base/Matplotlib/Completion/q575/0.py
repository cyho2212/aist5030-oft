fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(time, Swdown, "-", label="Swdown")
ax1.plot(time, Rn, "-", label="Rn")
ax1.legend(loc=0)
ax1.grid()
ax1.set_xlabel("Time (h)")
ax1.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
ax1.set_ylim(-20, 100)

ax2.plot(time, temp, "-r", label="temp")
ax2.legend(loc=0)
ax2.grid()
ax2.set_xlabel("Time (h)")
ax2.set_ylabel(r"Temperature ($^\circ$C)")
ax2.set_ylim(0, 35)

plt.show()
plt.clf()
