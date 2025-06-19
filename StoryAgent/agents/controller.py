#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controller agent implementation for story generation.
"""

import logging
import re
from .agent import BaseAgent, AgentState
from .llm import get_llm
from ..config import WorldInfo

class ControllerAgent(BaseAgent):
    """Controller agent that manages the story flow."""
    
    def __init__(self, model: str = "deepseek-chat"):
        """Initialize controller agent with model configuration."""
        super().__init__()
        self.logger = logging.getLogger(f"Story.Controller")
        self.llm = get_llm(model=model)
        self.logger.info(f"Story.Controller initialized with {model}")
    
    def _gen_prompt(self, state: AgentState) -> str:
        """Generate prompt for the controller agent."""
        prompt = f"""You are the host of a role-playing game, and you are responsible for managing the flow of the story. In this game you have a set of characters, and they are interacting with each other in a fictional world round by round. In each round, you will authorize one character depending on the situation of the story, and only this authorized character is allowed to speak or act at this round. Additionally, you also need to update the world state based on the conversation history. Your input includes the detailed description of the world, the detailed descriptions of the characters, the world state, and the role-playing history. The input texts are listed below.

## Characters

{"\n".join(f"### ID: {actor_id}\n{actor_info}\n" for actor_id, actor_info in state["actors"].items())}

## World State

{state["world_state"]}

## Role Play History

{"\n".join(f"### {sender}'s Round\n{content}\n" for sender, content in state["messages"])}

Please update the world state and select the character ID to authorize next. You can only update the \"current state\" field in the world state. You should place the updated current state in between <state> and </state> tags. You can only select the character ID from the list of characters. You should place the selected character ID in between <actor> and </actor> tags. Your output should be in the following format:

<state> UPDATED_CURRENT_WORLD_STATE </state>
<actor> CHARACTER_ID_TO_AUTHORIZE_NEXT </actor>

There are some IMPORTANT NOTES for you:
1. The \"description\" and the \"rules\" fields in the world state cannot be violated or changed. Your should only output the updated current state in the <state> tags. The state should be a complete and brief description of the current situation.
2. You should choose the most appropriate character to respond according to the current situation. You need to ensure the coherence and interactivity of the role-playing game. You should also promote multi-party dialogue."""
        return prompt
    
    def __call__(self, state: AgentState) -> AgentState:
        """Process the current state and return the next state."""
        self.logger.info(f"Story.Controller is acting...")
        response = self.llm.invoke([{"role": "user", "content": self._gen_prompt(state)}])

        msg = response.content
        new_current_state = re.search(r"<state>(.*?)</state>", msg, re.DOTALL)
        new_current_state = new_current_state.group(1).strip()
        next_actor_id = re.search(r"<actor>(.*?)</actor>", msg, re.DOTALL)
        next_actor_id = next_actor_id.group(1).strip()

        new_world_state = WorldInfo(
            description=state["world_state"].description,
            state=new_current_state,
            rules=state["world_state"].rules
        )
        self.logger.info(new_current_state)
        self.logger.info(next_actor_id)
        return AgentState(
            messages=state["messages"],
            actors=state["actors"],
            current_actor=next_actor_id,
            world_state=new_world_state
        )