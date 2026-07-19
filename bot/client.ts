import { Client, Collection, GatewayIntentBits, SlashCommandBuilder } from "discord.js";
import('fs');
import { config } from "dotenv";
import { readdirSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

config()

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const events_path = join(__dirname, 'events');
const commands_path = join(__dirname, 'commands');

const client = new Client({
	intents: [
		GatewayIntentBits.Guilds,
		GatewayIntentBits.GuildMessages,
		GatewayIntentBits.MessageContent,
		GatewayIntentBits.GuildModeration,
	],
});

// Loading event handles from events folder
async function load_evnets() {
	const event_files = readdirSync(events_path).
		filter(file => file.endsWith('.ts'));

	for (const file of event_files) {
		const { default: event } = await import(`${events_path}/${file}`);
		if (event.once) {
			client.once(event.name, (...args) => event.execute(...args));
		} else {
			client.on(event.name, (...args) => event.execute(...args));
		}
	}
}

// Loading slash commands from commands folder
const command_files = readdirSync(commands_path)
	.filter(file => file.endsWith('.ts'));

for (const file of command_files) {

}

load_evnets()
client.login(process.env.TOKEN);
