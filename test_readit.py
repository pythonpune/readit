import pytest
import click
from readit import cli as c
import readit.database
from click.testing import CliRunner


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


#Testcase for --version option
def test_version(runner):
    result = runner.invoke(c.main, ['--version'])
    assert not result.exception
    assert result.exit_code == 0
    expected = "readit v0.1.1\n"
    assert result.output == expected


#Testcase for -V option
def test_by_version(runner):
    result = runner.invoke(c.main, ['-V'])
    assert not result.exception
    assert result.exit_code == 0
    expected = "readit v0.1.1\n"
    assert result.output == expected


if __name__ == '__main__':
    c.main()
