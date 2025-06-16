#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
StoryAgents - A multi-agent story generation system
Main entry point for the story generation workflow.
"""

import os
import logging
from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import openai
from config import AGENTS, WORLD_RULES

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('story_agents.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
logger.info("Environment variables loaded")

# Configure OpenAI client
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.base_url = "https://api.deepseek.com/"
logger.info("OpenAI client configured with DeepSeek API")

# State Management
class AgentState(TypedDict):
    messages: Annotated[Sequence[str], "对话历史"]
    current_agent: Annotated[str, "当前行动的agent"]
    context: Annotated[str, "当前场景描述"]
    world_state: Annotated[str, "世界状态描述"]

def create_agent(agent_id: str):
    """Create an agent with specific role and persona."""
    agent_info = AGENTS[agent_id]
    logger.info(f"Creating agent: {agent_info['name']} ({agent_id})")
    
    def agent(state: AgentState) -> AgentState:
        logger.info(f"Agent {agent_info['name']} ({agent_id}) is acting...")
        # Create prompt for the agent
        prompt = f"""你是一个角色扮演AI，扮演{agent_info['name']}，{agent_info['role']}。
角色特点：
- 性格：{agent_info['persona']}
- 能力：{', '.join(agent_info['abilities'])}

当前场景：
{state['context']}

世界规则：
{WORLD_RULES}

对话历史：
{chr(10).join(state['messages'])}

请以{agent_info['name']}的身份回应，保持角色特点，推动故事发展。使用**加粗**来标记对话内容，使用*斜体*来标记动作和表情。"""
        
        # Get response from DeepSeek
        response = openai.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Update state
        new_message = response.choices[0].message.content
        return {
            "messages": [*state["messages"], new_message],
            "current_agent": state["current_agent"],
            "context": state["context"],
            "world_state": state["world_state"]
        }
    
    return agent

def create_story_controller():
    """Create a story controller agent that decides the next agent to act."""
    logger.info("Creating story controller")
    def story_controller(state: AgentState) -> AgentState:
        logger.info("Story controller is deciding next agent...")
        # Create prompt for the story controller
        prompt = f"""你是一个故事控制AI，负责决定下一个应该行动的agent。
当前场景：
{state['context']}

世界规则：
{WORLD_RULES}

对话历史：
{chr(10).join(state['messages'])}

请根据当前故事发展，选择下一个应该行动的agent。可选的agent有：
{', '.join(AGENTS.keys())}

选择规则：
1. 优先选择与上一个发言的agent不同的agent，以促进多方对话
2. 根据当前话题和场景，选择最合适的agent来回应
3. 确保对话的连贯性和互动性

只需回复agent的ID，不要添加任何其他内容。"""
        
        # Get response from DeepSeek
        response = openai.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Update state
        next_agent = response.choices[0].message.content.strip()
        return {
            "messages": state["messages"],
            "current_agent": next_agent,
            "context": state["context"],
            "world_state": state["world_state"]
        }
    
    return story_controller

def create_summarizer():
    """Create a summarizer agent that creates a polished version of the story."""
    logger.info("Creating summarizer")
    def summarizer(state: AgentState) -> AgentState:
        logger.info("Summarizer is creating the final story...")
        # Create prompt for the summarizer
        prompt = f"""你是一个故事总结AI，负责将对话历史整理成一个完整的故事。
当前场景：
{state['context']}

世界规则：
{WORLD_RULES}

对话历史：
{chr(10).join(state['messages'])}

请将以上内容整理成一个完整的故事，保持角色的特点，增强情感表达，使故事更加连贯和生动。
使用"=== The Chronicler's Tale ==="作为故事的开始标记。"""
        
        # Get response from DeepSeek
        response = openai.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Update state
        summary = response.choices[0].message.content
        logger.info("Story summarization completed")
        return {
            "messages": [*state["messages"], summary],
            "current_agent": END,  # Set to END to properly terminate the workflow
            "context": state["context"],
            "world_state": state["world_state"]
        }
    
    return summarizer

def should_continue(state: AgentState, max_iter: int = 1) -> bool:
    """Determine if the conversation should continue."""
    
    # Count only the messages from acting agents (excluding the summarizer's message)
    acting_messages = [msg for msg in state["messages"] if "=== The Chronicler's Tale ===" not in msg]
    logger.debug(f"Checking if conversation should continue. Current message count: {len(acting_messages)}")
    
    # If we've already summarized, end the workflow
    if any("=== The Chronicler's Tale ===" in msg for msg in state["messages"]):
        logger.info("Story has been summarized, ending workflow")
        return False
    
    # If we've reached max iterations, go to summarizer
    if len(acting_messages) >= max_iter:
        logger.info(f"Reached max iterations ({max_iter}), proceeding to summarizer")
        return False  # Return False to trigger summarization
    
    # Otherwise, continue with acting agents
    logger.debug(f"Continuing with acting agents. Current iteration: {len(acting_messages)}/{max_iter}")
    return True

def main():
    logger.info("Starting story generation workflow")
    # Create the graph
    workflow = StateGraph(AgentState)
    logger.info("Created state graph")
    
    # Add nodes for each agent
    for agent_id in AGENTS:
        if agent_id not in ["story_controller", "summarizer"]:
            workflow.add_node(agent_id, create_agent(agent_id))
            logger.debug(f"Added node for agent: {agent_id}")
    
    # Add story controller and summarizer nodes
    workflow.add_node("story_controller", create_story_controller())
    workflow.add_node("summarizer", create_summarizer())
    logger.info("Added all nodes to workflow")
    
    # Set the entry point
    workflow.set_entry_point("story_controller")
    logger.debug("Set story_controller as entry point")
    
    # Add conditional edges for each acting agent
    for agent_id in AGENTS:
        if agent_id not in ["story_controller", "summarizer"]:
            workflow.add_conditional_edges(
                agent_id,
                should_continue,
                {
                    True: "story_controller",  # Continue with acting agents
                    False: "summarizer"        # Go to summarizer when max iterations reached
                }
            )
            logger.debug(f"Added conditional edges for agent: {agent_id}")
    
    # Add edge from story controller to agents
    workflow.add_conditional_edges(
        "story_controller",
        lambda x: x["current_agent"],
        {agent_id: agent_id for agent_id in AGENTS if agent_id not in ["story_controller", "summarizer"]}
    )
    logger.debug("Added edges from story controller to agents")
    
    # Add edge from summarizer to end
    workflow.add_edge("summarizer", END)
    logger.debug("Added edge from summarizer to end")
    
    # Compile the workflow
    app = workflow.compile()
    logger.info("Workflow compiled successfully")
    
    # Initial state
    initial_state = {
        "messages": [],
        "current_agent": "story_controller",
        "context": "在王国、森林和山地部落的交界处，发现了一个神秘的魔法物品。三个势力的代表聚集在一起，讨论如何处理这个物品。",
        "world_state": "世界处于和平状态，但各方势力都在寻求增强自己的影响力。"
    }
    logger.info("Initial state created")
    
    # Run the workflow
    logger.info("Starting workflow execution")
    result = app.invoke(initial_state)
    logger.info("Workflow execution completed")
    
    # Print the final story
    logger.info("Printing final story")
    for message in result["messages"]:
        if "=== The Chronicler's Tale ===" in message:
            print("\n" + message)
        else:
            print(message)
    logger.info("Story generation completed")

if __name__ == "__main__":
    main()
