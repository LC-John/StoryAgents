#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
StoryAgents - A multi-agent story generation system
Main entry point for the story generation workflow.
"""

import os
import logging
import argparse
from typing import Dict, Any
import openai
from langgraph.graph import StateGraph, END
from StoryAgent.agents import ActorAgent, ControllerAgent, WriterAgent, AgentState
from StoryAgent.config import WorldInfo, ActorInfo
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
logger.info("Environment variables loaded")

# Configure OpenAI client
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.base_url = "https://api.deepseek.com/"
logger.info("OpenAI client configured with DeepSeek API")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='StoryAgents - A multi-agent story generation system')
    parser.add_argument('--actors-dir', 
                      default="StoryAgent/config/actor_cfg",
                      help='Directory containing actor configuration files')
    parser.add_argument('--world-config',
                      default="StoryAgent/config/world_cfg.json",
                      help='Path to world configuration file')
    parser.add_argument('--max-iterations',
                      type=int,
                      default=20,
                      help='Maximum number of iterations for actor interactions')
    parser.add_argument('--language',
                      default="English",
                      help='Language for story generation (default: English)')
    parser.add_argument('--model',
                      default="deepseek-chat",
                      help='LLM model to use for all agents (default: deepseek-chat)')
    return parser.parse_args()

def should_continue(state: AgentState, writer_id: str, max_iter: int = 3) -> bool:
    """Determine if the conversation should continue."""
    # Count only the messages from acting agents (excluding the writer's message)
    acting_messages = [msg for msg in state["messages"] if writer_id != msg[0]]
    
    # If we've already written the story, end the workflow
    if any(writer_id == msg[0] for msg in state["messages"]):
        logger.info("Story has been written, ending workflow")
        return False
    
    # If we've reached max iterations, go to writer
    if len(acting_messages) >= max_iter:
        logger.info(f"Reached max iterations ({max_iter}), proceeding to writer")
        return False
    
    # Otherwise, continue with acting agents
    logger.info(f"Continuing with acting agents. Current iteration: {len(acting_messages)}/{max_iter}")
    return True

def create_workflow(actors_dir: str, max_iter: int, lang: str, model: str) -> StateGraph:
    """Create the story generation workflow."""
    logger.info("Starting story generation workflow")
    
    # Get actor configurations
    actor_files = [f for f in os.listdir(actors_dir) if f.endswith('.json')]
    actor_ids = [f[:-5] for f in actor_files]  # Remove .json extension
    logger.info(f"Found {len(actor_ids)} actors: {', '.join(actor_ids)}")
    
    # Create the graph
    workflow = StateGraph(AgentState)
    logger.info("Created state graph")
    
    # Add nodes for each agent
    for actor_id in actor_ids:
        actor_info = ActorInfo.from_file(os.path.join(actors_dir, f"{actor_id}.json"))
        workflow.add_node(actor_id, ActorAgent(actor_id, actor_info, model=model))
        logger.debug(f"Added node for actor: {actor_id}")
    
    # Add controller and writer nodes
    workflow.add_node("controller", ControllerAgent(model=model))
    writer = WriterAgent(lang=lang, model=model)
    writer_id = writer.writer_id
    workflow.add_node("writer", writer)
    logger.info(f"Added all nodes to workflow with model: {model}")
    
    # Set the entry point
    workflow.set_entry_point("controller")
    logger.debug("Set controller as entry point")
    
    # Add conditional edges for each actor
    for actor_id in actor_ids:
        workflow.add_conditional_edges(
            actor_id,
            lambda state, writer_id=writer_id, max_iter=max_iter: should_continue(state, writer_id, max_iter),
            {
                True: "controller",  # Continue with acting agents
                False: "writer"      # Go to writer when max iterations reached
            }
        )
        logger.debug(f"Added conditional edges for actor: {actor_id}")
    
    # Add edge from controller to actors
    workflow.add_conditional_edges(
        "controller",
        lambda x: x["current_actor"],
        {actor_id: actor_id for actor_id in actor_ids}
    )
    logger.debug("Added edges from controller to actors")
    
    # Add edge from writer to end
    workflow.add_edge("writer", END)
    logger.debug("Added edge from writer to end")
    
    return workflow

def main():
    """Main entry point for the story generation system."""
    # Parse command line arguments
    args = parse_args()
    
    # Create workflow
    workflow = create_workflow(args.actors_dir, args.max_iterations, args.language, args.model)
    
    # Initialize state
    actor_ids = [f[:-5] for f in os.listdir(args.actors_dir) if f.endswith('.json')]
    initial_state = AgentState(
        messages=[],
        actors={actor_id: ActorInfo.from_file(os.path.join(args.actors_dir, f"{actor_id}.json")) 
               for actor_id in actor_ids},
        current_actor="controller",
        world_state=WorldInfo.from_file(args.world_config)
    )
    
    # Compile and run the workflow
    app = workflow.compile()
    logger.info("Workflow compiled successfully")
    
    # Run the workflow
    logger.info("Starting workflow execution")
    result = app.invoke(
        initial_state,
        config={"recursion_limit": args.max_iterations * 10}
    )
    logger.info("Workflow execution completed")

    # logger.info("All messages:\n\n" + "\n".join(f"### {sender}'s Round\n{content}\n" for sender, content in result["messages"]))

if __name__ == "__main__":
    main()
