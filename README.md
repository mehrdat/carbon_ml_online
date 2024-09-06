# Carbon Intensity Analysis in UK Areas
<div style="text-align: center;">
    <img src="img/1.jpg" style="width:85%; max-width:300px;">
</div>
This project focuses on analyzing carbon intensity levels across various regions of the UK. The data is retrieved from a public API and then processed and visualized using Python scripts to gain insights into the UK's energy mix and carbon emissions.

## Project Structure

The project comprises several scripts that work together to automate data retrieval, preparation, and analysis:

### `consume.py`
This script fetches carbon intensity data from an external source, most likely the [UK National Grid ESO's Carbon Intensity API](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v2-0-0). It makes requests to retrieve carbon intensity data for different regions in real-time or historically.

### `data_prep.py`
Once the data is fetched, this script cleans and prepares it for analysis. Tasks like handling missing values, standardizing formats, and adding additional features occur in this step.

### `producer.py`
The script responsible for further transforming the data or making it ready for long-term storage, databases, or real-time data streams.

### `utils.py`
Utility functions that handle common tasks across the project, like logging, formatting, or error handling.

## Data Source: UK Carbon Intensity API

The data for this project comes from the [UK National Grid Carbon Intensity API](https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v2-0-0), which provides real-time and historical data on carbon emissions from electricity consumption. This API allows for querying carbon intensity across different regions and time periods in the UK.

Here’s a quick summary of how data flows through the project:

1. **Fetch Data**: Use the `consume.py` script to request data from the API.
2. **Clean Data**: The `data_prep.py` script handles missing values and ensures data consistency.
3. **Feature Engineering**: Add new features or transform the data in `producer.py`.
4. **Model Training**: The `train.py` script trains a machine learning model on the processed data.
5. **Evaluation**: Evaluate the model’s performance to ensure accurate predictions.
<div style="text-align: center;">
    <img src="img/2.jpg" style="width:50%; max-width:300px;">
</div>
## Conclusion

This project uses real-time data from the UK Carbon Intensity API to analyze carbon emissions in different regions. By leveraging machine learning models, it also attempts to predict future trends in carbon intensity, providing a comprehensive look into the carbon emissions landscape in the UK.
