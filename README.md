# BQ Parser

BQ Parser is a tool developed to help create BigQuery JSON shemas based on other RDBMS' schemas.

## [Supported RDBMS](#supported-rdbms)

:white_check_mark: Oracle

## Usage

- Simply **clone this repo**
- Run the script using `python bqparser.py [args] [flags]`

### Arguments

- The script requires 2 **positional** arguments, being:
  - path_to_source: The path to the source schema file to convert from
    - For specifying a directory contaning schema files, use de `-d` flag
  - source_db: Which RDBMS schema you're converting from
    - Supported source RDBMS: [Check supported session](supported-rdbms)
