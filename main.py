import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.linear_model import LinearRegression
from datetime import timedelta

# Load CSV file into a DataFrame
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Train the Linear Regression model on the entire dataset
def train_model(df, features, target):
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

# Define a function to make forecasts
def make_forecast(model, initial_data, period_years):
    forecast_dates = pd.date_range(start=initial_data.index.max() + timedelta(days=1), 
                                   periods=period_years * 365, freq='D')
    forecast_data = pd.DataFrame(index=forecast_dates)
    forecast_data['forecast_price'] = model.predict(forecast_data.index.to_numpy().reshape(-1, 1))
    return forecast_data

# Main Streamlit app
def main():
    st.title('Oil Price Forecasting App')
    
    # Sidebar for uploading data
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        # Show DataFrame info
        st.subheader("Dataset Information")
        st.write(df.info())
        
        # Select columns for visualization
        st.subheader("Select Columns for Visualization")
        selected_columns = st.multiselect("Select columns", df.columns)
        
        # Plot selected columns against years
        if selected_columns:
            df['year'] = pd.to_datetime(df['year'], format='%Y')
            fig = px.line(df, x='year', y=selected_columns, title='Selected Columns Over Time')
            st.plotly_chart(fig)
        
        # Train the model and make forecasts
        st.subheader("Oil Price Forecast")
        features = ['demand', 'OPEC', 'OECD', 'opec_share']
        target = 'price'
        model = train_model(df, features, target)
        
        period_years = st.slider("Select forecast period (years)", 1, 5, 3)
        if st.button("Generate Forecast"):
            forecast_data = make_forecast(model, df.set_index('year'), period_years)
            st.write(forecast_data)
            st.line_chart(forecast_data)
    
if __name__ == '__main__':
    main()

