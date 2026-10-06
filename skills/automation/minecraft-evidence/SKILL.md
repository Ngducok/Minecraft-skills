---
name: minecraft-evidence
description: "Verify Minecraft APIs, formats, mechanics and tool availability; avoid fabricated symbols, citations, compatibility and test results."
---

# Evidence and hallucination prevention

Record the claim that matters, its target version/platform and the evidence needed before implementing or advising. This reduces unsupported claims; it does not guarantee zero model errors.

- For an API symbol, inspect pinned dependency source/Javadocs/signature or compile a minimal use. Search snippets and a similarly named method on another platform are insufficient.
- For formats, inspect target assets/spec/reader and perform readback where appropriate. Do not invent pack versions, NBT packing constants or undocumented flags.
- For client behavior, use an actual matching client or label it unverified. A screenshot, compile pass or mock test proves only its own evidence level.
- Open relevant primary sources before citing them. Distinguish inspected facts, inferred design choices, hypotheses and unavailable evidence. If docs conflict, verify implementation/runtime instead of choosing convenient wording.
- Discover tools/capabilities before naming actions. Never claim Browser, subagents, a running server or screenshots were used when unavailable.
- Stop repeating an unsupported assumption; find a narrow probe or explicitly state the limitation. Keep requested version and scope intact rather than substituting a newer API.

## Verification

Audit material claims against artifacts or opened sources. Include commands/results for performed checks and label skipped runtime/client checks accurately.

## Example request

An answer proposes an undocumented Dialog callback method; verify its signature and a minimal compile before writing feature code.

## Focused reference

Read [references/evidence-cases.md](references/evidence-cases.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
