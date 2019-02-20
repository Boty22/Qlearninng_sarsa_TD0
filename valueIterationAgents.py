# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        max_err = 0.001
        iteration_number = 1
        #U1 = {s:0 for s in mdp.getStates() }
        U = util.Counter()
        while(iteration_number <= self.iterations):
            U = self.values.copy()
            delta = 0
            
            for s in mdp.getStates():
                T = []
                if(self.mdp.isTerminal(s)):
                    self.values[s] = 0
                


                else:
                    max_a = mdp.getPossibleActions(s)[0] 
                    max_sum = -999999999990
                    for a in mdp.getPossibleActions(s):
                        sum_for_a= 0
                        

                        
                        # T will store a list of (nextState,prob)
                        T = mdp.getTransitionStatesAndProbs(s,a) 
                        
                        for pair in T:
                            sum_for_a += pair[1] * U[pair[0]]

                        if(max_sum < sum_for_a):
                            max_sum = sum_for_a
                            max_a = a       

                    self.values[s] = mdp.getReward(s,max_a,T[0]) + self.discount * max_sum


                delta = max(delta, abs(self.values[s]-U[s]))
            
            if (delta <= max_err * (1-self.discount)/self.discount) :
                for key in U:
                   self.values[key] = U[key]
                break
        
            #last line inside while
            iteration_number +=1


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
               
        q_value = 0
        T = self.mdp.getTransitionStatesAndProbs(state,action)
        for pair in T:
          q_value += pair[1] * (self.mdp.getReward(state,action,pair[0]) + self.discount * self.values[pair[0]])

        return q_value


        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if(self.mdp.isTerminal(state)):
            return None

        max_a = self.mdp.getPossibleActions(state)[0] 
        max_sum = -99999999999
        for a in self.mdp.getPossibleActions(state):
            sum_for_a= 0
            
            # T will store a list of (nextState,prob)
            T = self.mdp.getTransitionStatesAndProbs(state,a) 
            
            for pair in T:
                sum_for_a += pair[1] * self.values[pair[0]]

            if(max_sum < sum_for_a):
                max_sum = sum_for_a
                max_a = a

        return max_a

        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
