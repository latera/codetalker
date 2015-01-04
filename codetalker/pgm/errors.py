#!/usr/bin/env python


class CodeTalkerException(Exception):
    pass


class LineError(CodeTalkerException):
    def __init__(self, text, lineno, charno):
        super().__init__(text + ' at (%d, %d)' % (lineno, charno))

        self.lineno = lineno
        self.charno = charno


class ParseError(LineError):
    pass


class TokenError(CodeTalkerException):
    def __init__(self, msg, text, lineno, charno):
        tease = ''
        lines = text.splitlines()

        if lineno-1 < len(lines):
            tease = lines[lineno-1][charno-1:charno+30]

        super().__init__(msg + ' at (%d, %d) \'%s\'' %
                         (lineno, charno, tease.encode('utf-8')))

        self.lineno = lineno
        self.charno = charno


class AstError(CodeTalkerException):
    pass


class RuleError(CodeTalkerException):
    pass

# vim: et sw=4 sts=4
