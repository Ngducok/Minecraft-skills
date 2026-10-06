# Schema profile

Schemas are Draft 2020-12 documents. The offline stdlib validator implements only the keywords used here: type, enum, properties, required, additionalProperties=false, items, length/numeric bounds, pattern and uniqueItems. It rejects unknown keywords. It is not a general JSON Schema implementation.

CI additionally validates schemas and data with python-jsonschema. Extend both paths and negative tests when adding schema features. Canonical frontmatter deliberately uses only name and JSON-quoted description (valid YAML); contract.json carries structured metadata. Skill names match directory names.

Empty supports.platforms means platform-neutral guidance, not universal binary compatibility. Empty verified_versions means no certified releases. requires.java=null means resolve target toolchain. Intended scope and verification evidence are separate.
