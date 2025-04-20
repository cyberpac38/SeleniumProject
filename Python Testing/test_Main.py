from Main import get_weather


# noinspection Annotator
def test_get_weather():
    assert get_weather(21) == "hot"
