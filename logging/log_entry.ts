import { appendFile } from "fs/promises";

export class LogEntry {

	private logFile: string;

	constructor(logFile: string) {
		this.logFile = logFile
	}

	private async log(level: 'INFO' | 'ERROR' | 'CRITICAL' | 'DEBUG', message: string) {
		const entry = `[${new Date().toUTCString()}] [${level}] ${message}`;
		try {
			await appendFile(this.logFile, `${entry}\n`);
		} catch (err) {
			console.error('[Log Entry] ERROR', err);
		}
	}

	async info(message: string): Promise<void> {
		await this.log('INFO', message);
	}

	async debug(message: string): Promise<void> {
		await this.log('DEBUG', message);
	}

	async error(message: string): Promise<void> {
		await this.log('ERROR', message);
	}

	async critical(message: string): Promise<void> {
		await this.log('CRITICAL', message);
	}
}
