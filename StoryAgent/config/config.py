#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configurations for the story generation system.
"""

from typing import List
from dataclasses import dataclass
import json

@dataclass
class ActorInfo:
    name: str
    gender: str
    age: int
    race_or_faction: str
    appearance: str
    backstories: List[str]
    persona: str
    goal: str

    @classmethod
    def from_file(cls, actor_config_path: str) -> 'ActorInfo':
        with open(actor_config_path, "r", encoding="utf-8") as f:
            actor_config = json.load(f)
        return cls(**actor_config)

    def brief(self) -> str:
        return f"""Name: {self.name}
Gender: {self.gender}
Age: {self.age}
Race or faction: {self.race_or_faction}
Appearance: {self.appearance}"""

    def __str__(self) -> str:
        return self.brief() + f"""
Personality: {self.persona}
Goal: {self.goal}
Backstories:
{"\n".join(f"  - {story}" for story in self.backstories)}"""

@dataclass
class WorldInfo:
    description: str
    state: str
    rules: List[str]

    @classmethod
    def from_file(cls, world_config_path: str) -> 'WorldInfo':
        with open(world_config_path, "r", encoding="utf-8") as f:
            world_config = json.load(f)
        return cls(**world_config)

    def __str__(self) -> str:
        return f"""Description: {self.description}
Rules:
{"\n".join(f"  - {rule}" for rule in self.rules)}
Current state: {self.state}"""