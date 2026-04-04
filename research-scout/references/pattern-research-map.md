# Pattern → Research Map

A curated lookup table: observed code pattern → research domain → suggested search terms.
Used by research-scout to quickly find the right search terms for any code pattern.

---

## AI Agent & LLM Patterns

| Code Pattern | Research Domain | Top Search Terms |
|---|---|---|
| Agent loop with tool calls | Agentic AI efficiency | "ReAct agent optimization", "LLM tool use latency", "agentic loop efficiency 2024" |
| Full context passed every LLM call | KV cache / prompt caching | "prompt caching LLM", "KV cache reuse inference", "context window compression" |
| Context growing unboundedly | Context compaction | "context compaction LLM", "sliding window attention", "MemGPT", "infinite context" |
| Repeated similar prompts | Semantic prompt caching | "semantic caching LLM", "prompt deduplication", "cache-augmented generation" |
| Multi-agent message passing | Multi-agent coordination | "multi-agent LLM coordination", "agent communication protocol 2024", "AutoGen", "CrewAI patterns" |
| Sequential tool calls (could be parallel) | Parallel tool use | "parallel function calling LLM", "concurrent tool execution agents" |
| Chain-of-thought prompting | CoT efficiency | "chain of thought compression", "implicit CoT", "thought distillation" |
| Self-consistency voting | Efficient sampling | "self-consistency efficient", "speculative decoding", "best-of-N alternatives" |
| RAG with fixed chunking | Advanced retrieval | "late chunking RAG", "ColBERT", "HyDE", "RAPTOR", "contextual retrieval" |
| Cosine similarity retrieval | Dense retrieval | "learned sparse retrieval", "SPLADE", "hybrid retrieval BM25 dense" |
| Embedding recomputed each time | Embedding caching | "embedding cache", "lazy embedding", "batch embedding optimization" |
| Hard-coded prompt templates | Automatic prompt optimization | "APE automatic prompt engineering", "DSPy", "meta-prompting 2024" |
| LLM as judge/evaluator | LLM evaluation | "LLM-as-judge calibration", "G-Eval", "FActScore", "eval reliability" |
| Fine-tuning with RLHF | Alignment alternatives | "DPO direct preference optimization", "GRPO", "RLAIF", "constitutional AI" |
| Hallucination in output | Factuality improvement | "retrieval augmented generation factuality", "self-RAG", "FLARE", "chain of verification" |
| Long document summarization | Hierarchical summarization | "RAPTOR hierarchical summarization", "MapReduce summarization", "recursive summarization" |
| Tool result fed back verbatim | Result compression | "tool result summarization", "observation compression agents" |
| Planning before acting | Planning in LLMs | "LLM planning survey 2024", "tree of thought", "MCTS LLM", "voyager" |
| Reflection / self-critique loop | Self-improvement | "reflexion LLM", "self-refine", "iterative self-correction" |

---

## Performance & Infrastructure

| Code Pattern | Research Domain | Top Search Terms |
|---|---|---|
| Synchronous API calls | Async batching | "async LLM inference", "batched API calls", "throughput optimization inference" |
| No request batching | Dynamic batching | "continuous batching vLLM", "Orca scheduling", "inference throughput" |
| Full model loaded per request | Model serving efficiency | "model serving optimization", "speculative decoding", "flash attention" |
| High latency per token | Inference acceleration | "speculative decoding", "Medusa heads", "draft model acceleration" |
| Redundant recomputation | Computation caching | "memoization LLM inference", "computation graph caching" |
| Memory pressure from large models | Quantization/pruning | "GPTQ quantization", "AWQ", "SparseGPT", "LoRA inference efficiency" |
| Sequential pipeline stages | Pipeline parallelism | "pipeline parallelism inference", "tensor parallelism", "DeepSpeed inference" |

---

## Data & State Management

| Code Pattern | Research Domain | Top Search Terms |
|---|---|---|
| State stored in memory only | Persistent agent state | "MemGPT", "long-term memory LLM agents", "episodic memory AI" |
| Flat key-value state | Structured agent memory | "cognitive architecture AI agents", "knowledge graph agent memory" |
| No state compression | State summarization | "conversation summarization", "state abstraction RL", "working memory compression" |
| Duplicate data in context | Context deduplication | "context deduplication", "redundancy removal prompts" |
| Manual schema validation | Structured output | "structured generation LLM", "outlines library", "instructor library", "JSON mode reliability" |

---

## Network / Ops Specific (Nokia / AI-Ops context)

| Code Pattern | Research Domain | Top Search Terms |
|---|---|---|
| Rule-based anomaly detection | ML anomaly detection | "network anomaly detection deep learning 2024", "LSTM network telemetry" |
| Threshold-based alerting | Adaptive thresholding | "adaptive threshold network monitoring", "online learning anomaly detection" |
| Root cause correlation by hand | Automated RCA | "automated root cause analysis network", "causal inference network faults" |
| gNMI polling fixed intervals | Adaptive telemetry | "adaptive telemetry streaming", "event-driven monitoring gNMI" |
| Log parsing with regex | Neural log parsing | "LogBERT", "drain log parsing", "neural log analysis 2024" |
| Single-model prediction | Ensemble forecasting | "ensemble network traffic prediction", "mixture of experts forecasting" |
| No uncertainty estimation | Bayesian forecasting | "uncertainty quantification network AI", "conformal prediction network ops" |
| Reactive remediation only | Proactive self-healing | "proactive network fault prediction", "digital twin network simulation" |

---

## Security & Compliance

| Code Pattern | Research Domain | Top Search Terms |
|---|---|---|
| No input sanitization for LLM | Prompt injection defense | "prompt injection defense 2024", "LLM input validation", "adversarial prompt detection" |
| Secrets in prompts | Secrets management AI | "LLM secrets leakage", "PII in context windows", "differential privacy LLM" |
| No output filtering | Output safety | "LLM output filtering", "constitutional AI output", "guardrails AI" |
| Black-box model decisions | Explainability | "LLM explainability", "attention visualization", "SHAP LLM", "EU AI Act compliance" |
| No audit trail | AI audit logging | "AI audit trail", "model decision logging", "explainable AI ops" |

---

## Key Venues to Search

- **arXiv cs.AI, cs.CL, cs.LG** — preprints, cutting edge
- **NeurIPS, ICML, ICLR** — top ML conferences
- **ACL, EMNLP, NAACL** — NLP-focused
- **SIGCOMM, INFOCOM, IEEE JSAC** — networking-focused
- **Anthropic, Google DeepMind, Meta AI, OpenAI blogs** — production engineering
- **Hugging Face blog** — implementation-focused
- **Nokia Bell Labs research** — domain-specific
