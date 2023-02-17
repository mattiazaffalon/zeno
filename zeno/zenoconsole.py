from datetime import datetime

class ZenoConsole:

    PROMPT = ">>> "
    LOGS_DELIMITER = "-" * 80

    def __init__(self, buffer, input_function=input):
        self.buffer = buffer
        self.input_function = input_function

    def salutation(self):
        print("\n")

    def start(self, loopOnce=False):

        try:
            while True:
                user_input = self.input_function(f"{self.PROMPT} ")
                self.buffer.write("\n")
                self.buffer.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                self.buffer.write("\n\n")
                self.buffer.write(user_input)
                self.buffer.write("\n\n")
                self.buffer.write(self.LOGS_DELIMITER)
                self.buffer.flush()

                if (loopOnce):
                    break
        except EOFError:
            self.salutation()
        except KeyboardInterrupt:
            self.salutation()


