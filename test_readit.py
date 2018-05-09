import pytest
from click.testing import CliRunner
from readit import cli as c


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


# Testing --version option
def test_version(runner):
    result = runner.invoke(c.main, ['--version'])
    assert not result.exception
    assert result.exit_code == 0
    expected = "readit v0.2\n"
    assert result.output == expected


# Testing -V option
def test_by_version(runner):
    result = runner.invoke(c.main, ['-V'])
    assert not result.exception
    assert result.exit_code == 0
    expected = "readit v0.2\n"
    assert result.output == expected


# Testing --help option
def test_help_option(runner):
    """testing the help of readit"""
    result = runner.invoke(c.main, ['--help'])
    assert not result.exception
    assert result.exit_code == 0
    expected_output = ("Usage: main [OPTIONS] [INSERT]...\n"
                       "\n"
                       "  Readit - Command-line bookmark manager tool."
                       "\n\n"
                       "Options:\n"
                       "  -a, --add TEXT...       Add URLs with space-separated\n"
                       "  -t, --tag TEXT...       Add Tag with space-separated URL\n"
                       "  -d, --delete TEXT       Remove a URL of particular ID\n"
                       "  -c, --clear TEXT...     Clear bookmarks\n"
                       "  -u, --update TEXT...    Update a URL for specific ID\n"
                       "  -s, --search TEXT       Search all bookmarks by Tag\n"
                       "  -v, --view TEXT...      Show bookmarks\n"
                       "  -o, --openurl TEXT      Open URL in Browser\n"
                       "  -V, --version           Check latest version\n"
                       "  -e, --export TEXT...    Export URLs in csv file\n"
                       "  -tl, --taglist TEXT...  Show all Tags\n" 
                       "  --help                  Show this message and exit.\n")
    assert result.output == expected_output
