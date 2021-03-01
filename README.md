# BQ Parser

BQ Parser is a tool developed to help create BigQuery JSON shemas based on other RDBMS' schemas.

## Supported RDMBS'

Oracle :white_check_mark:

## Usage

- Simply **clone this repo**
- Run the script using `python bqparser.py [args] [flags]`

### Arguments

- The script requires 2 **positional** arguments, being:
  - path_to_source: The path to the source schema file to convert from
    - For specifying a directory contaning schema files, use de `-d` flag
  - source_db: Which RDBMS schema you're converting from
    - Supported source RDBMS: Oracle

### Usage examples

> Converting a TXT called `schema.txt` generated from Oracles' DESCRIBE method
> `python bqparser.py ./schema.txt Oracle`

## Future updates

Adding support for different RDBMS'

## Contributing

Feel free to make a PR adding support to or suggesting any improvements to the current code. Let's build this together!
