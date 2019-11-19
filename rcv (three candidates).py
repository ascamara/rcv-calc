## RANK CHOICE VOTING CALCULATOR for THREE CANDIDATES (-n, 0.1, n)
## Antonio Camara
## Columbia University
##
## external sources: https://www.science-emergence.com/Articles/How-to-integrate-a-normal-distribution-in-python-/ for normal distribution

##note
##this is a modified version of another program

from scipy.integrate import quad

import scipy.stats
import numpy as np

def normal_distribution_function(x):
    value = scipy.stats.norm.pdf(x,mean,std)
    return value

x_min = -999
x_max = 999

mean = 1.0 
std = 1.0
x = np.linspace(x_min, x_max, 100)
y = scipy.stats.norm.pdf(x,mean,std)

total, err = quad(normal_distribution_function, x_min, x_max)
print(total)

#politician class
class Politician:
  def __init__(self, ideology, pct):
    self.ideology = float(ideology)
    self.pct = float(pct)

  def __str__(self):
    return "Politician with ideology: {} and vote share: {}".format(self.ideology, self.pct)

  def win_print(self):
    return "Politician with ideology: {} and vote share: {} wins!".format(self.ideology, self.pct)

#function that checks if any candidates in a list have earned a majority
#also eliminates lowest polling candidate if no candidates have achieved a majority
#also prints winner
def check_and_eliminate(list):
  
  winner = False
  lowest = list[0];

  for x in list:
    if x.pct<lowest.pct:
      lowest = x
    if x.pct>=50:
      winner = True

  if(winner):
    can_win = list[0]
    for x in list:
      if x.pct > can_win.pct:
        can_win = x
    print("===")
    print(str(can_win)+" wins!")
    print("===")
    return True

  else:
    list.remove(lowest)
    return False

#function that runs an election round
#arguments: list of candidates competing and round number
def election_round(list, i):
  print("Election round: ", str(i))
  for x in range(0, len(list)):
    if(x == 0):
      x1 = x_min
      x2 = (list[0].ideology+list[1].ideology)/2

      res, err = quad(normal_distribution_function, x1, x2)
      list[x].pct = float(abs(res)*100.0)

    elif(x == len(list)-1):

      x1 = (list[x-1].ideology+list[x].ideology)/2
      x2 = x_max

      res, err = quad(normal_distribution_function, x1, x2)
      list[x].pct = float(abs(res)*100.0)

    else:
      x1 = (list[x-1].ideology+list[x].ideology)/2
      x2 = (list[x].ideology+list[x+1].ideology)/2

      res, err = quad(normal_distribution_function, x1, x2)
      list[x].pct = float(abs(res)*100.0)
  
  for i in list:
    print(i)
  print()

# create politicians
list = []
x = input("Enter ideology to test: ")
n=float(x)
list.append(Politician((-n), 0.0))
list.append(Politician(0.000000000000000000000000001, 0.0))
list.append(Politician(n, 0.0))

#round 1
print()
election_round(list, 1)

#runoff
i=2
while(check_and_eliminate(list) == False):
  election_round(list, i)
  i=i+1




  





