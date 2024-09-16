# TripAdvisor Restaurant Scraper

This project is a web scraper built using Python to extract data about restaurants listed on TripAdvisor for the Los Angeles area. The purpose of this scraper is to gather essential restaurant details such as their name, number of reviews, and price level, which can be used for various data analysis tasks, comparison, or to assist users in making informed dining choices.

## Data Description

The scraper uncovers the following key pieces of information about restaurants:

- **Restaurant Name**: The name of the restaurant listed on TripAdvisor.
- **Number of Reviews**: The total number of reviews provided by users for each restaurant.
- **Price Level**: The price level indicated by symbols like `$`, `$$`, or `$$$`, reflecting the relative cost of dining at the restaurant.

This data can be stored in CSV format, which allows for easy analysis, filtering, and sharing.

## Source Website

The data is scraped from [TripAdvisor's Los Angeles Restaurants Page](https://www.tripadvisor.com/Restaurants-g32655-Los_Angeles_California.html).

### Why TripAdvisor?

TripAdvisor is a well-known platform where users review restaurants, hotels, and other travel-related activities. It offers a large and detailed dataset of restaurant reviews, including user feedback and general information, making it a reliable source for scraping dining-related information.

## Features

- Scrapes restaurant name, number of reviews, and price level from TripAdvisor.
- Randomly rotates user-agent headers to avoid blocking.
- Outputs data to a CSV file for easy analysis.

## How to Run the Scraper

To run the scraper on your local machine, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/tripadvisor-restaurant-scraper.git
cd tripadvisor-restaurant-scraper
```

### 2. Install Dependencies

Once you are in the project directory, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the required libraries, including `requests`, `beautifulsoup4`, and `lxml`.

### 3. Run the Scraper

After installing the dependencies, you can run the scraper by executing the following Python command:

```bash
python main.py
```

This will initiate the scraper, fetch the restaurant data from TripAdvisor, and store the results in a CSV file named `TripAdvisor_LA.csv` in the project directory.

### 4. CSV Output

After running the scraper, the output will be stored in a CSV file (`TripAdvisor_LA.csv`), with the following columns:

- `name`: Restaurant name
- `reviews`: Number of reviews
- `price_level`: Price level of the restaurant

## Prerequisites

Before running the project, make sure you have:

- Python 3.x installed
- Internet connection (for fetching data from TripAdvisor)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to fork this repository, submit pull requests, or create issues for any bugs or suggestions for improvements!

---

### Example Output

| name              | reviews   | price_level |
|-------------------|-----------|-------------|
| Restaurant A      | 1200      | $$          |
| Restaurant B      | 450       | $           |
| Restaurant C      | 2345      | $$ - $$$    |

---

### Contact

If you have any questions or feedback, feel free to reach out at [basil.ahmed@nyu.edu](mailto:basil.ahmed@nyu.edu).