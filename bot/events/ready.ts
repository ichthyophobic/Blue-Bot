import { Events, Client, ActivityType, PresenceUpdateStatus } from "discord.js";

export default {
	name: Events.ClientReady,
	once: true,
	execute(client: Client) {
		console.log(`Logged in as ${client.user?.tag}`);
		client.user?.setPresence({
			activities: [{
				name: `Open-Source`,
				type: ActivityType.Watching
			}],
			status: PresenceUpdateStatus.Online,
		});
	}
};
