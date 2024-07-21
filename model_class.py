import docplex
from docplex.mp.model import Model


class psh_model(Model):
    def __init__(self) -> None:
        super().__init__
        self.name = "Hello"
        
