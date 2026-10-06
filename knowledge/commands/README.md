# Command evidence scope

Command parsing, permission predicates and execution context differ between Brigadier, Bukkit, Velocity and Bedrock. Inspect target command dispatcher/docs and test malformed arguments and authorization before mutations. A parse pass is not a runtime permission test.
