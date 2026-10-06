# Contributing

Add a narrowly scoped skill at skills/<category>/<minecraft-name>/. Use lowercase hyphen names matching the directory; description explains when to use it. Keep SKILL.md concise with name and quoted description frontmatter. Put structured scope in contract.json, facts/sources in REFERENCE.md, detailed references beside the skill, a realistic request in examples/request.md and a behavioral scenario in tests/scenario.json.

Provide actionable platform-specific guidance, not generic summaries or copied manuals. Do not impose one genre or provider. Include boundaries where similar platform APIs differ. Unknown versions/builds/toolchains stay unresolved.

For a new fact, add its primary source ID, URL, inspection date and note to knowledge/sources.json. Version matrix additions need exact release, pack formats and independently sourced platform requirements. Test claims require evidence artifacts and validator support; v1 only permits documented matrix entries. A link existing is not proof of an API signature. Prefer pinned docs/source or a minimal compile probe.

Run:

```sh
python -m tools.cli index
python -m tools.cli validate
python -m tools.cli test
python -m tools.standards_check  # requires optional jsonschema + PyYAML, installed by CI
```

For Paper example changes, run `mvn -f examples/paper-plugin/pom.xml -B package` with Java 21 and Maven. For datapack/pack changes, load a disposable exact-version world/client and attach observed logs/screenshots when possible. Never commit worlds, Minecraft binaries, proprietary assets, tokens or personal paths.

Scenario files are not executed by unit tests. For agent evaluation, give an independent authorized agent the scenario, skill and raw artifacts; capture output and checks. Score using tests/AGENT-EVAL.md, record host/model and exact targets, and identify unperformed checks. Do not label static fixtures as LLM regression success.

PR description: problem/outcome, exact scope, sources, performed checks and limits. CI is mandatory structural verification, not universal platform certification. Preserve contributor changes and remote history. Use normal branches/PRs; no force-push requirement.
