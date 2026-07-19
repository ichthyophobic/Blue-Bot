type LogLevel = 'INFO' | 'DEBUG' | 'ERROR' | 'WARN';

export class LogEntry {

	private timestamp: string;
	private level: LogLevel;
	private message: string;

	constructor(level: LogLevel, message: string) {
		this.level = level;
		this.message = message;
		this.timestamp = new Date().toUTCString();
	}

	to_str(): string {
		return `[${this.timestamp}] [${this.level}] ${this.message}`
	}

	logTime(): string { return this.timestamp }

	logLevel(): LogLevel { return this.level }

	logMessage(): string { return this.message }
}
