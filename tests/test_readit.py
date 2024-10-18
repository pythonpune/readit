import pytest
from click.testing import CliRunner

from readit import cli as c


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


# Testing --version option
def test_version(runner):
    result = runner.invoke(c.main, ["--version"])
    assert not result.exception
    assert result.exit_code == 0
    # Check if version number is correctly outputted
    assert "readit v0.3" in result.output


# Testing -V option
def test_by_version(runner):
    result = runner.invoke(c.main, ["-V"])
    assert not result.exception
    assert result.exit_code == 0
    # Check if version number is correctly outputted
    assert "readit v0.3" in result.output


# Testing --help option
def test_help_option(runner):
    """Test the help output of the readit CLI tool"""
    result = runner.invoke(c.main, ["--help"])
    assert result.exit_code == 0
    assert not result.exception

    # Asserting key parts of the help message are present
    assert "Usage: main [OPTIONS]" in result.output
    assert "Readit - Command-line bookmark manager tool." in result.output
    assert "-a, --add TEXT" in result.output
    assert "-t, --tag TEXT" in result.output
    assert "-V, --version" in result.output
    assert "--help" in result.output

    # Asserting information
    assert "Options:" in result.output
    assert "Show bookmarks" in result.output
    assert "Add urls" in result.output
