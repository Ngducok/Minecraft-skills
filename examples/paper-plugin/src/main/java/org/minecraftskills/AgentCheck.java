package org.minecraftskills;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.plugin.java.JavaPlugin;

public final class AgentCheck extends JavaPlugin {
    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (!command.getName().equals("agentcheck")) return false;
        if (!sender.hasPermission("agentcheck.use")) return true;
        if (args.length != 0) return false;
        sender.sendMessage("Agent example active.");
        return true;
    }
}
