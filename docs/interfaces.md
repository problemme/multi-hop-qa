# Proposed shared interfaces

Agree on these contracts before implementation.

retrieve(query: str, top_k: int = 5) -> list[Passage]
generate(question: str, accepted_history: list[Step], passages: list[Passage]) -> Step
verify(question: str, accepted_history: list[Step], candidate: Step, passages: list[Passage]) -> Verdict

Passage: passage_id, document_id, text, retrieval_score.
Step: subquestion, query, answer, passage_ids.
Verdict: status (supported / contradicted / insufficient_evidence), feedback.
Run: question_id, method, steps, final_answer, abstained, input_tokens,
output_tokens, retrieval_calls, model_revisions, code_commit, config.

Gold labels live in the evaluation dataset, not Step or Passage.
Only accepted steps enter the history. Failed steps trigger at most one
query rewrite + retrieval + regeneration + verification attempt.
If still unsupported, abstain. Stop after at most six proposed hops.
Score abstentions as incorrect in final-answer metrics.
Annotated-subquestion diagnostics are separate from autonomous end-to-end runs.
