# Tarantulas Submission
## Project description

1. **Data Engineering**: Merging data of different shapes (land prices, buildings, Zensus, etc.)
2. Generating features: Building new features by exploring other data streams such as OSM (number/length of travel paths) and World Cover (proportion of grassland, etc.)
3. Feature reduction: Using PCA we projected a total of 200 features to 20 while maintaining 95% of the data science variance
4. Model evaluation: Examination of different models (see Model Selection file) and scoring analysis

## How to test our product

**Locally**

1. Install Python and Anaconda
2. Run following command to create the anaconda environment with all necessary dependencies:`conda create --name tarantulas --file requirements.txt`
3. Activate environment with: `conda activate tarantulas`
4. Run the application by: `streamlit run app.py`

  **On the Remote Server**

> Access the app by clicking [This App Link](https://l-vicen-ifohack-dlr-challenge-home-l0fflx.streamlit.app/)

---

## Team Tarantulas Members

* Rohan Walia
* Yichen Zhang
* Lucas Vicentim
* Billy Herrmann
* Sandro Barrios
