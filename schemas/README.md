# Contract schemas

These Draft 2020-12 JSON Schema documents describe skill contracts, project context and compatibility records. They are reference documents; this repository supplies no schema validator.

Canonical SKILL.md frontmatter uses name and JSON-quoted description, which is valid YAML. contract.json carries structured metadata. Names must match skill directory names; contributors may check documents with their host's available JSON/YAML tooling.

Empty supports.platforms means platform-neutral guidance, not universal binary compatibility. Empty verified_versions means no certified release. requires.java=null means resolve the target toolchain. Intended scope and verification evidence are separate.
