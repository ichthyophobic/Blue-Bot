#include <fstream>
#include <iostream>
#include <optional>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

using std::string;
using std::string_view;
using std::vector;
using std::move;
using std::optional;
using std::nullopt;
using std::ifstream;
using std::cout;
using std::cerr;
using std::getline;
using std::stoi;

class Message
{
	vector<string> m_attachments;
	vector<string> m_embeds;
	string m_content;
	string m_date;
	int m_reference;
	int m_user_id;
	int m_message_id;

public:

	Message(
		vector<string> attachments,
		vector<string> embeds,
		string content,
		string date,
		int user_id,
		int message_id,
		int reference
	)
		: m_attachments(attachments)
		, m_embeds(embeds)
		, m_content(content)
		, m_date(date)
		, m_user_id(user_id)
		, m_message_id(message_id)
		, m_reference(reference)
	{}

	Message(string error_msg)
	{
		m_date = "Message failed to parse";
		m_content = error_msg;
	}

	void is_valid()
	{
		if (m_content == "")
			throw "Empty message";

		if (m_user_id == 0)
			throw "Invalid user ID";

		if (m_message_id == 0)
			throw "Invalid message ID";
	}
};

// It reads if the line starts with the given key.
// If it matches, returns value of the key.
inline optional<string> get_value(string_view key, string_view line)
{
	auto key_length { key.length() };
	if (line.substr(0, key_length) == key)
	{
		string value {};
		for (auto i { key_length + 1 }; i < line.length(); ++i)
		{
			auto character { line[i] };
			if (character == '\n') continue;
			value.push_back(character);
		}
		return value;
	}
	return nullopt;
}

inline vector<Message> parser(string_view filename, bool strict = false)
{
	ifstream file(filename.data());
	string line;
	vector<Message> messages;

	vector<string> attachments;
	vector<string> embeds;
	string content {};
	string date {};
	int user_id {};
	int message_id {};
	int reference {};

	bool first_iteration { true };
	optional<string> search;
	if (file.is_open())
	{
		while (getline(file, line))
		{
			if (line == "message" && !first_iteration)
			{
				auto message = Message
				(
					attachments,
					embeds,
					content,
					date,
					user_id,
					message_id,
					reference
				);

				try {
					message.is_valid();
				} catch (const char* error) {
					message = Message(error);
				}

				messages.push_back(message);

				attachments.clear();
				embeds.clear();
				content = "";
				date = "";
				user_id = 0;
				message_id = 0;
				reference = 0;
			}

			search = get_value("reference", line);
			if (search)
			{
				reference = stoi(search.value());
				continue;
			}

			search = get_value("content", line);
			if (search)
			{
				content = search.value();
				continue;
			}

			search = get_value("date", line);
			if (search)
			{
				date = search.value();
				continue;
			}
		}

		file.close();
	}
	else
		cerr << "Failed to open file\n";
}
