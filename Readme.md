
<div align="center">

</a>

</div>

<br/>

<p align="center" style="max-width:750px;">
A multi-agent AI research system that automates the research workflow by searching the web,
retrieving relevant information, generating structured reports, and critically evaluating the
final output.
</p>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:2563EB,100:0F172A&height=2&width=760" />
</div>

<br/>

## What It Does

The **Multi-Agent Research System** transforms a simple research topic into a structured and critically reviewed research report.

Instead of manually searching multiple websites, reading articles, collecting information, and reviewing the final report, the system distributes these responsibilities across specialized AI agents and chains.

<br/>

## Features

### Multi-Agent Research Workflow

Specialized agents handle different stages of the research process.

- **Web Search** — Uses Tavily to discover relevant information and web resources.
- **Content Extraction** — Retrieves and processes content from relevant web pages.
- **Automated Report Generation** — Converts collected research into a structured research report.
- **AI-Powered Criticism** — Reviews the generated report and identifies strengths and areas for improvement.

### Structured Output

Reports contain:

- Introduction
- Key Findings
- Conclusion
- Sources

### Streamlit Interface

Provides an interactive interface for running the research pipeline.

### Hugging Face LLM Integration

Uses Hugging Face's model infrastructure through an OpenAI-compatible API interface.

### Environment-Based API Configuration

API credentials are loaded securely using `.env`.

<br/>

## Architecture

The system follows a sequential multi-agent research architecture.

```text
                         ┌───────────────────┐
                         │    User Topic     │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Search Agent    │
                         │                   │
                         │ Tavily Web Search │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Reader Agent    │
                         │                   │
                         │ Web Scraping &    │
                         │ Content Extraction│
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Writer Chain    │
                         │                   │
                         │ Research Report   │
                         │ Generation        │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Critic Chain    │
                         │                   │
                         │ Quality Review    │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Final Output    │
                         └───────────────────┘
```

### Core Components

| Component     | Responsibility                             |
| ------------- | ------------------------------------------ |
| Search Agent  | Searches the web for relevant information  |
| Reader Agent  | Extracts useful content from web resources |
| Writer Chain  | Generates a structured research report     |
| Critic Chain  | Reviews and evaluates the generated report |
| Streamlit     | Provides the user interface                |
| Hugging Face  | Provides the LLM inference layer           |
| Tavily        | Provides web search capabilities           |
| BeautifulSoup | Supports web content extraction            |
| Requests      | Handles HTTP requests                      |

<br/>

## How It Works

### 01 · Search Agent

The Search Agent receives the user's research topic and uses Tavily to discover relevant information and sources from the web.

```text
Research Topic
      ↓
Search Agent
      ↓
Tavily Web Search
      ↓
Relevant Information & Sources
```

The agent is responsible for finding useful resources that can be passed to the next stage of the pipeline.

### 02 · Reader Agent

The Reader Agent processes relevant web resources and extracts useful content for deeper analysis.

```text
Relevant URLs
      ↓
Reader Agent
      ↓
Web Scraper
      ↓
Extracted Content
```

The reader stage uses web scraping utilities to retrieve information from selected resources.

### 03 · Writer Chain

The Writer Chain transforms the gathered research into a structured and professional research report.

```text
Research Data
      ↓
Writer Chain
      ↓
Structured Research Report
```

The generated report contains:

- Introduction
- Key Findings
- Conclusion
- Sources

### 04 · Critic Chain

The Critic Chain evaluates the generated report for quality, completeness, and potential weaknesses.

```text
Generated Report
      ↓
Critic Chain
      ↓
Quality Evaluation
```

The critic provides:

- Score
- Strengths
- Areas to Improve
- One-line Verdict

This final evaluation acts as a quality-control layer, helping identify weaknesses in the generated research before the workflow is considered complete.

<br/>

## Tech Stack

<div align="center">
