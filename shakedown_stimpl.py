from stimpl.expression import *
from stimpl.runtime import *

if __name__=='__main__':
  program = Print(Assign(Variable("i"), StringLiteral("Hello, World")))
  programAdd = Print(Add(IntLiteral(5), IntLiteral(5)))
  programDivide1 = Print(Divide(IntLiteral(1), IntLiteral(2)))
  programDivide2 = Print(Divide(FloatingPointLiteral(1.0), FloatingPointLiteral(2.0)))
  run_stimpl(program)
  run_stimpl(programAdd)
  run_stimpl(programDivide1)
  run_stimpl(programDivide2)
