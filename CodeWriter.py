ADD = "@SP\n" \
      "A=M-1\n" \
      "D=M\n" \
      "A=A-1\n" \
      "M=D+M\n" \
      "@SP\n" \
      "M=M-1\n"
ADD_LENGTH = 7

SUB = "@SP\n" \
      "A=M-1\n" \
      "D=M\n" \
      "A=A-1\n" \
      "M=M-D\n" \
      "@SP\n" \
      "M=M-1\n"
SUB_LENGTH = 7

NEG = "@SP\n" \
      "A=M-1\n" \
      "M=-M\n"
NEG_LENGTH = 3


COMPARISON_GT = "@*count*\n" \
             "D=A\n" \
             "@R13\n" \
             "M=D\n" \
             "@*mid_count*\n" \
             "D=A\n" \
             "@R14\n" \
             "M=D\n" \
             "@SP\n" \
             "M=M-1\n" \
             "A=M\n" \
             "D=M\n" \
             "@FIRST_POS_GT\n" \
             "D;JGT\n" \
             "@FIRST_NEG_GT\n" \
             "D;JLT\n" \
             "@SP\n" \
             "A=M\n" \
             "D=M\n" \
             "A=A-1\n" \
             "D=M-D\n" \
             "@IFTRUE\n" \
             "D;*cond1*\n" \
             "@IFNOTTRUE\n" \
             "D;*cond2*\n"

COMPARISON_LT = "@*count*\n" \
             "D=A\n" \
             "@R13\n" \
             "M=D\n" \
             "@*mid_count*\n" \
             "D=A\n" \
             "@R14\n" \
             "M=D\n" \
             "@SP\n" \
             "M=M-1\n" \
             "A=M\n" \
             "D=M\n" \
             "@FIRST_POS_LT\n" \
             "D;JGT\n" \
             "@FIRST_NEG_LT\n" \
             "D;JLT\n" \
             "@SP\n" \
             "A=M\n" \
             "D=M\n" \
             "A=A-1\n" \
             "D=M-D\n" \
             "@IFTRUE\n" \
             "D;*cond1*\n" \
             "@IFNOTTRUE\n" \
             "D;*cond2*\n"

COMPARISON_EQ = "@*count*\n" \
             "D=A\n" \
             "@R13\n" \
             "M=D\n" \
             "@SP\n" \
             "A=M-1\n" \
             "D=M\n" \
             "A=A-1\n" \
             "D=M-D\n" \
             "@SP\n" \
             "M=M-1\n" \
             "@IFTRUE\n" \
             "D;JEQ\n" \
             "@IFNOTTRUE\n" \
             "D;JNE\n"

COMPARISON_NE_LENGTH = 25
COMPARISON_EQ_LENGTH = 15
MID_LENGTH = 16
GT_COND1 = "JGT"
GT_COND2 = "JLE"
LT_COND1 = "JLT"
LT_COND2 = "JGE"

AND = "@SP\n" \
      "A=M-1\n" \
      "D=M\n" \
      "A=A-1\n" \
      "M=D&M\n" \
      "@SP\n" \
      "M=M-1\n"
AND_LENGTH = 7

OR = "@SP\n" \
      "A=M-1\n" \
      "D=M\n" \
      "A=A-1\n" \
      "M=D|M\n" \
      "@SP\n" \
      "M=M-1\n"
OR_LENGTH = 7

NOT = "@SP\n" \
      "A=M-1\n" \
      "M=!M\n"
NOT_LENGTH = 3

PUSH_CONSTANT = "@*value*\n" \
                "D=A\n" \
                "@SP\n" \
                "A=M\n" \
                "M=D\n" \
                "@SP\n" \
                "M=M+1\n"
PUSH_CONST_LENGTH = 7

PUSH_GLOBAL = "@*value*\n" \
              "D=A\n" \
              "@*segment*\n" \
              "A=A+D\n" \
              "D=M\n" \
              "@SP\n" \
              "A=M\n" \
              "M=D\n" \
              "@SP\n" \
              "M=M+1\n"

PUSH = "@*value*\n" \
       "D=A\n" \
       "@*segment*\n" \
       "A=M+D\n" \
       "D=M\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n"
PUSH_LENGTH = 10

PUSH_STATIC = "@*file_name*\n" \
              "D=M\n" \
              "@SP\n" \
              "A=M\n" \
              "M=D\n" \
              "@SP\n" \
              "M=M+1\n"
PUSH_STATIC_LENGTH = 7

POP = "@*value*\n" \
      "D=A\n" \
      "@*segment*\n" \
      "D=M+D\n" \
      "@R14\n" \
      "M=D\n" \
      "@SP\n" \
      "A=M-1\n" \
      "D=M\n" \
      "@R14\n" \
      "A=M\n" \
      "M=D\n" \
      "@SP\n" \
      "M=M-1\n"

POP_GLOBAL = "@*value*\n" \
             "D=A\n" \
             "@*segment*\n" \
             "D=A+D\n" \
             "@R14\n" \
             "M=D\n" \
             "@SP\n" \
             "A=M-1\n" \
             "D=M\n" \
             "@R14\n" \
             "A=M\n" \
             "M=D\n" \
             "@SP\n" \
             "M=M-1\n"
POP_LENGTH = 14

POP_STATIC = "@SP\n" \
             "A=M-1\n" \
             "D=M\n" \
             "@*file_name*\n" \
             "M=D\n" \
             "@SP\n" \
             "M=M-1\n"
POP_STATIC_LENGTH = 7

CALL = "@*count*\n" \
       "D=A\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n" \
       "@LCL\n" \
       "D=M\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n" \
       "@ARG\n" \
       "D=M\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n" \
       "@THIS\n" \
       "D=M\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n" \
       "@THAT\n" \
       "D=M\n" \
       "@SP\n" \
       "A=M\n" \
       "M=D\n" \
       "@SP\n" \
       "M=M+1\n" \
       "D=M\n" \
       "@5\n" \
       "D=D-A\n" \
       "@*nArgs*\n" \
       "D=D-A\n" \
       "@ARG\n" \
       "M=D\n" \
       "@SP\n" \
       "D=M\n" \
       "@LCL\n" \
       "M=D\n" \
       "@*target*\n" \
       "0;JMP\n"
CALL_LENGTH = 48

GOTO = "@*target*\n" \
       "0;JMP\n"
GOTO_LENGTH = 2

IF_GOTO = "@SP\n" \
          "M=M-1\n" \
          "A=M\n" \
          "D=M\n" \
          "@*target*\n" \
          "D;JNE\n"
IF_GOTO_LENGTH = 6

FUNCTION = "(*function_name*)\n"

RETURN = "@LCL\n" \
         "D=M\n" \
         "@endFrame\n" \
         "M=D\n" \
         "@5\n" \
         "D=A\n" \
         "@endFrame\n" \
         "D=M-D\n" \
         "A=D\n" \
         "D=M\n" \
         "@retAddr\n" \
         "M=D\n" \
         "@SP\n" \
         "A=M-1\n" \
         "D=M\n" \
         "@ARG\n" \
         "A=M\n" \
         "M=D\n" \
         "D=A+1\n" \
         "@SP\n" \
         "M=D\n" \
         "@endFrame\n" \
         "M=M-1\n" \
         "A=M\n" \
         "D=M\n" \
         "@THAT\n" \
         "M=D\n" \
         "@endFrame\n" \
         "M=M-1\n" \
         "A=M\n" \
         "D=M\n" \
         "@THIS\n" \
         "M=D\n" \
         "@endFrame\n" \
         "M=M-1\n" \
         "A=M\n" \
         "D=M\n" \
         "@ARG\n" \
         "M=D\n" \
         "@endFrame\n" \
         "M=M-1\n" \
         "A=M\n" \
         "D=M\n" \
         "@LCL\n" \
         "M=D\n" \
         "@retAddr\n" \
         "A=M\n" \
         "0;JMP\n"
RETURN_LENGTH = 48


class CodeWriter:
    """
    A class defining the VM to Assembly translator
    """
    def __init__(self):
        """
        Initialize the CodeWriter
        """
        self.__counter = 4
        self.__mid_count = 0
        self.__comparison_used = False

    def set_pc(self, value):
        """
        Set the program counter to the given value
        :param value: the value to set
        """
        self.__counter = value

    def comparison_used(self):
        """
        Check if comparison logic was used.
        :return: True if so, False otherwise
        """
        return self.__comparison_used

    def translate_arithmetic(self, operation):
        """
        Translate VM code of arithmetic operations
        :param operation: The operation to translate
        :return: The corresponding translated Assembly code
        """
        if operation == "add":
            self.__counter += ADD_LENGTH
            return ADD
        elif operation == "sub":
            self.__counter += SUB_LENGTH
            return SUB
        elif operation == "neg":
            self.__counter += NEG_LENGTH
            return NEG
        elif operation == "eq":
            self.__counter += COMPARISON_EQ_LENGTH
            eq = COMPARISON_EQ
            eq = eq.replace("*count*", str(self.__counter))
            self.__comparison_used = True
            return eq
        elif operation == "gt":
            self.__mid_count = self.__counter + MID_LENGTH
            self.__counter += COMPARISON_NE_LENGTH
            gt = COMPARISON_GT
            gt = gt.replace("*count*", str(self.__counter))
            gt = gt.replace("*mid_count*", str(self.__mid_count))
            gt = gt.replace("*cond1*", GT_COND1)
            gt = gt.replace("*cond2*", GT_COND2)
            self.__comparison_used = True
            return gt
        elif operation == "lt":
            self.__mid_count = self.__counter + MID_LENGTH
            self.__counter += COMPARISON_NE_LENGTH
            lt = COMPARISON_LT
            lt = lt.replace("*count*", str(self.__counter))
            lt = lt.replace("*mid_count*", str(self.__mid_count))
            lt = lt.replace("*cond1*", LT_COND1)
            lt = lt.replace("*cond2*", LT_COND2)
            self.__comparison_used = True
            return lt
        elif operation == "and":
            self.__counter += AND_LENGTH
            return AND
        elif operation == "or":
            self.__counter += OR_LENGTH
            return OR
        else:
            self.__counter += NOT_LENGTH
            return NOT

    def translate_push(self, segment, value, file_name):
        """
        Translate VM code of push command
        :param segment: The memory segment of the command
        :param value: The index offset of the wanted value
        :param file_name: The current file's name
        :return: The corresponding translated Assembly code
        """
        file_name = file_name.split(".")[0]
        if segment == "constant":
            self.__counter += PUSH_CONST_LENGTH
            const = PUSH_CONSTANT
            const = const.replace("*value*", str(value))
            return const
        elif segment == "static":
            self.__counter += PUSH_STATIC_LENGTH
            push = PUSH_STATIC
            push = push.replace("*file_name*", file_name+"."+str(value))
            return push
        else:
            self.__counter += PUSH_LENGTH
            if segment == "local":
                push = PUSH
                push = push.replace("*segment*", "LCL")
            elif segment == "argument":
                push = PUSH
                push = push.replace("*segment*", "ARG")
            elif segment == "temp":
                push = PUSH_GLOBAL
                push = push.replace("*segment*", "R5")
            elif segment == "pointer":
                push = PUSH_GLOBAL
                push = push.replace("*segment*", "R3")
            else:
                push = PUSH
                push = push.replace("*segment*", segment.upper())
            push = push.replace("*value*", str(value))
            return push

    def translate_pop(self, segment, value, file_name):
        """
        Translate VM code of pop command
        :param segment: The memory segment of the command
        :param value: The index offset of the wanted value's destination
        :param file_name: The current file's name
        :return: The corresponding translated Assembly code
        """
        file_name = file_name.split(".")[0]
        if segment == "static":
            self.__counter += POP_STATIC_LENGTH
            pop = POP_STATIC
            pop = pop.replace("*file_name*", file_name+"."+str(value))
            return pop
        self.__counter += POP_LENGTH
        if segment == "local":
            pop = POP
            pop = pop.replace("*segment*", "LCL")
        elif segment == "argument":
            pop = POP
            pop = pop.replace("*segment*", "ARG")
        elif segment == "temp":
            pop = POP_GLOBAL
            pop = pop.replace("*segment*", "R5")
        elif segment == "pointer":
            pop = POP_GLOBAL
            pop = pop.replace("*segment*", "R3")
        else:
            pop = POP
            pop = pop.replace("*segment*", segment.upper())
        pop = pop.replace("*value*", str(value))
        return pop

    def translate_call(self, function_name, n_args):
        self.__counter += CALL_LENGTH
        code = CALL.replace("*count*", str(self.__counter))
        code = code.replace("*nArgs*", str(n_args))
        code = code.replace("*target*", str(function_name))
        return code

    def translate_function(self, function_name, n_vars, file_name):
        code = FUNCTION.replace("*function_name*", str(function_name))
        for i in range(int(n_vars)):
            code += self.translate_push("constant", 0, file_name)
        return code

    def translate_return(self):
        self.__counter += RETURN_LENGTH
        return RETURN

    def translate_goto(self, function_name, label_name, condition):
        if condition:
            self.__counter += IF_GOTO_LENGTH
            code = IF_GOTO.replace("*target*", str(function_name) + "$" +
                                   str(label_name))
        else:
            self.__counter += GOTO_LENGTH
            code = GOTO.replace("*target*", str(function_name) + "$" + str(
                label_name))
        return code

    def translate_label(self, function_name, label_name):
        code = "(" + str(function_name) + "$" + str(label_name) + ")\n"
        return code
