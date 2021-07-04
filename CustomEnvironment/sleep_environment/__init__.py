from gym.envs.registration import register

register(id="SleepEnv-v0",
         entry_point='sleep_environment.envs:SleepEnvironment')
