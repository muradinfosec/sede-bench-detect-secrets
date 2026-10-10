import pytest

from detect_secrets.plugins.mailchimp import MailchimpDetector


class TestMailchimpKeyDetector:

    @pytest.mark.parametrize(
        'line,should_flag',
        [
            (

                True,
            ),
            (

                True,
            ),
            (
                '3ea4572956e2b381923ed34c31db76aa-2',
                False,
            ),
            (
                'aea462953eb192d38c31a433e76257db-al32',
                False,
            ),
            (

                False,
            ),
            (
                '3a5633e829d3c71-us2',
                False,
            ),
        ],
    )
    def test_analyze(self, line, should_flag):
        logic = MailchimpDetector()

        output = logic.analyze_line(filename='mock_filename', line=line)
        assert len(output) == (1 if should_flag else 0)
