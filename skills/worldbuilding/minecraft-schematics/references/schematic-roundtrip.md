# Schematic interoperability check

Use before declaring a generated schematic usable in its target tool.

Litematica .litematic, Sponge .schem and vanilla structure .nbt have distinct schemas.
An extension change does not convert them. Confirm exact format version and reader;
the common Litematica extension is .litematic, despite informal misspellings.

Use the target format's maintained writer when available. For a custom serializer,
inspect its schema/author implementation for palette indexes, minimum bit widths,
word boundaries, signed region sizes, origin transforms and entity coordinates.
Do not guess whether packed values straddle longs. Include DataVersion and item
component encoding appropriate to the target release.

Create a tiny fixture with air, two distinguishable blocks, asymmetric dimensions,
negative offset/region geometry where supported and a chest containing distinct
items/counts. Add a boundary-sized palette fixture to exercise index packing.
Read it back independently, then open/paste it in the actual target tool.

Compare block count and coordinates, region bounds/origin, chest contents and block
entities. A screenshot of a solid island does not test inventories or orientation.
Check that saving/reloading preserves data. Report NBT parsing, independent readback
and real-tool loading as different verification levels.
