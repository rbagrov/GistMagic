from IPython.core.magic import (
    Magics,
    magics_class,
    line_magic,
)
import github


@magics_class
class Gister(Magics):
    def __init__(self, shell, token=None):
        super(Gister, self).__init__(shell)

        if not token:
            self.token = token
            print("\nPlease add token. Ex %load_ext gister <github_token>")
            return

        self.token = token

    @line_magic
    def gister(self, line):
        """
        Upload code to gist

        Usage:\\
            %load_ext gister
            %gister -X  (%gister -5 / %gister -25)

        The argument -X is representing the last X In/Out sequences
        """
        if not self.token:
            print("\nPlease add token and reload: %reload_ext gister <github_token>")
            return

        try:
            assert line.startswith("-")
        except AssertionError:
            print("\nMissing - before the amount of lines to extract. Ex. %gister -10")
            return

        try:
            n = int(line.lstrip("-"))
        except ValueError:
            print("\nLines need to be integer.")
            return

        SubIn = self.shell.user_ns["In"][-n:]
        Out = self.shell.user_ns["Out"]
        len_in = len(self.shell.user_ns["In"]) - 1
        data = ""

        try:
            for l in range(1, n):
                data = (
                    data
                    + f"In[{l}]: {SubIn[l-1]}<br/>Out[{l}]: {Out.get((len_in-n)+l)}<br/><br/>"
                )
        except IndexError:
            print("Getting everything from the start of the current session.")

        try:
            g = github.Github(self.token)
            gu = g.get_user()
            gist = gu.create_gist(
                True,
                {"snipped.md": github.InputFileContent(content=data)},
                description="Generated by Gister",
            )
            print(f"\n{gist.html_url}\n")
            return
        except github.BadCredentialsException:
            print("\n The provided Gist token failed to authenticate with GutHub")
