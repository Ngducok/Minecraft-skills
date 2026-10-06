---
name: minecraft-schematics
description: "Generate, inspect or convert .litematic, .schem and vanilla structure NBT files and verify their imported blocks/entities."
---

# Litematic, Sponge schematics and structures

Identify the exact format and target data version before writing bytes. A renamed ZIP/NBT file is not a format conversion; .litematic, Sponge .schem and structure .nbt have distinct schemas.

- Prefer an installed format library or author implementation over a new serializer. Read the exact target branch/spec for palette packing, coordinates and version fields; do not guess bit order or minimum bits.
- Preserve origin, signed region sizes, block-state properties, block entities and optional entities. Conversions can be lossy; state omitted features instead of silently dropping them.
- Use gzip/NBT handling with explicit limits and validate dimensions, palette indexes and data length. Test arrays crossing machine-word boundaries, not only tiny two-block fixtures.
- For WorldEdit, detect supported format and close readers/EditSession. Apply transforms before paste and account for clipboard origin; decide whether air replaces existing blocks.
- Read the exported artifact independently and compare non-air counts, bounds and chest contents. Import into the actual target tool; a Python preview does not prove Litematica/WorldEdit accepts it.

## Verification

Round-trip mixed states, containers, negative regions and a palette large enough to change bit width. Inspect the imported world at known coordinates and confirm DataVersion handling.

## Example request

A generated starter .litematic imports as empty; validate its schema, palette and packed state array.

## Focused reference

Read [references/schematic-roundtrip.md](references/schematic-roundtrip.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Sponge schematic v3 specification](https://github.com/SpongePowered/Schematic-Specification/blob/master/versions/schematic-3.md)
- [Litematica author repository](https://github.com/maruohon/litematica)
- [WorldEdit clipboard and schematic API](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/)
