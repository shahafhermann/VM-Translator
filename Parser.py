class Parser:
    """
    A class defining a file parser.
    """

    COMMENT_START = "/"
    PUSH = "push"
    POP = "pop"

    def __init__(self, path, output, code_writer, file_name):
        """
        Initialize the file parser.
        :param path: The file path
        :param output: The output file
        :param code_writer: The CodeWriter "object"
        :param file_name: The file's name
        """
        self.__path = path
        self.__output = output
        self.__codeWriter = code_writer
        self.__file_name = file_name

    def parse_file(self):
        """
        Parse the file.
        :return: True if a code for comparison logic was found, False otherwise
        """
        with open(self.__path, "r") as file:

            cur_function = ""
            for line in file:
                line = line.strip()
                line = " ".join(line.split())
                if not line.strip() or line[0] == self.COMMENT_START:
                    continue
                elif self.COMMENT_START in line:
                    line = line.split(self.COMMENT_START, 1)[0]
                args = line.split(" ")

                if args[0] == "push":
                    code = self.__codeWriter.translate_push(args[1], args[2],
                                                            self.__file_name)
                elif args[0] == "pop":
                    code = self.__codeWriter.translate_pop(args[1], args[2],
                                                           self.__file_name)
                elif args[0] == "call":
                    code = self.__codeWriter.translate_call(args[1], args[2])
                elif args[0] == "function":
                    if args[1] == "Sys.init":
                        code = self.__codeWriter.translate_function(args[1],
                                                                    args[2],
                                                                    self.
                                                                    __file_name
                                                                    )
                    else:
                        code = self.__codeWriter.translate_function(args[1],
                                                                    args[2],
                                                                    self.
                                                                    __file_name
                                                                    )
                    cur_function = args[1]
                elif args[0] == "return":
                    code = self.__codeWriter.translate_return()
                elif args[0] == "label":
                    code = self.__codeWriter.translate_label(cur_function,
                                                             args[1])
                elif args[0] == "goto":
                    code = self.__codeWriter.translate_goto(cur_function,
                                                            args[1], False)
                elif args[0] == "if-goto":
                    code = self.__codeWriter.translate_goto(cur_function,
                                                            args[1], True)
                else:
                    code = self.__codeWriter.translate_arithmetic(args[0])

                self.__output.write(code)

            if self.__codeWriter.comparison_used():
                return True
            return False
