# Contributing

Add narrowly scoped documentation at skills/<category>/<minecraft-name>/. Use lowercase hyphen names matching the directory. Keep SKILL.md concise, with name and quoted description frontmatter. Put scope in contract.json, evidence in REFERENCE.md, detailed references beside the skill, and request/scenario documents under examples/.

Provide actionable platform-specific guidance without imposing a game genre or provider. Unknown versions/builds/toolchains remain unresolved. Preserve instruction authority and authorized scope.

For a new fact, record its primary source, URL, inspection date and limitations in knowledge/sources.json. Matrix entries need exact releases and independently sourced formats/platform requirements. Claims of compile/runtime/client success require reproducible evidence for that exact target. A source link alone does not prove an API signature.

Before submitting, review names/frontmatter, contracts against schemas, source IDs, local links and catalog.json consistency. JSON/YAML parsing and other checks may use available tools outside this repository; no validator, package installation or CI is required by this docs-only library.

For scenario review, give an authorized agent the prompt, relevant skill and raw artifacts. Record host/model, exact targets, output, actual checks and unresolved facts. Fabricated symbols or test results fail review. Do not label scenario documents as passed agent tests.

Do not add tool implementations, executable examples, workflows, generated binaries, worlds, tokens or personal paths. Code snippets inside explanatory documents are allowed when needed to clarify instructions.

PR descriptions should state outcome, scope, sources and performed checks. Preserve contributor changes and remote history.
