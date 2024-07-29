# Poisson Distribution
'''The probability that the number of calls 
will be maximum 5 can be calculated using the 
cumulative distribution function (CDF) of the Poisson distribution:'''
import scipy.stats as stats

# Define the parameters
mu = 10  # average number of calls per hour
k = 5    # maximum number of calls

# Calculate the probability
probability = stats.poisson.cdf(k, mu)
print(probability)

'''To calculate the probability that the number of calls
 over a 3-hour period will exceed 30, we need to 
 calculate the average number of calls over 3 hours, 
 which is 30 (10 calls/hour x 3 hours). 
 Then, we can use the CDF of the Poisson distribution 
 to calculate the probability that the number of calls 
 will be 30 or less, and subtract this value from 1 to 
 get the probability that the number of calls will 
 exceed 30:
'''
import scipy.stats as stats

# Define the parameters
mu = 30  # average number of calls over 3 hours
k = 30   # number of calls

# Calculate the probability
probability = 1 - stats.poisson.cdf(k, mu)
print(probability)