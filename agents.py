from langchain.agents import create_agent

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

from tools import web_search, scrape_url

from dotenv import load_dotenv
import os

load_dotenv()


# --------------------------------------------------
# Model configuration
# --------------------------------------------------

class MissingAPIKeyError(RuntimeError):
    """Raised when a provider key required by a pipeline stage is missing."""


def _required_api_key(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise MissingAPIKeyError(f"Set {name} in your project .env file.")
    return value


def _build_mistral_model() -> ChatMistralAI:
    return ChatMistralAI(
        model="ministral-3b-2512",
        api_key=_required_api_key("MISTRAL_API_KEY"),
        temperature=0.1,
        max_tokens=512,
        max_retries=2,
    )


def _build_groq_model() -> ChatGroq:
    return ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=_required_api_key("GROQ_API_KEY"),
        temperature=0.1,
        max_tokens=512,
    )


# --------------------------------------------------
# 1st Agent - Search Agent
# --------------------------------------------------

def build_search_agent():

    return create_agent(
        model=_build_mistral_model(),
        tools=[web_search]
    )


# --------------------------------------------------
# 2nd Agent - Reader Agent
# --------------------------------------------------

def build_reader_agent():

    return create_agent(
        model=_build_mistral_model(),
        tools=[scrape_url]
    )


# --------------------------------------------------
# Writer Chain
# --------------------------------------------------

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. "
        "Write clear, structured and insightful reports."
    ),

    (
        "human",
        """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:

{research}

Structure the report as:

- Introduction

- Key Findings (minimum 3 well-explained points)

- Conclusion

- Sources (list all URLs found in the research)

Be detailed, factual and professional."""
    ),
])

def build_writer_chain():
    return writer_prompt | _build_mistral_model() | StrOutputParser()


# --------------------------------------------------
# Critic Chain
# --------------------------------------------------

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a sharp and constructive research critic. "
        "Be honest and specific."
    ),

    (
        "human",
        """Review the research report below and evaluate it strictly.

Report:

{report}

Respond in this exact format:

Score: X/10

Strengths:

- ...

- ...

Areas to Improve:

- ...

- ...

One line verdict:

..."""
    ),
])

def build_critic_chain():
    return critic_prompt | _build_groq_model() | StrOutputParser()