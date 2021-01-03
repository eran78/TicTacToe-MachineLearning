import random

from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, start

class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0

    return reward

my_agent = MyAgent()
random_agent = RandomAgent()

train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

start(player_x=my_agent)
