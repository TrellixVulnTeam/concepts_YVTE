import gym
import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

from collections import deque


class DQN:
    def __init__(self, env):
        self.env = env
        self.memory = deque(maxlen=2000)

        self.gamma = 0.85
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.005
        self.tau = .125

        self.model = self.create_model()
        self.target_model = self.create_model()

    def create_model(self):
        model = Sequential()
        state_shape = self.env.observation_space.shape
        model.add(Dense(24, input_dim=state_shape[0], activation="relu"))
        model.add(Dense(48, activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(self.env.action_space.n))
        model.compile(loss="mean_squared_error",
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        self.epsilon *= self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.model.predict(state)[0])

    def remember(self, state, action, reward, new_state, done):
        self.memory.append([state, action, reward, new_state, done])

    def replay(self):
        batch_size = 32
        if len(self.memory) < batch_size:
            return

        samples = random.sample(self.memory, batch_size)
        for sample in samples:
            state, action, reward, new_state, done = sample
            target = self.target_model.predict(state)
            if done:
                target[0][action] = reward
            else:
                Q_future = max(self.target_model.predict(new_state)[0])
                target[0][action] = reward + Q_future * self.gamma
            self.model.fit(state, target, epochs=1, verbose=0)

    def target_train(self):
        weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        for i in range(len(target_weights)):
            target_weights[i] = weights[i] * self.tau + target_weights[i] * (1 - self.tau)
        self.target_model.set_weights(target_weights)

    def save_model(self, fn):
        self.model.save(fn)
        self.target_model.save("target_"+fn)

    def load_model(self, fn):
        self.model = load_model(fn)


def main():
    env = gym.make("MountainCar-v0")
    gamma = 0.9
    epsilon = .95

    trials = 1000
    trial_len = 500

    # updateTargetNetwork = 1000
    dqn_agent = DQN(env=env)
    steps = []
    for trial in range(trials):
        cur_state = env.reset().reshape(1, 2)
        step = 0
        for step in range(trial_len):
            action = dqn_agent.act(cur_state)
            new_state, reward, done, _ = env.step(action)

            # reward = reward if not done else -20
            new_state = new_state.reshape(1, 2)
            dqn_agent.remember(cur_state, action, reward, new_state, done)

            dqn_agent.replay()  # internally iterates default (prediction) model
            dqn_agent.target_train()  # iterates target model

            cur_state = new_state
            if done:
                break
        if step >= 199:
            print("Failed to complete in trial {}".format(trial))
            if step % 10 == 0:
                dqn_agent.save_model("trial-{}.model".format(trial))
        else:
            print("Completed in {} trials".format(trial))
            dqn_agent.save_model("success.model")
            break


def act(model, state):
    return np.argmax(model.predict(state)[0])


def run_model(filename):
    env = gym.make("MountainCar-v0")
    model = load_model(filename)
    print(f"model summary: {model.summary()}")

    # trials = 10
    # trial_len = 500
    #
    # # updateTargetNetwork = 1000
    # dqn_agent = DQN(env=env)
    # steps = []
    #
    # env.render()
    # for trial in range(trials):
    #     cur_state = env.reset().reshape(1, 2)
    #     for step in range(trial_len):
    #         action = dqn_agent.act(cur_state)
    #         new_state, reward, done, _ = env.step(action)
    #
    #         # reward = reward if not done else -20
    #         new_state = new_state.reshape(1, 2)
    #         dqn_agent.remember(cur_state, action, reward, new_state, done)
    #
    #         dqn_agent.replay()  # internally iterates default (prediction) model
    #         dqn_agent.target_train()  # iterates target model
    #
    #         cur_state = new_state
    #         if done:
    #             break
    #     if step >= 199:
    #         print("Failed to complete in trial {}".format(trial))
    #         if step % 10 == 0:
    #             dqn_agent.save_model("trial-{}.model".format(trial))
    #     else:
    #         print("Completed in {} trials".format(trial))
    #         dqn_agent.save_model("success.model")
    #         break

    """Evaluate agent's performance after Q-learning"""

    total_epochs, total_penalties = 0, 0
    episodes = 100

    for _ in range(episodes):
        print(f"episode: {_}")
        state = env.reset().reshape(1, 2)
        epochs, penalties, reward = 0, 0, 0

        done = False

        while not done:
            env.render()
            action = act(model, state)
            state, reward, done, info = env.step(action)
            state = state.reshape(1, 2)
            # print(state, reward, done, info)

            if reward == -1:
                penalties += 1

            epochs += 1

        total_penalties += penalties
        total_epochs += epochs

    print(f"Results after {episodes} episodes:")
    print(f"Average timesteps per episode: {total_epochs / episodes}")
    print(f"Average penalties per episode: {total_penalties / episodes}")


if __name__ == "__main__":
    # main()
    run_model("target_success.model")
