# Host adapters

Canonical skill files are provider-neutral. No adapter installs globally or alters model/provider settings. Explicitly load the router and relevant skills when host discovery is unavailable. Native loading depends on installed host version; this repository does not certify every host.

Flatten selected skill folders into the documented project skill directory, preserving contract, references, examples and tests. REFERENCE.md links to shared knowledge must be adjusted or point to the original checkout. Prefer symlinks to original skill folders where supported. Do not silently replace existing skills with matching names. Restart/reload the host only when its documentation requires it.

An agent without native skills can read catalog.json, selected SKILL.md, contract.json and REFERENCE.md. This also works for Aider/OpenCode/custom agents without claiming their auto-discovery behavior.
