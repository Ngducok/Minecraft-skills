# Datapack smoke example

Target: Java 1.21.11, data format 94.1. Copy this folder into a disposable world's datapacks directory, run `/reload`, inspect errors and `/datapack list`, then `/function agentcheck:load` with a player connected.

The load tag is under `tags/function` and functions under `function`, not legacy plural directories. Static tests inspect paths and function references; they do not execute Minecraft's command parser. Do not claim in-game load success without matching server logs.
