#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configuration package for the story generation system.
Exports agent configurations and world rules.
"""

from .agents import AGENTS
from .world_rules import WORLD_RULES

__all__ = ['AGENTS', 'WORLD_RULES'] 