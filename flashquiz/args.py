from argparse import ArgumentParser
from .gui.constants import Screen


def handle_args():
    """Create all arguments, and return the parsed given arguments"""
    args = ArgumentParser()
    args.add_argument("--fps",
                      metavar="FPS",
                      type=int,
                      help="Frames per second to run at",
                      default=60
                      ),

    args.add_argument("--cards_file",
                      metavar="INPUT_FILE",
                      help="Path to the file containing questions and answers for your flashcards",
                      default="default.csv")
    args.add_argument("--font",
                      metavar="FONT_NAME",
                      type=str,
                      help="Name of the pygame-supported font to use",
                      default="inkfree")
    args.add_argument("--cards_front",
                      metavar="IMG_PATH",
                      help="Path to the .jpg to use for all flashcard front backgrounds (500x250 pixels)",
                      default="assets/card_front.jpg")
    args.add_argument("--cards_back",
                      metavar="IMG_PATH",
                      help="Path to the .jpg to use for all flashcard back backgrounds (500x250 pixels)",
                      default="assets/card_back.jpg")
    args.add_argument("--h",
                      type=int,
                      metavar="WIN_HEIGHT",
                      help="Window height",
                      default=Screen.height)
    args.add_argument("--w",
                      type=int,
                      metavar="WIN_WIDTH",
                      help="Window width",
                      default=Screen.width)
    args.add_argument("--title",
                      type=str,
                      metavar="WIN_TITLE",
                      help="Window title",
                      default=Screen.title)

    return args.parse_args()
