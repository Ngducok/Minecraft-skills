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

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/)
- [Paper vanilla compatibility](https://docs.papermc.io/paper/vanilla/)
- [Litematica author repository](https://github.com/maruohon/litematica)
- [Official OpenAI AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
