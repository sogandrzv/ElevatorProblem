# ElevatorProblem
This is an algorithm for an elevator in a 15-floor building.

## Description
Here is the algorithm we used for elevator:
- We use 
<a href="https://www.geeksforgeeks.org/look-disk-scheduling-algorithm/">look algorithm</a> 
with an optimization. The optimization: after the elevator gets a queue of requests, it breaks the queue into 2 sub-queue and then responds to each. This reduces the waiting time for people.

## Usage
If you want to test the algorithm you can create a passenger in the main like this:
```
manager.create_passenger(destination, typeOfRequest)
# destination is an Integer
# typeOfRequest is "internal" or "external"
```
and then run the program
