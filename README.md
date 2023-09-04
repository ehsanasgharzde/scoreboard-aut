# Amir Kabir University (AUT) Event Scoreboard

This is a simple score board application developed for managing and visualizing event scores at Amir Kabir University (AUT). The application allows you to create, load, add, and visualize scores for different teams or participants.

## Project Files

- `main.py`: The main entry point of the application.
- `app.py`: Contains the `App` class responsible for the user interface and interactions.
- `files.py`: Manages file operations such as creating, loading, adding, and saving datasets.
- `plots.py`: Provides functions for calculating and visualizing scores as plots.
- `team-score.csv`: The CSV file used to store the event scores.

## Usage

1. Run `main.py` to launch the application.

2. Use the following options within the application:

   - **Create Dataset**: Create a new dataset by specifying columns for features.

   - **Load Dataset**: Load an existing dataset from a CSV file.

   - **Add Entry**: Add a new entry with scores for a team or participant.

   - **Calculate Scores**: Calculate scores based on the dataset and display visual plots.

   - **Display Plot**: Display the calculated plot based on the scores.

   - **Clear Plot**: Clear the displayed plot.

   - **Save Plot**: Save the current plot to an image file.

## Dependencies

- Python 3.x
- pandas library
- seaborn library
- matplotlib library
- turtle library
- tkinter library
- winsound library (for sound effects)

## Acknowledgments

This project makes use of various Python libraries and tools to create and visualize event scores. It provides a simple interface for managing and displaying scores for different teams or participants.

Feel free to customize and extend the project as needed for your specific event or use case.
