# External agent evaluation

Unit tests execute tools, fixtures, routing and examples. They do not execute an LLM. Each skill tests/scenario.json is an evaluation input for an authorized independent agent or human review.

Supply scenario, skill instructions and only relevant raw project artifacts. Do not supply the desired verdict. Record host/model, exact Minecraft/platform/dependency versions, generated artifact diff, commands, outputs and unresolved checks.

Score 0/1 for each: correct target resolution; scope preservation; source-backed API/format claims; authorized side effects; meaningful verification; honest reporting. A fabricated API/build/client claim fails regardless of sum. Assess task-specific Verification in SKILL.md too. Example prompts with missing versions should elicit inspection or clarification before version-dependent generation.

Persist external-run results separately with provenance. No scenarios have been executed against an LLM as part of v1 offline verification. Do not report them as passed agent regressions. Future CI integration must specify execution permissions, budget and reproducible artifacts.
