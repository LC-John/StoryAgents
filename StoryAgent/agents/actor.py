#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Actor agent implementation for story generation.
"""

import logging
import re
from typing import List, Tuple
from .agent import BaseAgent, AgentState
from .llm import get_llm
from ..config import ActorInfo

class ActorAgent(BaseAgent):
    """Actor agent that plays a character in the story."""
    
    def __init__(self, actor_id: str, actor_info: ActorInfo, model: str = "deepseek-chat"):
        """Initialize actor agent with character configuration."""
        super().__init__()
        self.actor_id = actor_id
        self.actor_info = actor_info
        self.logger = logging.getLogger(f"Actor.{self.actor_id}")
        self.llm = get_llm(model=model)
        self.logger.info(f"Actor.{self.actor_id} initialized with {model}")

    def _filter_thoughts(self, messages: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Filter out the thoughts from the messages."""
        filtered_messages = []
        for sender, content in messages:
            if sender == self.actor_info.name:
                filtered_messages.append((sender, content))
            else:
                filtered_content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL)
                filtered_messages.append((sender, filtered_content))
        return filtered_messages

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

{"\n".join(f"### {sender}'s Round\n{content}\n" for sender, content in self._filter_thoughts(state["messages"]))}

Please respond as your character, maintaining your personality traits and staying in character. Your response should be natural and engaging, reflecting your character's unique personality. Your response should also advance the overall story. In your response, you are allowed to do the following:

1. Thinking. You can simulate the development of the event in your mind, or conjecture other characters' internal activities, etc. You must place your thoughts (i.e., what is going on in your own mind) in between <think> and </think> tags.
2. Speaking. You need to speak in first person. The words you speak must be placed between <speak> and </speak> tags.
3. Action. Besides physical actions, you can also take actions such as gestures, expressions, etc. The action you take must be placed between <action> and </action> tags.

There are some IMPORTANT NOTES for you:
1. Your thoughts are only visible to yourself, and so do other characters. Specifically, in the role-playing history, you are the only one who can see your own thoughts, and for other characters, they can only see your words and actions.
2. Your words and actions must be consistent with your character's personality and your thoughts.
"""
        return prompt

    def __call__(self, state: AgentState) -> AgentState:
        """Process the current state and return the next state."""
        self.logger.info(f"Actor.{self.actor_id} is acting...")
        prompt = self._gen_prompt(state)
        response = self.llm.invoke([{"role": "user", "content": prompt}])
        new_message = response.content
        self.logger.info(new_message)
        return AgentState(
            messages=state["messages"] + [(self.actor_info.name, new_message)],
            actors=state["actors"],
            current_actor=self.actor_id,
            world_state=state["world_state"]
        )