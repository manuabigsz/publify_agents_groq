#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from .crew import NovoBack

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(topic, content, social_network):
    """
    Run the crew with a topic and specific content.
    """
    inputs = {
        'topic': topic,
        'content': content,
        'social_network': social_network,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = NovoBack().crew().kickoff(inputs=inputs)
        return result  # agora retorna o conteúdo gerado
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
