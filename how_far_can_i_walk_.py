# -*- coding: utf-8 -*-
"""How far can I walk?.ipynb



"""## HOW FAR CAN I WALK?

Rules:

1. If you roll a 1, 2: You go 1 step down
2. If you roll a 3,4 or 5: You go 1 step up
3. If you role a 6: You roll again and walk up the resulting number of steps

Things to take into consideration:

1. Cant go below step 0
2. 0.1% chance of falling down the stairs - If this happens, then you have to start again
3. You made a bet with your friend that you will reach step 60

What is the chance we will win this bet?

We are going to stimulate the process
"""

# We need a random generator

import numpy as np

np.random.randint(1,7) # Randomly gen numbers from 1,6

import numpy as np

step = 50

dice = np.random.randint(1,7)

if dice <= 2:
  step = step - 1
elif dice >= 3 and dice <= 5:
  step = step +1
else:
  step = step + np.random.randint(1,7)

print(dice, step)

"""If we want to model a random path e.g. stock valuation, then we need to know how to create a list using a for loop"""

# How to create a list using a for loop:

import numpy as np
np.random.seed(123)

list = []

for x in range(11):
  coin_outcome = np.random.randint(1,3)
  if coin_outcome == 1:
    list.append('Head')
  else:
    list.append('Tails')


print(list)

list.count('Tails')

# We also want to count the number of tails in our simulated list:

import numpy as np
np.random.seed(123)

H_or_T = []
no_of_tails = []

for x in range(11):
  coin_outcome = np.random.randint(1,3)
  if coin_outcome == 1:
    H_or_T.append('Head')
  else:
    H_or_T.append('Tails')
  no_of_tails.append(H_or_T.count('Tails'))


print(H_or_T)
print(no_of_tails)

random_walk = [0]

print(type(random_walk))

random_walk = [0]

for x in range(11):
  step = random_walk[-1] # Step is the last element of random_walk
  dice = np.random.randint(1,7)
  if dice <= 2:
    step = step - 1
  elif dice >= 3 and dice <= 5:
    step = step +1
  else:
    step = step + np.random.randint(1,7)
  random_walk.append(step)

# Initially I wrote random_walk = random_walk.append(step)
# But that is wrong

print(random_walk)

"""This shows the amount of steps it took in 10 rounds (based on the number of the dice)"""

# Lets now visualise the walk using matplotlib

import matplotlib.pyplot as plt

x = [1, 2 ,3 ,4 ,5 , 6, 7, 8, 9, 10, 11, 12]

plt.scatter(x, random_walk, c = 'Green')

plt.xlabel('Rounds')
plt.ylabel('Cumulative Step')

plt.title('The cumulative number of steps after each round')

plt.show()

# Lets see if a line graph looks better:

import matplotlib.pyplot as plt

x = [1, 2 ,3 ,4 ,5 , 6, 7, 8, 9, 10, 11, 12]

plt.plot(x, random_walk, c = 'Green')

plt.xlabel('Rounds')
plt.ylabel('Cumulative Step')

plt.title('The cumulative number of steps after each round')

plt.show()

# If we pass only 1 arguement,
# Python will assume x = element index, y = the arguement given

import matplotlib.pyplot as plt

plt.plot(random_walk, c = 'Green')

plt.ylabel('Cumulative Step')

plt.title('The cumulative number of steps after each round')

plt.show()

# Lets increase the number of rounds to see if we actually reach step 60

random_walk = [0]

for x in range(100):
  step = random_walk[-1] # Step is the last element of random_walk
  dice = np.random.randint(1,7)
  if dice <= 2:
    step = step - 1
  elif dice >= 3 and dice <= 5:
    step = step +1
  else:
    step = step + np.random.randint(1,7)
  random_walk.append(step)

import matplotlib.pyplot as plt

plt.plot(random_walk, c = 'Green')

plt.ylabel('Number of Steps From Origin')
plt.xlabel('Number xth Dice Roll')

plt.title('The Number of Steps From Origin, After Each Dice Roll')

plt.show()

"""Now we simulated the walk. We need to implement 'clumsiness'. If we fall, then we need to start. From the question we know that there is a 0.1% chance of falling.

So, what is the chance of reaching step 60?


"""

# Now we want to simulate this experimemt, 100 times.
# So lets try simulate the coin experiment first.
#Then apply our code to the 'walk' example.
# We want the number of tails if we repeat this 100 times:

import numpy as np
np.random.seed(123)



# Get a list of HT outcomes in 1 experiment(10 trails)
# Count the number of tails after 1 experiment
# Simulate this 100 times:


final_tails = []

for experiment_no in range(100):
  H_or_T = []
  no_of_tails = []
  for trail in range(10):
    coin_outcome = np.random.randint(1,3)
    if coin_outcome == 1:
      H_or_T.append('Head')
    else:
      H_or_T.append('Tails')
    no_of_tails.append(H_or_T.count('Tails'))
  final_tails.append(max(no_of_tails))

# We knew to use max
# The reason why we have to put the H_or_T and no_of_tails list
# in the outer for loop, is because after the inner for loop
# iteration is done, we want to reset the H_or_T and
# no_of_tails list, as a new experiment starts.



print(H_or_T)
print(no_of_tails)
print(final_tails)

a = len(final_tails)

"""This means that in the

1st experiment: 4 tails,  
2nd experiment: 5,
3rd experiment: 6

and so on...
"""

# Now lets try and visualise the distribution
# We are going to use a histogram

import matplotlib.pyplot as plt

experiment_no = list(range(1, 101))

plt.hist(experiment_no ,weights = final_tails, bins = len(final_tails))
plt.show()

import matplotlib.pyplot as plt


plt.hist(final_tails, bins=len(final_tails), width=1.1, align = 'mid')
plt.xlabel('Number of Tails after each experiment')
plt.ylabel('Frequency')
plt.title('Histogram of Tails in 100 Experiments')

plt.ylim(0, 30)  # Changing y-axis scale
plt.xlim(0, 10)  # Adjust x-axis limit based on the range of experiment numbers

plt.show()

"""If we do more experiments, the histogram will converge to a normal bell curve"""

# Now we had a chance to visualise the coin experiment.
# Lets try to visualise the walk experiment after we simulate the
# experiment 100 times

# So first we need to simulate 100 experiments


total_steps = []

for experiment_no in range(100):
  random_walk = [0]
  for x in range(100):
    step = random_walk[-1] # Step is the last element of random_walk
    dice = np.random.randint(1,7)
    if dice <= 2:
      step = step - 1
    elif dice >= 3 and dice <= 5:
      step = step +1
    else:
      step = step + np.random.randint(1,7)
    random_walk.append(step)
  total_steps.append(max(random_walk))

print(random_walk)
print(total_steps)

# As you can see, the person is travelling -1 steps
# But thats not possible. So lets fix that

total_steps = []

for experiment_no in range(100):
  random_walk = [0]
  for x in range(100):
    step = random_walk[-1] # Step is the last element of random_walk
    dice = np.random.randint(1,7)
    if dice <= 2:
      step = max(0, step - 1)
    elif dice >= 3 and dice <= 5:
      step = step +1
    else:
      step = step + np.random.randint(1,7)
    random_walk.append(step)
  total_steps.append(max(random_walk))

print(random_walk)
print(total_steps)

len(total_steps)

# Now that we simulated 100 experiments
# Lets visualise it

import matplotlib.pyplot as plt

plt.hist(total_steps, bins= len(total_steps) )
plt.xlabel('Total No of Steps travelled after each experiment')
plt.ylabel('Frequency')
plt.title('Histogram Demonstrating the Distribution of the Total No of Steps Travelled in 100 Experiments')

plt.ylim(0, 10)

plt.show()

# Lets see what would happen if we increase the number of experiments:


total_steps = []

for experiment_no in range(1000):
  random_walk = [0]
  for x in range(100):
    step = random_walk[-1] # Step is the last element of random_walk
    dice = np.random.randint(1,7)
    if dice <= 2:
      step = max(0, step - 1)
    elif dice >= 3 and dice <= 5:
      step = step +1
    else:
      step = step + np.random.randint(1,7)
    random_walk.append(step)
  total_steps.append(max(random_walk))

print(total_steps)


import matplotlib.pyplot as plt

plt.hist(total_steps, bins= len(total_steps), width = 1.1 )
plt.xlabel('Total No of Steps travelled after each experiment')
plt.ylabel('Frequency')
plt.title('Histogram Demonstrating the Distribution of the Total No of Steps Travelled in 1000 Experiments')



plt.show()

"""As you can see, as we increase the no of experiments, the distribution becomes more continous."""

# Now we have to implement the clumsiness

# There is a 0.1% chance of falling down.
# If we do, then we have to start again i.e step = 0

import numpy as np

total_steps = []

for experiment_no in range(1000):
  random_walk = [0]
  for x in range(100):
    step = random_walk[-1] # Step is the last element of random_walk
    dice = np.random.randint(1,7)
    if dice <= 2:
      step = max(0, step - 1)
    elif dice >= 3 and dice <= 5:
      step = step +1
    else:
      step = step + np.random.randint(1,7)
    if np.random.rand() <= 0.001: # This is where we implement clumsiness
      step = 0
    random_walk.append(step)
  total_steps.append(max(random_walk))

print(total_steps)


import matplotlib.pyplot as plt

plt.hist(total_steps, bins= len(total_steps), width = 1.1 )
plt.xlabel('Total No of Steps travelled after each experiment')
plt.ylabel('Frequency')
plt.title('Histogram Demonstrating the Distribution of the Total No of Steps Travelled in 1000 Experiments (with clumsiness)')

plt.ylim(0,35)


plt.show()

# Now that we plotted the distribution,
# We need to see the probability of reaching step 60

# From the graph, we can see that there is a high probability of reaching step 60
# Now lets calc the actual probability


# How many times did we reach step 60 or higher:
# Lets convert the total_steps list to an array:

np_total_steps = np.array(total_steps)

print(np_total_steps)

# Now lets extract the values that are bigger or equal to 60

np_total_steps[np_total_steps >= 60]

# Now lets workout the length of this array:

np_total_steps_60 = np_total_steps[np_total_steps >= 60]

len(np_total_steps_60)

# Thus 805 experiments consisted of the ppt reaching atleast step 60.
# Now lets workout the probability

Probability_of_reaching_step_60 = (len(np_total_steps_60) / 1000) * 100

print(Probability_of_reaching_step_60)

"""Therefore, there is a 80.3% chance that we will reach step 60. This means that there is a 80.3% chance we will win the bet.

Thus, I recommend taking on the bet.
"""
