# DigiKala Scraping Project 📦

A Python-based web scraping project that searches DigiKala products, filters them by minimum star rating, extracts relevant information, and saves the results into a CSV file.

This project demonstrates a simple end-to-end scraping workflow using Python, HTTP requests, data parsing, and CSV export.

## ✨ Features

- Search products on DigiKala using a custom query
- Collect data across multiple pages
- Filter results by minimum star rating
- Extract key product details such as:
  - title
  - stars
  - price
  - URL
- Save the collected data into a CSV file
- Console-based interactive workflow

## 🛠️ Tech Stack

- Python 3
- requests
- pandas
- pyfiglet

## 📁 Project Structure

- [main.py](main.py) – application entry point and user interaction flow
- [scraper.py](scraper.py) – handles API requests to DigiKala
- [parser.py](parser.py) – extracts and filters the required data
- [exporter.py](exporter.py) – exports the results to CSV
- [log.py](log.py) – custom terminal logging messages
- [data/data.csv](data/data.csv) – sample exported results
- [requirements.txt](requirements.txt) – project dependencies

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/ParhamFarasatyar/DigiKalaScraping.git
cd DigiKalaScraping
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the project with:

```bash
python main.py
```

You will be prompted to enter:

- the product keyword to search for
- the number of pages to collect
- the minimum star rating required

The script will then scrape the matching results, extract the relevant data, and save it to [data/data.csv](data/data.csv).

## 🔍 How It Works

1. The app asks for a search term and filtering criteria.
2. The scraper sends requests to the DigiKala search API.
3. The parser extracts relevant product fields from each response.
4. Products below the selected star threshold are ignored.
5. The filtered results are saved into a CSV file.

## 📄 Output Example

The exported CSV contains columns such as:

- title
- stars
- price
- url

## ⚠️ Notes

- This project is intended for learning and personal use.
- Respect the website’s terms of service and avoid excessive requests.
- Some websites may change their structure or API behavior over time, so the scraper may need updates.

## 💡 Future Improvements

Possible enhancements for this project include:

- adding support for Excel export
- implementing a more robust retry mechanism
- improving error handling for API changes
- adding pagination and rate-limit control
- building a graphical user interface

---

If you want, I can also help you turn this into a more advanced version with a proper CLI interface, async scraping, or a database export feature.
