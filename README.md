# Lionel Messi vs Cristiano Ronaldo | Club Career Analysis

This web app provides a detailed comparison of Lionel Messi and Cristiano Ronaldo's club careers. It allows users to explore various statistics, achievements, and key moments in their careers to analyze the ongoing GOAT (Greatest of All Time) debate between the two legendary footballers.

## About Dataset
This is a kaggle dataset on the club career goals(without friendly) of Lionel Messi and Cristiano Ronaldo, between `10 July 2002 to 18 March 2023`. 
You can check out the dataset [here](https://www.kaggle.com/datasets/azminetoushikwasi/lionel-messi-vs-cristiano-ronaldo-club-goals)

## Features

-**Interactive Visualizations:** Dynamic charts and visualizations powered by matplotlib and seaborn libraries.

-**User-friendly Interface:** Designed with simplicity in mind, making it easy to navigate through the data and visual insights.


## Demo

You can check out the live version of the web app [here](https://goat-debate.streamlit.app/).

## Project Structure
goat-debate-web-app/

````
├── data                  # Directory containing dataset
├── .gitignore            # Files and directories to be ignored by Git
├── app.py                # Main Streamlit app file
├── img                   # Directory containing favicon
├── helper.py             # Script containing helper functions for the app
├── preprocessor.py       # Script for preprocessing data before analysis 
├── requirements.txt      # List of all the necessary Python packages              
└── README.md             # Project documentation
````

## Dependencies

- **Streamlit**: Web framework for creating interactive apps.
- **streamlit_option_menu**: packages for easy creation of navigation menus
- **numpy**: Support for large, multi-dimensional arrays and matrices.
- **pandas**: Data manipulation and analysis.
- **matplotlib**: Visualization library for plotting charts and graphs.
- **seaborn**: Statistical data visualization library for attractive and informative graphics.

## Installation

Follow the steps below to set up and run the project locally:

### Clone the repository:

```bash
git clone https://github.com/xyxuxx/goat-debate-web-app.git
cd goat-debate-web-app
```

### Install dependencies:
Make sure you have Python 3.7+ installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```

### Run the app:
Launch the Streamlit web app locally:
```bash
streamlit run app.py
```

### Access the web app: 
Once the server is running, open your browser and navigate to `http://localhost:8501` to explore the app.

## Contact

For any inquiries or suggestions, reach out to me at: [syfullah.shifat@gmail.com](mailto:syfullah.shifat@gmail.com).
