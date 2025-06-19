#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langchain.chat_models import init_chat_model
from langchain.chat_models.base import BaseChatModel

supported_models = [
    "deepseek-chat",
    "deepseek-chat:deepseek-chat"
]

def get_llm(model: str = "deepseek-chat", temperature: float = 0.0) -> BaseChatModel:
    if model not in supported_models:
        raise ValueError(
            f"Unsupported LLM - {model}. Use the following LLMs: {', '.join(supported_models)}"
        )
    return init_chat_model(model=model, temperature=temperature)