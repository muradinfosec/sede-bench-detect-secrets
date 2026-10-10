import pytest

from detect_secrets.plugins.npm import NpmDetector


class TestNpmDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [



            ('//registry.npmjs.org/:_authToken=npm_xxxxxxxxxxx', True),




            ('foo', False),
            ('//registry.npmjs.org/:_authToken=${NPM_TOKEN}', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = NpmDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)
        assert len(output) == int(should_flag)
