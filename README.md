# Classroom-Scheduler
A program to schedule the classroom schedule using Greedy-Algorithm 

## What is Greedy
- Greedy is an algorithm that takes an object with the most value no looking back or thinking

## Why ends-earliest works
- I have 3 tasks
- 1:CODING : 9-12
- 2:KUMON : 9:30 - 10
- 3:STRETCH : 10-11
**Greedy** will only keep what is ending early: as a result we have only **Kumon** and **Stretching**
  But if i had rescedue i would move the 2 down (greedy wont do that)

## Where greedy fails
  - I have 3 items:
    - 1: A pencil costing 20₹ and has a weight of 1k
    - 2: An Eraser costing 20₹ and has a weight of 2k
    - 3: An laptop costing 30₹ and a weight of 3k
  - My bag can only hold 3k
  - *Greedy* will immediately take laptop so weight is 3k but value is 30₹
  - Where as if i take pencil and eraser we have weight of 3k but value of 40₹

## How to run
`python main.py`
