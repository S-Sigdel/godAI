# Group Discussion LLM Wrapper

A **Python-based abstraction layer** for orchestrating group-style discussions between multiple Large Language Models (LLMs). Designed to simulate collaborative AI conversations, debate resolution, and consensus-building across different model providers.

---

## 🎯 Purpose
Facilitate human-like group discussions between AI models (e.g., GPT-4, Claude, PaLM, Llama 2) by:
- Managing input/output formatting across providers
- Handling API/auth differences
- Aggregating responses into a unified discussion thread
- Implementing debate rules/consistency checks

---

## 🔧 Key Features
1. **Multi-Model Mediation**
   - Simultaneously connect to OpenAI, Anthropic, Hugging Face, and local models
   - Auto-retry failed API calls with provider fallback

2. **Discussion Orchestration**
   - Role assignment (e.g., "Devil's Advocate", "Moderator")
   - Turn-based conversation flow
   - Conflict detection between model responses

3. **Unified Output**
   - Standardized JSON/XML discussion transcripts
   - Summary generation ("The group concluded that...")
   - Sentiment/agreement analysis across responses

---

## 🤖 Why Python?
- **Rapid Prototyping**: Quickly test discussion workflows without compilation
- **API Flexibility**: Native support for REST (OpenAI), gRPC (Vertex AI), Websockets (Claude)
- **Data Wrangling**: Built-in tools for parsing JSON/XML responses across providers
- **Async Scaling**: Parallelize model queries with `asyncio`/`aiohttp`

---

## 🛠️ Implementation Approach
1. **Provider Adapters**
   - Abstract API-specific logic (e.g., OpenAI's `messages` vs Claude's `prompt`)
   - Normalize temperature/top_p parameters across models

