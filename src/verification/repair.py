def verify_and_repair(question, result, verifier, rerun, max_repairs=1):
    """rerun(question, feedback) must return the controller's result dict."""
    attempts = []
    for _ in range(max_repairs + 1):
        verdict = verifier.verify(result["answer"], result["evidence"])
        attempts.append(verdict)
        if verdict["verdict"] == "SUPPORTED":
            break
        if len(attempts) <= max_repairs:
            result = rerun(question, verdict["reason"])
    return {**result, "verification": attempts, "repair_count": len(attempts) - 1}
