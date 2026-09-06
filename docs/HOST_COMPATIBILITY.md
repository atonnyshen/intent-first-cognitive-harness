# Host compatibility

The Skill is a Markdown contract. Each host decides how to discover it and whether it can expose menus, structured output, tools, or recovery controls.

The minimum fallback is plain text: infer the goal, ask a material A/B/C question when needed, and continue from the user's answer. A host-specific adapter may add menus or structured state, but it must preserve the same fail-closed boundaries and report its own runtime evidence.
