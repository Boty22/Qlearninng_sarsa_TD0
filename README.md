# TD-0 and Sarsa for Pac-Man and Grid World
## Introduction
Games are experimental systems for Artificial Intelligence. They allow AI scientists to compare algorithms and set baselines for performance. The AI community continuously implements games as learning environments. 
UC Berkeley course [CS188](https://inst.eecs.berkeley.edu/~cs188/sp19/), Introduction to Artificial Intelligence, uses the game Pac-Man and a simplied version of the environment called GridWorld. As part of the course, the project 3 reques the implementation of Dynamic programing methods (Value/Policy Iteration) and one reinforcement learning method(Q-Learning).
I have expanded the required work and implemented two additional reinforcement learning methods: TD-0 an Sarsa.

## Notes on the Reinforcement Learning Environment
* States: position of the agent
* Actions: north, south, east, west 
* The original reinforcement learninv environment (Pacman game) was impemented with Python 2. Be sure to have Python to in your system so you can run test the algorithms.

## Run the Algorithm
Downland the repository
```sh
$ python2 gridworld.py -a sarsa -k 100 -s 5 -e 0.5
```

```sh
$ python2 gridworld.py -a td0 -i 100 -k 10 s 10 e 0.4
```

:+1::octocat: 
