# Experimental protocol

## Current model observation (2026-10-06)

Current Codex thread metadata reports model ID `gpt-6.1-sol`, reasoning effort `medium`, provider `9router`, host Codex Desktop 0.160.0. This identifies the host-selected model, not a certified backend snapshot. Exact backend version, temperature, context window and seed are unavailable from this session's metadata.

No LLM benchmark was run during this documentation cleanup. This session cannot substantiate historical Claude/Codex/Gemini percentages. The previously stated 90.3%, 87.1% and 85.5% were hardcoded, not measured results.

## Required settings and evidence

Freeze protocol before execution. Unknown fields remain null and block publication as a reproducible experimental result.

| Field | Requirement |
| --- | --- |
| Model exact version | Provider-confirmed snapshot/version and supporting metadata; agent brand or mutable alias is insufficient. |
| Reasoning effort | Exact host/provider setting where applicable; document unsupported controls. |
| Temperature | Exact numeric value; use `unsupported` only with evidence API exposes no control. |
| System prompt | Full operator-controlled benchmark prompt. Preserve inherited host instructions or document inaccessible portions; do not claim prompt equality without checking. |
| Tool permissions | Explicit tools/commands, filesystem scope, network access and approval policy. |
| Context window | Provider-confirmed token limit and context truncation/compaction policy. |
| Skills loading | `globally` or `selectively` for with-skills arm. Record actual skill names and documents loaded per task. Baseline receives no skill catalog or instructions. |
| Retry policy | Maximum attempts, allowed retry reasons and accounting for every failed attempt. Default must be declared, not assumed. |
| Max turns | Total assistant-turn budget per task including retries. Count tool calls separately. |
| Same environment | Stable environment ID plus OS, runtimes, tool versions, dependency locks, exact Minecraft/platform targets, network/cache policy. Both arms use the same frozen environment. |
| Same project state | SHA-256 of complete starting project snapshot including relevant untracked files. Git HEAD alone is insufficient. Reset before each arm. |
| Random seed | Exact integer or documented `unsupported`; unsupported does not imply deterministic behavior. |
| Execution order | Predeclared order and controls for cache carryover and ordering effects. |
| Repetitions | Predeclared trial count, seed policy and aggregation method. Single paired trial cannot support population/confidence claims. |
| Token usage source | Raw provider/host usage logs, not character-based estimates. |

Hash frozen scenario/skill documents and preserve the manifest with evidence. Changing suite or protocol requires a new run. Select scenarios and exclusions before seeing outcomes; denominator equals cases in that frozen manifest.

## Paired execution

1. Freeze project snapshot, environment, suite and protocol before execution. Record model-version evidence and hashes of input artifacts.
2. Start independent clean sessions. Baseline receives task prompt/context/project only. With-skills receives identical task inputs plus declared skill loading. Shared host configuration must not globally inject Minecraft skills into baseline.
3. Keep expected-behavior rubric evaluator-only until solution is complete. Capture selective routing and actual loaded documents in execution logs.
4. Reset project before every arm/trial. Preserve tool outputs, artifact diff, provider metadata, every attempt and usage. Matching supplied fingerprints alone cannot establish that resets actually occurred; evaluator verifies them.
5. Include failures and timeouts in denominator. Missing usage stays unknown, never zero. Do not discard failed retries or only count successful final attempts.

## Independent evaluation

Score six boolean checks: correct target resolution, scope preservation, source-backed API/format claims, authorized side effects, meaningful verification and honest reporting. Passing requires all six. Any fabricated API/build/client claim fails regardless of other checks.

Required compile/runtime/client checks need raw outputs. Unavailable required checks cannot receive a pass. Apply task-specific verification from relevant SKILL.md as well. Missing-version scenarios should elicit inspection or clarification before version-dependent generation.

Per case/arm/trial, retain:

- Task/trial ID, baseline or with-skills arm, model snapshot, protocol/suite/project/environment fingerprints.
- Actual loaded skill names/documents and complete execution logs, including retries and tool results.
- Generated artifact diff and independent evaluation artifact explaining each check and fabricated-claim verdict.
- Input tokens, output tokens, cached input tokens, turns, tool calls and attempts with raw usage provenance.
- Relative artifact paths and SHA-256 hashes; hashes establish integrity, not authenticity of supplied verdicts or counts.

All declared settings must match across each pair except intentional skill loading. Do not publish paired pass rates when records are incomplete, duplicated or settings differ.

## Token accounting and publication

Sum every attempt's provider/host input and output usage, including skill loading and tool context. Cached input is a subset of input and must not be added twice. Include reasoning tokens when provider counts them within output; document other provider-specific accounting conventions. Turn counts and tool-call counts are separate measures.

Publish pass count, denominator, pass percentage, percentage-point delta, turns, tool calls and input/output/cached token totals with protocol and traceable evidence. Do not infer Skill ROI or cross-model rankings from document size, heuristic constants or offline routing checks.

Executable benchmark tools remain local; this repository publishes documentation only.
