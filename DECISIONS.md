# Decision Log

## D-001 — Start with AI-driven biological discovery

**Decision:** Begin in biology, with aging as the long-term mission.

**Reason:** It has very high personal importance and civilizational impact, while
AI and public biological data provide an accessible way to make contact with the
real work before needing a laboratory.

## D-002 — Start with perturbation prediction

**Decision:** Use cellular perturbation prediction as the first technical wedge.

**Reason:** It exercises the core discovery loop: measure a system, intervene,
predict the response, compare with evidence, and update the model. This is more
causal and useful than merely predicting chronological age.

## D-003 — Use a reproduction before proposing a new model

**Decision:** Begin with simple baselines and reproduce an existing model before
designing a novel architecture.

**Reason:** This exposes data limitations and evaluation mistakes early and gives
future novelty a trustworthy point of comparison.

## D-004 — Keep strategy and execution separate

**Decision:** Keep the `future-we-want-to-build` documents as strategic context
and `ai-bio-discovery` as the active technical workspace.

**Reason:** This prevents philosophical exploration from obscuring the next
testable action.

## D-005 — Delay environment installation until the OS is known

**Decision:** Create the file structure now, but do not select or install Python,
Git, or GPU tooling yet.

**Reason:** Operating-system-specific instructions reduce conflicting Python
installations and PATH problems for a beginner.

## D-006 — Use the browser workspace first

**Decision:** Run initial code in the managed browser workspace instead of
installing a development stack directly on the user's Mac.

**Reason:** The browser workspace already provides isolated Linux, Python 3.12,
Git, and uv. It has no dedicated GPU, but a GPU is unnecessary for inspecting
data and building simple baselines. A separate GPU environment can be introduced
only when a published-model reproduction demonstrably requires it.

## D-007 — Keep the technical repository public

**Decision:** Publish the active technical workspace as a public GitHub
repository.

**Reason:** Public work makes the learning process, methods, assumptions, and
eventual results inspectable by researchers and potential collaborators. Raw or
large datasets, credentials, private health information, and local environment
files remain excluded from version control.

## D-008 — Make the repository the continuity system

**Decision:** Use `CURRENT_STATE.md`, the roadmap, decision log, experiment log,
and active experiment specification as the authoritative handoff between chats.

**Reason:** Project memory is helpful but not perfectly inspectable or guaranteed
to contain every implementation detail. A short, version-controlled state file
makes work recoverable by a future chat, collaborator, or tool.
