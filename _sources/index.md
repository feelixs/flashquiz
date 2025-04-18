# Documentation

FlashQuiz is a study tool Python package for practicing flashcards

## Installation

`pip install flashquiz`


## Running

Open the terminal and run

 `flashquiz --arg ARG`


## Args

| Argument        | Behavior                                                      | Default                         |
|-----------------|---------------------------------------------------------------|---------------------------------|
| `--file`        | .csv file containing questions and answers for the flashcards | flashquiz/default.csv           |
| `--font`        | Sets the font for all text (must be pygame-supported)         | inkfree                         |
| `--cards_front` | .jpg file to use as the background for cards' front           | flashquiz/assets/card_front.jpg |
| `--cards_back`  | .jpg file to use as the background for cards' back            | flashquiz/assets/card_back.jpg  |
| `--h`           | Sets the window height                                        | 500                             |
| `--w`           | Sets the window width                                         | 700                             |
| `--title`       | Changes the window title                                      | FlashQuiz                       |
| `--fps`         | Set the fps for the window to run at                          | 30                              |


## Usage

Although FlashQuiz contains 10 default flashcards to show its functionality, this package is designed to help you study your own flashcards.

In order to study your own questions and answers, simply create a .csv file formatted:

| Questions   | Answers |
|-------------|---------|
| What's 1+1? | 2       |
| ...         | ...     |

Let's say for example you named this file `math_questions.csv`

To use FlashQuiz with this custom .csv document, `cd` into the directory containing `math_questions.csv` and run

`flashquiz --file math_questions.csv`
