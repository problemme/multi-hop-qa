# Team workflow

1. Clone this private repository using your own GitHub credentials.
2. Run git switch main and git pull --ff-only origin main.
3. Create a task branch (git switch -c xinyue/new-task), or use your initial branch.
4. Edit your module; coordinate interface changes with teammates.
5. Stage specific files, commit, and push your branch.
6. Open a PR to main; request another teammate's review before merging.
7. Pull updated main before creating a fresh branch for your next task.

Initial branches: zhenghao/baselines, haosen/retrieval, xinyue/verifier, shutong/evaluation.

Agree on docs/interfaces.md before integration. Each run must record commit SHA,
dataset/split IDs, model revisions, prompts, inference settings, and random seed.
Pin dependencies after the first working GPU pilot; requirements.txt is a starting list.

Store raw data, indexes and full run outputs in a shared Drive folder (team to create).
Use separate run directories; never overwrite another member's results.
Keep test gold labels outside generator/verifier inputs.
Private repository invitations require each teammate's GitHub username.
