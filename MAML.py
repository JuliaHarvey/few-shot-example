# Model-Agnostic Meta-Learning


class MAML():
    def __init__(self, alpha, beta, K, dist, theta = 1.0):
        self.C = None
        self.alpha = alpha
        self.beta = beta
        self.theta = theta #randomly initialize parameters (or can import pretrained parameters)
        self.K = K
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
