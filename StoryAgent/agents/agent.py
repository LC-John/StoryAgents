#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import TypedDict, Annotated, Sequence, NamedTuple, Dict, List, Tuple
from abc import ABC, abstractmethod
from ..config.config import WorldInfo, ActorInfo

class AgentState(TypedDict):
    messages: Annotated[List[Tuple[str, str]], "Message history (id -> content)"]
    actors: Annotated[Dict[str, ActorInfo], "Actor list (id -> info)"]
    current_actor: Annotated[str, "Current acting actor"] 
    world_state: Annotated[WorldInfo, "Current world state"]

class BaseAgent(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, state: AgentState) -> AgentState:
        pass
