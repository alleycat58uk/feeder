# Feeder
Natural language processing of RSS news feed aggregations

## Aim
- havest and agregate news feeds from around the world
- provide a searchable interface to the data
- use natural language processing to analyse the narative

## progress
- download, process and store feed items (current)
- create search interface for stored items (to do)
- natural language processing of items (to do)

## Technologies
- **Python 3** is the scripting language because it comes highly recomended for this type of use case, plus I wanted to learn it!
- **couchDB** is the prefered database, again because I wanted learn it.  Elastic search was a close contender and may be integrated as an option in the future.

## Dependencies
- Python 3 (tested with 3.6.4)
  - requests
  - beautifulsoup4
  - json
- couchDB 2 (tested with 2.1.1)
