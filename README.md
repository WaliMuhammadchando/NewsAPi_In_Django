# Django News App

This is a Django web application that displays the latest news articles using the News API. It fetches the top headlines from the API and presents them in an interactive and dynamic manner.

## Features

- Display the top 3 news articles initially.
- Clicking on a news article title reveals its description.
- Load more news articles by clicking the "More News" button.
- Responsive design for optimal viewing on different devices.

## Prerequisites

- Python 3.6+
- Django 3.0+
- News API key (Sign up for an API key at [News API](https://newsapi.org/))

## Installation

1. Clone the repository:

git clone https://github.com/your-username/django-news-app.git

2. Navigate to the project directory:

cd django-news-app

3. Create a virtual environment:

  python3 -m venv env

4. Activate the virtual environment:

- On macOS and Linux:
- 
source env/bin/activate

- On Windows:

- env\Scripts\activate
  
5. Install the dependencies:

   pip install -r requirements.txt


7. Set up the API key:

- Open the `settings.py` file in the `newsapp` directory.
- Replace `'YOUR_NEWS_API_KEY'` with your actual News API key.

7. Run the Django development server:

   python manage.py runserver


8. Open a web browser and visit [http://localhost:8000](http://localhost:8000) to see the application.

## Usage

- The application will display the top 3 news articles initially.
- Click on a news article title to expand its description.
- Click the "More News" button to load additional news articles.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).






