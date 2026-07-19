import { spawn, ChildProcess } from "child_process";
import { LogEntry } from './types.ts';
import fs from "fs";

class BotManager {

	private uuid: ChildProcess | null = null;
	private running: boolean = false;

	startBot() {

		if (this.running) {
			throw "Bot has already started.";
		}

		const child: ChildProcess = spawn('node', ['bot/client.js']);
	}

	stopBot() {
		if (!this.running) {
			throw "Bot has already stopped.";
		}
	}
}
