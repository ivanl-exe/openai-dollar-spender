from typing import Union
from toml import load
from util.path import conjoin
from util.random import sequence
import openai

class Chat:
    def __init__(self, config: Union[tuple, str] = ('toml', '/config.toml')) -> None:
        if type(config) == tuple: config = conjoin(*config)
        self.config = config

        with open(self.config, 'r') as file:
            self.attributes = load(file)

            api = self.attributes['openai']
            self.api_key = api['api_key']
            openai.api_key = self.api_key

            user = api['user']
            self.prefix = user['prefix']
            
            engine = api['engine']
            self.model = engine['model']

            pricing = engine['pricing']
            self.input_pricing = pricing['input']
            self.output_pricing = pricing['output']
    
    def waste(self, n: int = 1000) -> int:
        
        #content = self.prefix.format(sequence(n // 2))
        content = 'Hello, world!'
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [{'role': 'user', 'content': content}]
        )
        print(response)
        usage = response['usage']
        prompt_tokens = usage['prompt_tokens']
        completion_tokens = usage['completion_tokens']

        input_cost = self.input_pricing * prompt_tokens / 1000
        output_cost = self.output_pricing * completion_tokens / 1000
        
        cost = input_cost + output_cost
        return cost