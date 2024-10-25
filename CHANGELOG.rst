*********
Changelog
*********

All notable changes to this project will be documented in this file.

readit v1.0.0 - 2020-01-21
========================

* Supports Python 3.6+

Features
********
- Add URL with Tags: Introduced the ability to add URLs along with a tag in a single operation, improving efficiency and flexibility.
- Enhanced Bookmark Export: Users can now choose the path to save exported bookmarked URLs, offering greater control and customization.

Improvements
************
- URL Validation: Improved validation logic for URLs to ensure accuracy and prevent errors.
- URL Tagging: Enhanced the tagging feature, allowing a URL to be associated with multiple tags.
- Search Functionality: Expanded search capabilities, enabling users to search URLs by tags or substrings for better filtering and retrieval.
- Open URL Flexibility: Updated the "open URL" feature, giving users the ability to specify how many URLs they want to open simultaneously.
- Error Handling: Improved error handling across the application, providing more graceful responses and preventing abrupt failures.

Updates
*******
- Test Cases for Database Modules: Added comprehensive test cases for database-related modules to ensure stability and reliability with future updates.
- Documentation: Updated the project documentation to reflect newly added features and changes.

readit v0.3 - 2020-01-21
========================

* Supports Python 3.0+

Updates
*******

* Github action workflows
* Refactor setup.cfg and setup.py
* Fix deploy

readit v0.2 - 2018-05-10
========================

* Supports Python 3.0+

Updates
*******

* Write the documentation (#63)
* Update description in setup file (#100)
* Write the test-cases for --help option (#85)
* Taglist should available to user instead of Error message (#91)
* Update README.rst (#90)
* User should get information about existed URLs in database (#88)
* User should have flexibility to bookmark links offline (86)
* Show list of all Tags (#83)
* Add doc strings to each method (#79)
* Export bookmarks to CSV file (#77)
* Copyright header appearing multiple times in the readthedocs documention (#98)
* Convert CHANGELOG.md to ReStructuredText for documentation (#93)
* Deprecation Warning after prompting any commands leads to readit (#103)

readit v0.1.1 - 2018-03-04
==========================

* Supports Python 2.7 and Python 3.6

Updates
*******

* 'test.db' is created in current directory (#60)
* Convert README.md to ReStructuredText (#58)
* Improve readability of code in 'database.py' file (#61)
* Add copyright header to files from readit (#47)

readit v0.1 - 2018-02-11
========================

* Initial release supports Python 2.7 and Python 3.6

Updates
*******
* Bookmark multiple URLs at a time
* Bookmark URL with respective Tags
* Search and display Bookmarks by TAG
* Display all Bookmarks in table format
* Remove a Bookmarked URL using specific ID
* Remove all Bookmarked URLs
* Update a Bookmarked URL with specific ID
* URL validation
* Open URL in browser
