#include <string_view>
#include <vector>

using std::string_view;
using std::vector;

struct Message
{
	string_view author;
	string_view content;
	string_view time;
	vector<string_view> attachments;

	Message(string_view author, string_view content,
			string_view time, vector<string_view> attachments)
		: author(author), content(content)
		, time(time), attachments(attachments)
	{}
};

class Json
{
	
};
