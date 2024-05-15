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

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/log-query-interface.git
cd log-query-interface

Replace placeholders like `your_username`, `your_project_name`, and `[insert ... here]` with appropriate values relevant to your project. You can also customize and expand upon this template as needed to provide more detailed information about your project.
