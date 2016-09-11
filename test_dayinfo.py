from errbot.backends.test import testbot  # noqa


class TestDayInfo(object):
    extra_plugin_dir = '.'

    def test_dayinfo_specific_day(self, testbot):  # noqa
        testbot.push_message('!dayinfo 1.1.2016')
        msg = 'Friday 01.01.2016, Day of the Establishment of the Slovak ' \
              'Republic'
        assert msg in testbot.pop_message()

        testbot.push_message('!dayinfo 5.6.2014')
        assert 'Thursday 05.06.2014, Nameday: Laura' in testbot.pop_message()

    def test_dayinfo_invalid_date(self, testbot):  # noqa
        testbot.push_message('!dayinfo 29.2.2015')
        assert 'Not a valid date' in testbot.pop_message()

    def test_nameday_specific_day(self, testbot):  # noqa
        testbot.push_message('!nameday 24.12.2016')
        assert 'Adam, Eva' in testbot.pop_message()

    def test_nameday_invalid_date(self, testbot):  # noqa
        testbot.push_message('!nameday 30.2.2015')
        assert 'Not a valid date' in testbot.pop_message()

        testbot.push_message('!nameday 10.5.20')
        assert 'Not a valid date' in testbot.pop_message()

    def test_nameday_noone(self, testbot):  # noqa
        testbot.push_message('!nameday 1.1.2015')
        assert "Noone's got nameday" in testbot.pop_message()
