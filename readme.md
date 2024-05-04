# Oil Price Forecasting Project

This project aims to predict oil prices using machine learning techniques and provide a web-based visualization tool for exploring historical trends and making future price forecasts.

## Overview

The project consists of two main components:
1. **Data Analysis and Modeling**: The historical oil price data is analyzed using machine learning models (such as Linear Regression) to predict future oil prices based on various factors like demand, OPEC production, and OECD consumption.
2. **Web Application**: A Streamlit-based web app is developed to allow users to upload their own oil-related datasets, visualize historical trends using interactive plots, and generate forecasts for future oil prices.

## Dataset

The primary dataset used for this project is `data/new.csv`, which contains historical oil-related data including:
- `year`: Year of observation
- `demand`: Oil demand
- `OPEC`: OPEC production
- `OECD`: OECD consumption
- `price`: Oil price (target variable)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/kshula/Oil-price-ML-predictor.git
   cd opec
