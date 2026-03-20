# cons=[{'type':'ineq', 'fun': lambda x: x[t]}]

out=minimize(function, x0, method="SLSQP", constraints=cons)
x=out["x"]
