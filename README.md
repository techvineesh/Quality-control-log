# Quality-control-log
# Log Query Interface

A simple command-line interface (CLI) for searching through log files based on user-defined criteria.

## Overview

This project consists of two main components:

1. Log Ingestor: A Python script (`log_ingestor.py`) that captures logs from different stages of an application and writes them to designated log files.

2. Query Interface: A Python script (`query_interface.py`) that provides a CLI for users to search through log files using various criteria such as log level, source, and timestamp.

## Features

- **Log Ingestor:**
  - Integrates with multiple APIs to capture logs.
  - Configurable logging levels and file paths.
  - Robust error handling to ensure logging functionality is not disrupted.

- **Query Interface:**
  - Offers a user-friendly CLI for log search.
  - Allows filtering based on log level, source, and timestamp.
  - Efficient search algorithm for quick results.
Usage
Log Ingestor:

Run log_ingestor.py to capture logs from your application's APIs and write them to log files.
Query Interface:

Run query_interface.py to launch the CLI.
Enter your search criteria as prompted.
View search results displayed in the console.
Configuration
Modify config.json to customize logging configurations such as log levels and file paths for the Log Ingestor.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by [insert inspiration here].
Special thanks to [insert contributor names here] for their contributions.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/log-query-interface.git
cd log-query-interface

Replace placeholders like `your_username`, `your_project_name`, and `[insert ... here]` with appropriate values relevant to your project. You can also customize and expand upon this template as needed to provide more detailed information about your project.
