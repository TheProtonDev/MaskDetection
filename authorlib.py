print("If an error has occured\n\nPlease run `python3 -m pip install -r requirements.txt` to fix the error")
import pyfiglet
class AuthorLib:
    """
    Valid Colors: Case Doesn't Matter

    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    LIGHT_GRAY,
    DARK_GRAY,
    LIGHT_RED,
    LIGHT_GREEN,
    LIGHT_YELLOW,
    LIGHT_BLUE,
    LIGHT_MAGENTA,
    LIGHT_CYAN,
    WHITE
    """

    def __init__(self, author: str, project_name: str = None, color: str = None):
        self.author = author
        try:
            self.color = color.upper()
        except:
            pass
        self.project_name = project_name

    def output(self):
        try:
            if self.color:
                if self.project_name:
                    # Project Name Output
                    pyfiglet.print_figlet(text=self.project_name, colors=self.color)
                # Author Name Output
                pyfiglet.print_figlet(text=f"Made   By {self.author}", colors=self.color)
        except:
             if self.project_name:
                # Project Name Output
                pyfiglet.print_figlet(text=self.project_name)
                # Author Name Output
                pyfiglet.print_figlet(text=f"Made   By {self.author}")
