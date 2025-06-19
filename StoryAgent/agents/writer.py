#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import openai
from langgraph.graph import END
from .agent import BaseAgent, AgentState
from .llm import get_llm

class WriterAgent(BaseAgent):
    def __init__(self, lang: str = "中文", model: str = "deepseek-chat"):
        super().__init__()
        self.logger = logging.getLogger(f"Story.Writer")
        self.lang = lang
        self.writer_id = "__STORY_WRITER__"
        self.llm = get_llm(model=model)
        self.logger.info(f"Story.Writer initialized with {model} in {lang}")

    def _gen_prompt(self, state: AgentState) -> str:
        prompt = f"""You are a story writer. You will write a novel story based on the transcript of a role-playing game. In the role-playing game, there are several characters interacting with each other in a fictional world. In each round, only one character is allowed to speak or act. You are supposed to read the script of this whole game, and write a complete story based on the script. Your input includes the detailed description of the world, the detailed descriptions of the characters, the world state, and the role-playing history. The input texts are listed below.

## Characters

{"\n".join(f"### ID: {actor_id}\n{actor_info}\n" for actor_id, actor_info in state["actors"].items())}

## World State

{state["world_state"]}

## Role Play History

{"\n".join(f"### {sender}'s Round\n{content}\n" for sender, content in state["messages"])}

Please write a complete story based on the above script. You should maintain the characters' personalities. You should make the story not only interesting and vivid, but also conforming to the script.

There are some IMPORTANT NOTES for you:
1. You need to write the story in {self.lang}.
2. You must follow the script strictly. You are not supposed to add or remove any plots into or out of the script. If you find the script not smooth enough, you can slightly modify the script to make the story smoother."""

        return prompt
    
    def __call__(self, state: AgentState) -> AgentState:
        self.logger.info("Story.Writer is acting...")
        prompt = self._gen_prompt(state)
        response = self.llm.invoke([{"role": "user", "content": prompt}])
        summary = response.content
        self.logger.info(summary)
        return AgentState(
            messages=state["messages"] + [(self.writer_id, summary)],
            actors=state["actors"],
            current_actor=END,
            world_state=state["world_state"]
        )