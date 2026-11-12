# Multi-hop QA with Retrieval-Interleaved Reasoning

Course project: IRCoT and ReAct with per-hop verification and bounded repair.
This repository is a collaboration scaffold; model pipelines are not implemented yet.

## Team
| Owner | Module | Deliverable |
|---|---|---|
| Zhenghao Zhang | src/baselines | Qwen inference, IRCoT/ReAct controllers, step logs |
| Haosen Zhang | src/retrieval | Dataset preparation, deduplicated passages, BM25 top-5 |
| Xinyue Xia | src/verification | Gemma verification, verdict parsing, bounded repair |
| Shutong Lv | src/evaluation | Splits, scoring, cost tracking, error analysis |

## Experiment plan
Generator: Qwen/Qwen3.5-4B. Verifier: google/gemma-4-E2B-it.
Freeze model revisions/settings before experiments; no fine-tuning.
Datasets: human-verified MoreHopQA and MEQA. Index source passages only.
Never expose test gold answers/decompositions to either model.
One repair per hop, maximum six hops; unresolved failures abstain.
Compare IRCoT/ReAct with and without verification; include a matched-retrieval control.
Report EM, token F1, per-hop and all-hops-correct accuracy, tokens, retrieval calls.
Pilot: integrated 10-question smoke run, then 50 development questions.

## Collaboration
Work in a task branch; open a pull request into main and request one teammate review.
Do not commit directly to main after initialization. This is a team convention, not an enforced branch rule.
Keep PRs small; synchronize main before starting the next task.
See CONTRIBUTING.md and docs/interfaces.md.
Use individual Colab notebooks for development; use shared Drive for datasets and run artifacts.
GitHub shares code, not GPU memory or runtime state.
Never commit credentials, model weights, raw datasets, or large outputs.
