# Web Scraping Project: Memoryzone.com.vn

This project is designed to scrape product information from [Memoryzone](https://memoryzone.com.vn/) using Selenium and save the data in JSON and CSV formats.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Installation

1. **Clone the repository:**

   ```sh
   git https://github.com/HLoc26/crawling-memoryzone.git
   cd crawling-memoryzone
   ```

2. **Set up a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Download and set up the Edge WebDriver:**

   Ensure you have the Microsoft Edge browser installed. Download the Edge WebDriver that matches your browser version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Add the WebDriver to your system PATH.

   In case you use another browser, in `main.py`, change line `10` from `driver = webdriver.Edge()` to `driver = webdriver.<YourBrowser>()`

   Check [here](https://www.selenium.dev/documentation/webdriver/browsers/) to see if your browser is supported by Selenium and [here](https://selenium-python.readthedocs.io/installation.html#drivers) for more information.

## Usage

To start the web scraping process, simply run the `main.py` script:

```sh
python main.py
```

This will open the Edge browser, navigate to the Memoryzone website, and begin scraping product information. The scraped data will be saved in both JSON and CSV formats in the `JSON` and `CSV` directories, respectively.

## Project Structure

```
memoryzone-scraper/
├── JSON/
├── CSV/
├── main.py
├── PageStructure.py
├── requirements.txt
└── README.md
```

- `main.py`: The main script that runs the web scraping process.
- `PageStructure.py`: Contains the definitions for the `Item`, `Page`, and `Collection` classes.
- `JSON/`: Directory where the JSON output files will be saved.
- `CSV/`: Directory where the CSV output files will be saved.
- `requirements.txt`: File listing the required Python packages.
- `README.md`: This readme file.
