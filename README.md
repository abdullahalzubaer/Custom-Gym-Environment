# Custom OpenAI Gym environment

---

In this repository I will document step by step process how to create a custom OpenAI Gym environment. From creating the folders and the necessary files, installing the package with pip and creating an instance of the custom environment as follows. With which later we can plug in RL/DRL agents to interact with the environment. 

```python
env = gym.make('CustomEnvironment')
```
---

#### The folder structure will be like below:

```
CustomEnvironment/
 README.md
 setup.py 
 sleep_environment/
  __init__.py
  envs/
   __init__.py
   main.py  
```
---
##### CustomEnvironment/setup.py 

Contains name of the package we are going to install and also we are going to import that package for working, version and the list of librariers needed for the package to function.

```python

from setuptools import setup


setup(name='sleep_environment',
      version='0.01',
      install_requires=['gym'])

```


---
##### CustomEnvironment/sleep_environment/__init__.py 

We have to register the custom environment and the the way we do it is as follows below. The id will be used in gym.make("SleepEnv-v0"). entry_point referes to the location where we have the custom environment class i.e. the folder. Naming convention of the custom environment should be like this "NAME-vX", X = version number, NAME = name of the custom environment.

```python

from gym.envs.registration import register

register(id="SleepEnv-v0",
         entry_point='sleep_environment.envs:SleepEnvironment')

```
---
##### CustomEnvironment/sleep_environment/envs/__init__.py

Exact location of our custom environment class and import it.

```python
from sleep_environment.envs.main import SleepEnvironment

```

---
##### CustomEnvironment/sleep_environment/envs/main.py 

Contains the Custom environment class

```python

import gym
from gym import error, spaces, utils
from gym.utils import seeding


class SleepEnvironment(gym.Env):
    
    message = "I am from custom sleep environmennt"

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass


```

When the folders has been organized in this way then open command prompt in the location where we have setup.py and run the following command to install the package via pip.

```
pip install -e .
```

After successful installion of our custom environment we can work with this environment by following the below process, for example in Jupyter Notebook.

```python

>>> import gym
>>> import sleep_environment
>>> env = gym.make("SleepEnv-v0")
>>> env.message
>>> "I am from custom sleep environmennt"
```

Remark: Even if after successful installation we cannot import the environment, in the case of Jupyter notebook, restart the kernel. Hopefully, it will work.








---
Reference: 

 1. https://github.com/openai/gym/blob/master/docs/creating-environments.md
 2. https://www.saashanair.com/custom-envs-in-openai-gym/


# Todo

<!-- - Add detail structure (basic) of an environment required by gym. -->
- Detail basic structure and purpose of each methods in our custom environment class.
- When and why we might be interested for custom environment.
