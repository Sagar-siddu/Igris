# IGRIS Architecture

## Overview

IGRIS is an orchestrator-based AI assistant that combines a Large Language Model (LLM), modular tools, and memory to process user inputs and perform actions.

The system follows a **separation of concerns**:

* Reasoning → handled by LLM
* Execution → handled by tools
* Context → handled by memory
* Coordination → handled by orchestrator

---

## Core Components

### 1. Interface Layer

* Command Line Interface (CLI)
* Accepts user input
* Displays responses

---

### 2. Orchestrator (`core/orchestrator.py`)

* Central control unit of IGRIS
* Responsibilities:

  * Receives user input
  * Fetches memory context
  * Calls Agent (LLM)
  * Parses LLM response
  * Executes tools if required
  * Returns final response

---

### 3. Agent (`core/agent.py`)

* Interfaces with Groq API (LLM)
* Responsibilities:

  * Maintains system prompt
  * Sends input + memory + tools to LLM
  * Receives structured JSON output
  * Returns parsed response

---

### 4. Memory (`memory/short_term.py`)

* Implements short-term memory using FIFO queue
* Stores recent conversation history (default: 10 messages)
* Provides context for LLM

---

### 5. Tools System (`tools/`)

#### Base Tool (`base_tool.py`)

* Abstract class defining:

  * `name`
  * `description`
  * `run()` method

#### System Tools (`system_tools.py`)

* OpenNotepadTool
* OpenGoogleTool
* OpenWebsiteTool

---

### 6. Configuration (`utils/config.py`)

* Loads environment variables using `python-dotenv`
* Stores:

  * `GROQ_API_KEY`
  * `MODEL_NAME`

---

## Execution Flow

1. User inputs command via CLI
2. Input is sent to Orchestrator
3. Orchestrator retrieves short-term memory
4. Agent is invoked with:

   * System prompt
   * Conversation history
   * Available tools
5. LLM returns JSON response:

   * Direct response OR tool call
6. Orchestrator parses JSON
7. If tool is requested:

   * Executes tool with arguments
8. Final response is printed to user
9. Interaction is stored in memory

---

## Tool Calling Format

```json
{
  "action": "tool_name" | "respond",
  "tool_input": {},
  "response": "message to user"
}
```

* `action`: determines execution path
* `tool_input`: parameters for tool
* `response`: user-facing output

---

## Design Philosophy

* IGRIS acts as an **orchestrator**, not a monolithic AI
* LLM is used only for:

  * reasoning
  * decision-making
* Tools handle real-world execution
* Memory provides context, not intelligence
* System prioritizes:

  * modularity
  * extensibility
  * controlled execution

---

## Extensibility

New features can be added by:

* Creating new tools (plug into tools/)
* Enhancing memory (long-term storage)
* Updating system prompt
* Expanding orchestrator logic

---

## Future Architecture Enhancements

* Long-term memory (database / vector store)
* Voice interface layer
* Permission & safety layer
* Async/background task execution
* Multi-agent coordination