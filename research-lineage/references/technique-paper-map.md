# Technique → Paper Map

A curated lookup table: observed code technique → canonical paper → citation.
Used by research-lineage to quickly identify the paper behind any implementation.

---

## Transformer & Attention Mechanisms

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| Scaled dot-product attention | Attention Is All You Need | Vaswani et al., NeurIPS 2017 |
| Multi-head attention | Attention Is All You Need | Vaswani et al., NeurIPS 2017 |
| Sinusoidal positional encoding | Attention Is All You Need | Vaswani et al., NeurIPS 2017 |
| Rotary position embedding (RoPE) | RoFormer | Su et al., 2021 (arXiv:2104.09864) |
| ALiBi positional bias | Train Short Test Long | Press et al., ICLR 2022 |
| Flash attention kernel | FlashAttention | Dao et al., NeurIPS 2022 |
| Flash attention 2 | FlashAttention-2 | Dao, 2023 (arXiv:2307.08691) |
| Grouped query attention (GQA) | GQA: Training Generalized Multi-Query | Ainslie et al., EMNLP 2023 |
| Multi-query attention (MQA) | Fast Transformer Decoding | Shazeer, 2019 (arXiv:1911.02150) |
| Sliding window attention | Longformer | Beltagy et al., 2020 (arXiv:2004.05150) |
| KV cache | (standard inference optimization) | Various; see Transformer inference surveys |
| Mixture of Experts layer | Outrageously Large Neural Networks | Shazeer et al., ICLR 2017 |
| Switch Transformer routing | Switch Transformers | Fedus et al., JMLR 2022 |

---

## Training & Optimization

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| Adam optimizer | Adam: A Method for Stochastic Optimization | Kingma & Ba, ICLR 2015 |
| AdamW (decoupled weight decay) | Decoupled Weight Decay Regularization | Loshchilov & Hutter, ICLR 2019 |
| Cosine annealing LR schedule | SGDR: Stochastic Gradient Descent with Warm Restarts | Loshchilov & Hutter, ICLR 2017 |
| Gradient accumulation | (standard distributed training technique) | Various |
| LoRA adapter layers | LoRA: Low-Rank Adaptation of Large Language Models | Hu et al., ICLR 2022 |
| QLoRA | QLoRA: Efficient Finetuning of Quantized LLMs | Dettmers et al., NeurIPS 2023 |
| DPO loss function | Direct Preference Optimization | Rafailov et al., NeurIPS 2023 |
| GRPO | DeepSeekMath / Group Relative Policy Optimization | Shao et al., 2024 |
| PPO for RLHF | Proximal Policy Optimization | Schulman et al., 2017 (arXiv:1707.06347) |
| RLHF pipeline | Training Language Models to Follow Instructions with Human Feedback | Ouyang et al., NeurIPS 2022 (InstructGPT) |
| Label smoothing | Rethinking the Inception Architecture | Szegedy et al., CVPR 2016 |
| Dropout regularization | Dropout: A Simple Way to Prevent Neural Networks from Overfitting | Srivastava et al., JMLR 2014 |
| Layer normalization | Layer Normalization | Ba et al., 2016 (arXiv:1607.06450) |
| RMSNorm | Root Mean Square Layer Normalization | Zhang & Sennrich, NeurIPS 2019 |
| SwiGLU activation | GLU Variants Improve Transformer | Shazeer, 2020 (arXiv:2002.05202) |

---

## Retrieval & RAG

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| RAG pipeline (retrieve→augment→generate) | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al., NeurIPS 2020 |
| BM25 scoring | The Probabilistic Relevance Framework: BM25 and Beyond | Robertson & Zaragoza, 2009 |
| TF-IDF weighting | (multiple origins) | Sparck Jones 1972 (IDF), Salton 1975 (TF-IDF) |
| Dense passage retrieval (DPR) | Dense Passage Retrieval for Open-Domain QA | Karpukhin et al., EMNLP 2020 |
| ColBERT late interaction | ColBERT: Efficient and Effective Passage Search | Khattab & Zaharia, SIGIR 2020 |
| HyDE (hypothetical doc embedding) | Precise Zero-Shot Dense Retrieval without Relevance Labels | Gao et al., 2022 |
| RAPTOR (recursive abstractive processing) | RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval | Sarthi et al., ICLR 2024 |
| Self-RAG | Self-RAG: Learning to Retrieve, Generate, and Critique | Asai et al., ICLR 2024 |
| Cross-encoder reranking | (standard in information retrieval) | Nogueira & Cho, 2019 |
| SPLADE sparse retrieval | SPLADE: Sparse Lexical and Expansion Model | Formal et al., SIGIR 2021 |
| Reciprocal rank fusion (RRF) | Reciprocal Rank Fusion Outperforms Condorcet | Cormack et al., SIGIR 2009 |

---

## Agentic / Reasoning Patterns

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| ReAct (reason + act loop) | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al., ICLR 2023 |
| Chain-of-thought prompting | Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al., NeurIPS 2022 |
| Self-consistency sampling | Self-Consistency Improves Chain of Thought Reasoning | Wang et al., ICLR 2023 |
| Tree of Thoughts | Tree of Thoughts: Deliberate Problem Solving with LLMs | Yao et al., NeurIPS 2023 |
| Reflexion / self-critique loop | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al., NeurIPS 2023 |
| Tool-use with function calling | Toolformer | Schick et al., NeurIPS 2023 |
| Plan-and-execute agent | Plan-and-Solve Prompting | Wang et al., ACL 2023 |
| Multi-agent debate | Improving Factuality and Reasoning via Multiagent Debate | Du et al., 2023 |
| Constitutional AI output filtering | Constitutional AI: Harmlessness from AI Feedback | Bai et al., 2022 |
| Meta-prompting | Meta-Prompting: Enhancing LLMs with Expert-Level Prompts | Suzgun & Kalai, 2024 |

---

## Sequence Models (Pre-Transformer)

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| LSTM cell | Long Short-Term Memory | Hochreiter & Schmidhuber, Neural Computation 1997 |
| GRU cell | Learning Phrase Representations using RNN Encoder-Decoder | Cho et al., EMNLP 2014 |
| Bidirectional RNN / BiLSTM | Bidirectional Recurrent Neural Networks | Schuster & Paliwal, IEEE TSP 1997 |
| Seq2seq with attention | Neural Machine Translation by Jointly Learning to Align and Translate | Bahdanau et al., ICLR 2015 |
| Temporal Fusion Transformer | Temporal Fusion Transformers for Interpretable Multi-horizon Forecasting | Lim et al., IJF 2021 |
| PatchTST | A Time Series is Worth 64 Words | Nie et al., ICLR 2023 |

---

## Networking & Systems

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| Dijkstra shortest path | A Note on Two Problems in Connexion with Graphs | Dijkstra, 1959 |
| OSPF / IS-IS link-state routing | RFC 2328 (OSPF) / RFC 1195 (IS-IS) | Moy 1998 / Callon 1990 |
| MPLS label switching | RFC 3031 | Rosen et al., 2001 |
| Segment Routing (SR-MPLS) | RFC 8402 | Filsfils et al., 2018 |
| SRv6 | RFC 8986 | Filsfils et al., 2021 |
| EVPN | RFC 7432 | Sajassi et al., 2015 |
| gNMI streaming telemetry | gNMI specification | OpenConfig, 2017+ |
| YANG data modeling | RFC 7950 | Bjorklund, 2016 |
| TCP congestion control (Reno/CUBIC) | RFC 5681 / RFC 8312 | Various |
| Bloom filter | Space/Time Trade-offs in Hash Coding with Allowable Errors | Bloom, CACM 1970 |
| Consistent hashing | Consistent Hashing and Random Trees | Karger et al., STOC 1997 |
| Raft consensus | In Search of an Understandable Consensus Algorithm | Ongaro & Ousterhout, USENIX ATC 2014 |

---

## Anomaly Detection & AIOps

| Code Technique | Canonical Paper | Citation |
|---|---|---|
| Isolation Forest | Isolation Forest | Liu et al., ICDM 2008 |
| Autoencoder anomaly detection | (multiple origins) | Various; Sakurada & Yairi 2014 for time-series |
| DBSCAN clustering | A Density-Based Algorithm for Discovering Clusters | Ester et al., KDD 1996 |
| Drain log parser | Drain: An Online Log Parsing Approach | He et al., ICWS 2017 |
| LogBERT | LogBERT: Log Anomaly Detection via BERT | Guo et al., IJCNN 2021 |
| Conformal prediction | Algorithmic Learning in a Random World | Vovk et al., 2005 |

---

## Key Venues by Domain

- **ML/AI general:** NeurIPS, ICML, ICLR, AAAI, JMLR
- **NLP:** ACL, EMNLP, NAACL, TACL
- **Information retrieval:** SIGIR, WSDM, CIKM
- **Systems:** OSDI, SOSP, NSDI, USENIX ATC
- **Networking:** SIGCOMM, INFOCOM, CoNEXT, IEEE JSAC
- **Databases:** VLDB, SIGMOD
- **Security:** IEEE S&P, USENIX Security, CCS, NDSS
