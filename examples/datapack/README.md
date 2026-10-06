# Datapack walkthrough

Example target: Java 1.21.11, data format 94.1. No runnable datapack is included.

For that exact target, document min_format/max_format as [94, 1]. A load tag belongs under data/minecraft/tags/function/load.json and its function under data/<namespace>/function/<name>.mcfunction; verify paths against the requested release rather than copying legacy plural directories.

Generate files in the user's project. In a disposable matching world, inspect reload logs, enabled datapacks and function execution with a player connected. JSON parsing alone does not establish Minecraft command or registry validity.
