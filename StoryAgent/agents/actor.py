#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Actor agent implementation for story generation.
"""

import logging
import openai
from .agent import BaseAgent, AgentState
from ..config import ActorInfo

class ActorAgent(BaseAgent):
    """Actor agent that plays a character in the story."""
    
    def __init__(self, actor_id: str, actor_info: ActorInfo):
        """Initialize actor agent with character configuration."""
        self.actor_id = actor_id
        self.actor_info = actor_info
        self.logger = logging.getLogger(f"Actor.{self.actor_id}")
        self.logger.info(f"Actor.{self.actor_id} initialized")
        super().__init__()

    def _gen_prompt(self, state: AgentState) -> str:
        """Generate prompt for the actor agent."""
        prompt = f"""You are participating a role-playing game. You will be playing a character in a fictional world. You should act according to your character settings and respond to the world and other characters. Your input contains the detailed description of your character, the brief descriptions of other characters, the world state, and the conversation history. The input texts are listed below.
        
## Character Description

{self.actor_info}

## Other Characters

{"\n".join(f"### {actor_info.name}\n{actor_info.brief()}\n" for actor_id, actor_info in state["actors"].items() if actor_id != self.actor_id)}

## World State

{state["world_state"]}

## Role Play History

{"\n".join(f"### {sender}'s Round\n{content}\n" for sender, content in state["messages"])}

Please respond as your character, maintaining your personality traits and staying in character. Your response should be natural and engaging, reflecting your character's unique personality. Your response should also advance the overall story. In your response, you are allowed to do the following:

1. Speaking. You need to speak in first person. The words you speak must be placed between <speak> and </speak> tags.
2. Action. Besides physical actions, you can also take actions such as gestures, expressions, etc. The action you take must be placed between <action> and </action> tags."""
        return prompt

    def __call__(self, state: AgentState) -> AgentState:
        """Process the current state and return the next state."""
        self.logger.info(f"Actor.{self.actor_id} is acting...")
        prompt = self._gen_prompt(state)
        response = openai.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        new_message = response.choices[0].message.content
        self.logger.info(new_message)
        return AgentState(
            messages=state["messages"] + [(self.actor_info.name, new_message)],
            actors=state["actors"],
            current_actor=self.actor_id,
            world_state=state["world_state"]
        )