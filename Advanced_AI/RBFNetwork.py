import gym
import numpy as np
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import StandardScaler
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDRegressor

class FeatureTransformer:
  def __init__(self, env, n_components=500):
    observation_examples = np.array([env.observation_space.sample() for x in range(10000)])
    scaler = StandardScaler()
    scaler.fit(observation_examples)

    # Used to converte a state to a featurizes represenation.
    # We use RBF kernels with different variances to cover different parts of the space
    featurizer = FeatureUnion([
            ("rbf1", RBFSampler(gamma=5.0, n_components=n_components)),
            ("rbf2", RBFSampler(gamma=2.0, n_components=n_components)),
            ("rbf3", RBFSampler(gamma=1.0, n_components=n_components)),
            ("rbf4", RBFSampler(gamma=0.5, n_components=n_components))
            ])
    example_features = featurizer.fit_transform(scaler.transform(observation_examples))

    self.dimensions = example_features.shape[1]
    self.scaler = scaler
    self.featurizer = featurizer

  def transform(self, observations):
    # print "observations:", observations
    scaled = self.scaler.transform(observations)
    # assert(len(scaled.shape) == 2)
    return self.featurizer.transform(scaled)


env = gym.make('MountainCar-v0')
env.reset()
env._max_episode_steps = 400
gamma = 0.99
ft = FeatureTransformer(env)

model = []
#Init model as a list of SGDRegressor
for i in range(env.action_space.n):
    m = SGDRegressor()
    m.partial_fit(ft.transform([env.reset()]),[0])
    model.append(m)


def predict(observation):
    result =[]
    for m in model:
        G = m.predict(ft.transform([observation]))
        result.append(G)

    return result

def sample_action(s):
    # eps = 0
    # Technically, we don't need to do epsilon-greedy
    # because SGDRegressor predicts 0 for all states
    # until they are updated. This works as the
    # "Optimistic Initial Values" method, since all
    # the rewards for Mountain Car are -1.
    if np.random.random() < 0.05:
      return env.action_space.sample()
    else:
      result = predict(s)
      return result.index(max(result))

def update(s,a,G):
    X= ft.transform([s])
    assert(len(X.shape) == 2)
    model[a].partial_fit(X , [G] )


def play_one():
    observation = env.reset()
    done = False
    totalreward = 0
    while not done:
        env.render()
        a = sample_action(observation)
        prev = observation
        #a = env.action_space.sample()
        observation, reward, done, info = env.step(a)
        G = reward + gamma* max(predict(observation))
        update(prev,a,G)
        totalreward += reward

    return totalreward


for i in range(300):
    r = play_one()
    print(r)




env.close()

'''
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
'''
