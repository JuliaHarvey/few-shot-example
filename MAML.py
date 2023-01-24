# Model-Agnostic Meta-Learning
import random

class MAML():
    def __init__(self, alpha, beta, K, dist, theta = random.random()):
        self.C = None
        self.alpha = alpha
        self.beta = beta
        self.theta = theta
        self.K = K #number of examples from training set (1 for one-shot, some for few-shot, etc)
        self.dist = dist #distribution over tasks
    
    def train(self, num_episodes = 50):
        curr_episode = 1
        while curr_episode != num_episodes:
            #sample batch
            sample_batch = []
            for batch in sample_batch:
                self.evaluate(batch)
                #update theta
    
    def evaluate(self, batch):
        examples = []
        for image in examples:
            self.C.evaluate(image)
