# Assistacate

This is a new project called Assistacate. It includes a web application named `sara_web_app.py`.

## Sara Web App

The `sara_web_app.py` is a Flask application with several endpoints. It is designed to manage and schedule meetings.

### Endpoints

- `/status`: This endpoint returns the status of the scheduler.
- `/meetings`: This endpoint returns a list of upcoming meetings.
- `/config`: This endpoint allows for getting and updating the configuration.

## Setup and Installation

To run the project, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required packages using pip:

```
pip install -r requirements.txt
```

3. Run the Flask application:

```
python3 sara_web_app.py
```

This will start the server and the application will be accessible at `localhost:5000`.

## Contributing

Contributions are welcome. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)