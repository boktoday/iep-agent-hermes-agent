# Choosing a local model

The plan folder holds the most personal documents a family keeps about a child. Running IEP Agent on a local model keeps every word on your machine: no key, no bill, no data leaving the house.

**First stop: [canirun.ai](https://canirun.ai).** It reads your GPU or Mac straight from the browser, ranks the open models that fit your machine, and hands you the exact Ollama or LM Studio command to run the one you choose. No account, no install.

Two more worth knowing:

- [localllm-advisor.com](https://localllm-advisor.com) works both directions: best models for your hardware, or best hardware for a model you have your eye on. Fully client-side and private.
- [localllm.run](https://localllm.run) walks you through goal, hardware, model and setup in order, with guides for agent use.

## What this work asks of a model

The agent reads the plan, writes notes and drafts documents. That puts three demands on a local model:

1. **Instruction following.** The About Me writing rules (strengths first, no blame, the dignity test) only hold if the model follows instructions.
2. **Tool calling.** The model must support function calling, or the agent cannot read and write the shared folder.
3. **Enough context.** The profile plus a report can be long. Look for 32k context or more.

## The tiers

| Your machine | Start with (Ollama tag) | Also good |
|---|---|---|
| Modest laptop, 8 to 16 GB RAM, no dedicated GPU | `qwen3:8b` | `llama3.2:3b` on 8 GB machines |
| Capable machine, 16 to 32 GB RAM or 8 to 12 GB VRAM | `qwen3:14b` | `phi4:14b` |
| Strong machine, 32 GB+ RAM or 16 to 24 GB VRAM | `gpt-oss:20b` | `qwen3:30b-a3b` |
| Workstation, 64 GB+ RAM or 24 GB+ VRAM | `llama3.3:70b` | `gpt-oss:120b` |

Every tag runs in both Ollama and LM Studio. Trust the checkers on memory, not the parameter count.

## Getting one running

1. Install [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai) and pull a tag from the table.
2. Point Hermes at it: Ollama at `http://localhost:11434/v1`, LM Studio at `http://localhost:1234/v1` (see the commented block in `config.yaml`).
3. Try it on one job first: a note capture, then a Meeting Prep. Hermes can run each scheduled job on its own model.

## Which jobs suit a local model

- **Great fit, and the place to start: the repetitive work.** Cron jobs, the weekly note prompt, the meeting countdown, note capture. Small, frequent and the same every day, which is exactly what a local model is for.
- **Better on a bigger model:** drafting a long advocacy letter or processing a whole assessment report. A frontier model reached for occasionally is the pragmatic mix.
- **The all-local setup:** a capable machine plus a good local model means the plan folder never touches the internet at all.
