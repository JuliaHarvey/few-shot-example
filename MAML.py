# Model-Agnostic Meta-Learning

class MAML():
    def __init__(self, alpha, beta, K, theta = 1.0):
        self.C = None
        self.alpha = alpha
        self.beta = beta
        self.theta = theta #randomly initialize parameters (or can import pretrained parameters)
        self.K = K
    
    def train(num_episodes = 50):
        curr_episode = 1
        while curr_episode != num_episodes:
            #sample batch
            sample_batch = []
            for batch in sample_batch:
                evaluate(batch)
                #update theta
    
    def evaluate(batch):
        examples = []
        for image in examples:
            C.evaluate(image)
