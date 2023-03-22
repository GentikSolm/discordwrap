import re


# This method will be used by the mock to replace requests.get
def mock_request(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    base_url = f"https://discord.com/api/v9"
    if re.match(rf"{base_url}/channels/\d+/messages", args[0]):
        return MockResponse({"key1": "value1"}, 200)
    return MockResponse(None, 404)
