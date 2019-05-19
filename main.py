import sys
import os
import platform
from Parser import Parser
from CodeWriter import *

FIRST_POS_GT = "(FIRST_POS_GT)\n" \
               "@SP\n" \
               "A=M-1\n" \
               "D=M\n" \
               "@R14\n" \
               "A=M\n" \
               "D;JGE\n" \
               "@IFNOTTRUE\n" \
               "D;JLT\n"

FIRST_NEG_GT = "(FIRST_NEG_GT)\n" \
               "@SP\n" \
               "A=M-1\n" \
               "D=M\n" \
               "@R14\n" \
               "A=M\n" \
               "D;JLE\n" \
               "@IFTRUE\n" \
               "D;JGT\n"

FIRST_POS_LT = "(FIRST_POS_LT)\n" \
               "@SP\n" \
               "A=M-1\n" \
               "D=M\n" \
               "@R14\n" \
               "A=M\n" \
               "D;JGE\n" \
               "@IFTRUE\n" \
               "D;JLT\n"

FIRST_NEG_LT = "(FIRST_NEG_LT)\n" \
               "@SP\n" \
               "A=M-1\n" \
               "D=M\n" \
               "@R14\n" \
               "A=M\n" \
               "D;JLE\n" \
               "@IFNOTTRUE\n" \
               "D;JGT\n"

IF = "(IFTRUE)\n" \
     "@SP\n" \
     "A=M-1\n" \
     "M=-1\n" \
     "@R13\n" \
     "A=M\n" \
     "0;JMP\n" \
     "(IFNOTTRUE)\n" \
     "@SP\n" \
     "A=M-1\n" \
     "M=0\n" \
     "@R13\n" \
     "A=M\n" \
     "0;JMP\n"

JMP_END = "@END\n" \
          "0;JMP\n"

INIT = "@256\n" \
       "D=A\n" \
       "@SP\n" \
       "M=D\n"

END = "(END)\n"

WIN_PATH_DEL = "\\"  # Delimiter in Windows based directory path
OTHER_PATH_DEL = "/"  # Delimiter in Other OS's directory path
ASM_SUFFIX = ".asm"
SUFFIX_DELIMITER = "."
APPROVED_SUFFIX = ".vm"


def process_file(path, output_file, coder, fn):
    """
    Process the current file for parsing and translation.
    :param path: The current file's path
    :param output_file: The output file to write to
    :param coder: The CodeWriter "object"
    :param fn: The file's name
    :return: True if a code for comparison logic was found, False otherwise
    """
    file = Parser(path, output_file, coder, fn)
    comparison_used = file.parse_file()
    return comparison_used


if __name__ == '__main__':
    comp_used = False
    output = 0
    code_Writer = CodeWriter()
    for i in range(1, len(sys.argv)):

        if os.path.isdir(sys.argv[i]):  # It's a directory
            code_Writer.set_pc(4)  # reset the PC
            # Create the output file
            if platform.system() == "Windows":
                file_name = sys.argv[i] + WIN_PATH_DEL + \
                            os.path.basename(sys.argv[i])
            else:
                file_name = sys.argv[i] + OTHER_PATH_DEL + \
                            os.path.basename(sys.argv[i])
            file_name += ASM_SUFFIX
            output = open(file_name, "a+")

            # Initialize
            init = INIT + code_Writer.translate_call("Sys.init", 0)
            output.write(init)

            for file_name in os.listdir(sys.argv[i]):  # for each file
                if file_name.endswith(APPROVED_SUFFIX):
                    # Cross platform support:
                    if platform.system() == "Windows":
                        comp_used = process_file(sys.argv[i] + WIN_PATH_DEL +
                                                 file_name, output,
                                                 code_Writer, file_name)
                    else:
                        comp_used = process_file(sys.argv[i] + OTHER_PATH_DEL
                                                 + file_name, output,
                                                 code_Writer, file_name)

        elif os.path.isfile(sys.argv[i]):  # It's a file
            code_Writer.set_pc(0)  # reset the PC
            # Create the output file
            file_path = sys.argv[i].rsplit(SUFFIX_DELIMITER, 1)[0]
            file_path += ASM_SUFFIX
            output = open(file_path, "a+")

            # Initialize
            # init = INIT + code_Writer.translate_call("Sys.init", 0)
            # output.write(init)

            file_name = os.path.basename(sys.argv[i])
            file_name = file_name.rsplit(SUFFIX_DELIMITER, 1)[0]

            comp_used = process_file(sys.argv[i], output, code_Writer,
                                     file_name)

        if comp_used:  # add these lines of code if comparison logic was used
            output.write(JMP_END)
            output.write(FIRST_POS_GT)
            output.write(FIRST_NEG_GT)
            output.write(FIRST_POS_LT)
            output.write(FIRST_NEG_LT)
            output.write(IF)
            output.write(END)
