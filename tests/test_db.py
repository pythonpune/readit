import os

import pytest

from readit.database import DatabaseConnection


@pytest.fixture
def db_connection():
    # Setup: Create a temporary database file for testing
    db = DatabaseConnection()
    yield db
    # Teardown: Close the database and remove the temporary database file
    db.db.close()
    if os.path.exists(db.databasefile):
        os.remove(db.databasefile)


def test_init_db_creates_tables(db_connection):
    # Test if the tables are created during initialization
    cursor = db_connection.cursor
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    assert len(tables) == 4  # bookmarks, tags, url_tags and considering sqlite_sequence table too
    assert ("bookmarks",) in tables
    assert ("tags",) in tables
    assert ("url_tags",) in tables


def test_add_url_success(db_connection):
    # Test successful addition of a URL
    url = "http://example.com"
    result = db_connection.add_url(url)
    assert result

    # Verify the URL was added to the database
    cursor = db_connection.cursor
    cursor.execute("SELECT url FROM bookmarks WHERE url=?", (url,))
    assert cursor.fetchone()[0] == url


def test_add_url_duplicate(db_connection):
    # Test adding a duplicate URL
    url = "http://example.com"
    db_connection.add_url(url)  # First time
    result = db_connection.add_url(url)  # Second time (should fail)
    assert not result


def test_tag_url_success(db_connection):
    # Test tagging a URL with a new tag
    url = "http://example.com"
    tag = "test"
    result = db_connection.tag_url(url, tag)
    assert result

    # Verify the tag was added to the database
    cursor = db_connection.cursor
    cursor.execute(
        """
        SELECT b.url, t.tag_name
        FROM bookmarks b
        JOIN url_tags ut ON b.id = ut.url_id
        JOIN tags t ON ut.tag_id = t.id
        WHERE b.url=? AND t.tag_name=?
    """,
        (url, tag),
    )
    assert cursor.fetchone() == (url, tag)


def test_list_all_tags(db_connection):
    # Test listing all tags
    db_connection.tag_url("http://example.com", "test")
    db_connection.tag_url("http://example.org", "example")

    tags = db_connection.list_all_tags()
    assert len(tags) == 2
    assert "test" in tags
    assert "example" in tags


def test_delete_url(db_connection):
    # Test deleting a URL and associated tags
    url = "http://example.com"
    db_connection.add_url(url)
    db_connection.tag_url(url, "test")

    # Get the URL ID
    cursor = db_connection.cursor
    cursor.execute("SELECT id FROM bookmarks WHERE url=?", (url,))
    url_id = cursor.fetchone()[0]

    # Delete the URL
    result = db_connection.delete_url(url_id)
    assert result

    # Verify the URL and associated tags were deleted
    cursor.execute("SELECT url FROM bookmarks WHERE id=?", (url_id,))
    assert cursor.fetchone() is None


def test_update_url_success(db_connection):
    # Test updating an existing URL
    db_connection.add_url("http://example.com")

    # Get the URL ID
    cursor = db_connection.cursor
    cursor.execute("SELECT id FROM bookmarks WHERE url=?", ("http://example.com",))
    url_id = cursor.fetchone()[0]

    # Update the URL
    result = db_connection.update_url(url_id, "http://updated.com")
    assert result

    # Verify the URL was updated in the database
    cursor.execute("SELECT url FROM bookmarks WHERE id=?", (url_id,))
    assert cursor.fetchone()[0] == "http://updated.com"


def test_search_url(db_connection):
    # Test searching for URLs by tag or substring
    db_connection.tag_url("http://example.com", "test")
    db_connection.tag_url("http://example-test.org", "mytag")

    # Search by tag
    results = db_connection.search_url("test")
    assert len(results) == 1
    assert results[0][1] == "http://example.com"

    # Search by substring
    # (if given search value is tag and if it is available then it does not search in url substring)
    results = db_connection.search_url("example")
    assert len(results) == 2


def test_open_url(db_connection, mocker):
    # Test opening a URL in the browser
    mocker.patch("builtins.input", return_value="yes")  # Mock user confirmation input
    mocker.patch("webbrowser.open", return_value=True)  # Mock web browser opening

    db_connection.add_url("http://example.com")
    result = db_connection.open_url("example")
    assert result
