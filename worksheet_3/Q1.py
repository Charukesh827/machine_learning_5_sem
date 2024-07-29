#binomial distribution

import scipy.stats as stats
import matplotlib.pyplot as plt
import math
# Define the parameters
n = 20  # Total number of trials
p = 0.1  # Probability of success (returning the item)

# Calculate the probability that exactly 5 customers will return the items
k = 5  # Number of successes
prob = stats.binom.pmf(k, n, p)
print(f"Probability that exactly {k} customers will return the items: {prob:.4f}")

# Create a list of all possible number of successes (0 to 20) and corresponding PMF values
successes = list(range(21))  # 0 to 20
pmf_values = [stats.binom.pmf(i, n, p) for i in successes]

# Draw a bar plot
plt.bar(successes, pmf_values)
plt.xlabel("Number of Customers Returning Items")
plt.ylabel("Probability")
plt.title("PMF of Binomial Distribution")
plt.show()

#Calculating the CDF of max 5 and for all values of successor
print("The probability of maximum of 5 returns is ",stats.binom.cdf(5,n,p))
cdf_value=[stats.binom.cdf(i,n,p) for i in successes]

#Drawing a line plot 
plt.plot(successes, cdf_value)
plt.xlabel("Number of Customers Returning Items")
plt.ylabel("Probability")
plt.title("CDF of Binomial Distribution")
plt.show()

# Calculate mean varience and Standard of the binomial distribution
mean = stats.binom.mean(n, p)
var = stats.binom.var(n, p)
print("The average number of customers to return : ",mean)
print("The varience is : ",var)
print("Standard deviation: ",math.sqrt(var))