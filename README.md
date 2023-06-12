# Web Scraper

## Overview
Utility for web scraping through the command line.

## Requirements
- python3
- python3 pip

## Installation

If you accomplish the requirements, create a Python virtual environment with the necessary libraries by running:
```
make venv
```

If you haven't installed requirements yet, you can execute:
```
make install
```

## Getting Started

1. Source en virtual environment:
    ```
    source env/bin/activate
    ```
2. Scraping a url:
    ```
    python3 scrap.py URL
    ```

## Adding fields
You can edit the `config/options.json` file to increase the fields for web scraping.
You can include in the metadata array-value, more elements like:

```json
{   
    "name":     "description",
    "label":    "meta",
    "attrs":    [
                    {
                        "name": "description"
                    },
                    {
                        "property": "og:description"
                    }
                ],
    "class_":   [
                    "desc"
                ]
}
```
In the example, `description` is searched in the `meta` tags of the html code with the filters indicated on `attrs` and `class_`.