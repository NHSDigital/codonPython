# Changelog

<!--next-version-placeholder-->

## v1.0.0 ()

### Feature

To enable packaging:

- Added the pyproject.toml (updated dependencies to latest versions)
- Added the poetry lockfile
- Updated folder structure to match typical package format (/src/packagename, and /tests/)
- Renamed to codonpython and updated imports

Updates to tests:

- Added a path to the file import function tests to force them to scan the tests/ folder instead of the whole project directory
- Added csv and xlsx files in the tests/ folder to test the file import functions

### Bug fixes

Various updates to deprecated code as a result of updating dependencies

### Documentation

- Updated readme with new installation instructions
- Now hosting documentation on Read the Docs

## v0.2.1 (09/01/2021)

- First release of codonPython