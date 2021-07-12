# Project 0: Data Zero #

## Project Description ##

A console application for automating the initial stages of a data pipeline, finding and storing tabular data. It makes requests to a website provided by its user, checks on User-Agent permissions of that site, then seeks tabular data to parse, download, and format. The program's functional design allows for easily adding or extending features depending on the user's needs. Automated testing, infrastructure, and deployment tools allow for easy integration with other tools to supplement a user's analysis workflow, and in a variety of environments.

## Technologies Used ##
- Programming
  - Python
  - Bash Scripting
- Automation
  - Ansible
-  Test
  - Shell Scripts targeting functions.
- Containerization and Orchestration
  - Docker


## Features ##

### Implemented Features ###

- Checks site for User Agent Permissions
  - Provides user with information from the site's robot.text and advises on the implications of scraping data for that sites.
  - Parses url path into pieces for Data functions.
  - Makes an http request and searches for tabular data.
  - If site has tabular data, will temporarily save HTML to be parsed.
  - Using the Beautiful Soup library, app parses HTML data into a human readable format.
  - Gives a snapshot or saves data as an CSV.
  - Organizes saved files, by creating directories and file names, based on the site's hostname, and page scraped.
  - Logs each scrape in separate directory, with useful information for its user.

### Planned Features ###
- Improve Interface
  - Improve readability using the Blessed module.
  - Create and Document CLI commands
  - Expand Command line features and add functions for more robust Data Collection.
  - Create Repeatable, or scheduled scraping of past sites. (i.e. Market data at Open and Close each day)

## Getting Started ##


## Usage ##


## Contributors ##

Anthony M. Jarvis

## License ##

Copyright 2021 Anthony M. Jarvis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

