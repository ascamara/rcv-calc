# rcv-calc
A rank-choice voting (instant-runoff) calculator

These programs determine which candidates will win elections under a ranked-choice voting system or instant-runoff voting system, given candidates' ideology as a floating point.

The first allows you to input a number of candidates and assign each an ideology and determine which candidate wins under RCV (it prints each round of the election so you can follow along). 

The second allows you to input an ideology, n, and then test that ideology with your conjecture: that is, candidate 1 is assigned -n, candidate 2 is an \epsilon>0 and candidate 3 is assigned n. 

This program was created to assist in some work on electoral theory done under the supervision of Dr. Prato at Columbia University, department of Political Science.

A note: I wrote the programs with a normal distribution of mean and std dev = 1, but this is easily modifiable in the program.

A note: I recommend that when entering ideological values for candidates you do so in increasing order (e.g. -5, -1.1, 3, 6.7). 
