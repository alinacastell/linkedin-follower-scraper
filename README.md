# Company Follower Scraper
This script scrapes follower counts from company LinkedIn URLs listed in a CSV file and saves the results in a new CSV file. It uses the requests library to make HTTP requests and BeautifulSoup to parse HTML content.

### Prerequisites
Python 3.x

Virtual environment (optional but recommended)

### Installation

Download the script files:
```bash
cd <path_to_files>
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

Install the required libraries:
```bash
pip install -r requirements.txt
```

### Usage

Create a `companies.csv` file in the same directory as the script with the following columns:
```csv
company_name,company_url
Company A,https://www.linkedin.com/company/company-a
Company B,https://www.linkedin.com/company/company-b
```

Run the `main.py` script:
```bash
python main.py
```

Check the generated `followers.csv` file for the results:

- The output CSV will have the columns company_name, company_url, and follower_counts.

## Script Details

- **scrape_follower_count(company_url)**: Scrapes the follower count from the given LinkedIn URL.

- **save_to_csv(data, file_path)**: Saves the scraped data to a CSV file.

- **main(input_csv, output_csv)**: Main function that reads the input CSV, scrapes follower counts, and saves the results to the output CSV.
