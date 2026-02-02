# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : SRIKAKOLAPU GANGA LAKSHMI

*INTERN ID* : CTIS2918

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH

*DESCRIPTION*:
Weather Forecast Visualization – Codetech IT Solutions Pvt Ltd
Overview

This project demonstrates API integration and data visualization using Python, aimed at providing a clear, interactive way to analyze weather trends. It fetches real-time weather forecast data for Hyderabad from the OpenWeatherMap API and visualizes key parameters such as temperature, humidity, and wind speed over a five-day period. The project showcases practical skills in API interaction, data processing, and visualization techniques, and is designed to run on a cross-platform Python environment including Windows, macOS, and Linux.

The goal of this project is to demonstrate how real-world data can be accessed programmatically and presented in an informative and visually appealing manner. It is suitable for academic projects, professional portfolios, and as a foundation for more advanced weather data analysis applications.

Features

API Integration: Connects seamlessly with the OpenWeatherMap API to fetch live weather data using a secure API key.

Structured Data Processing: Parses JSON responses from the API and organizes them into a structured Pandas DataFrame, making it easy to manipulate and analyze.

Data Visualization: Utilizes Matplotlib and Seaborn to generate line plots that visually represent temperature, humidity, and wind speed trends over time.

Interactive Analysis: Although currently static plots are used, the framework allows for future extensions into interactive dashboards.

Error Handling: Checks API responses for errors and provides meaningful messages if the API request fails, ensuring reliability.

Cross-Platform Compatibility: The project can be executed on any platform supporting Python, including Windows, macOS, and Linux.

Platform & Technology Stack

Programming Language: Python 3.x

Python Libraries:

requests – for API calls

pandas – for data manipulation

matplotlib – for static visualizations

seaborn – for enhanced visual styling

Data Source: OpenWeatherMap API (RESTful API)

Development Environment: Jupyter Notebook, VS Code, or any Python IDE

Supported Platforms: Windows, macOS, Linux

The project demonstrates a full workflow of data collection, processing, and visualization, providing a strong example of Python’s versatility in handling real-time datasets.

How It Works

API Request: The script constructs a request URL using the city name and API key, specifying metric units for temperature. It sends a GET request to the OpenWeatherMap API.

Data Extraction: The JSON response from the API contains a list of forecast data at 3-hour intervals. The script extracts:

dt_txt (date and time of forecast)

main.temp (temperature in Celsius)

main.humidity (humidity percentage)

wind.speed (wind speed in meters per second)

Data Organization: The extracted data is converted into a Pandas DataFrame with appropriate column names (Date, Temperature (°C), Humidity (%), Wind Speed (m/s)).

Visualization: Using Seaborn and Matplotlib, the script creates three line plots representing:

Temperature trends over time

Humidity trends over time

Wind speed trends over time
Each plot is titled for clarity, and all plots are arranged together for easy comparison.

Display: The plots are displayed using plt.show(), providing an intuitive visual understanding of weather patterns.

Usage Instructions

Install Dependencies:

pip install requests pandas matplotlib seaborn

View Visualizations: Three line plots will be displayed, representing temperature, humidity, and wind speed trends for the city of Hyderabad.

Purpose and Applications

This project highlights the practical use of API integration to fetch real-time data and demonstrates data visualization techniques to analyze and interpret the data effectively. It provides a foundation for:

Weather trend analysis

Academic and portfolio projects in data science

Learning Python’s data handling and visualization capabilities

Developing more advanced dashboards and interactive applications

By integrating API data with Python visualization libraries, users can transform raw numerical data into meaningful insights, a critical skill in data analysis, business intelligence, and software development.

This project is developed under Codetech IT Solutions Pvt Ltd, showcasing professional-quality Python coding standards, structured data handling, and practical visualization skills.


*OUTPUT* : 
<img width="1594" height="997" alt="Image" src="https://github.com/user-attachments/assets/ada2b4f8-0fb1-4da2-ba0c-1a3c7103841b" />
