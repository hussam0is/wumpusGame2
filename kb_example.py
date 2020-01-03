from logic import *

wumpus_kb = PropKB()

#P11, P12, P21, P22, P31, B11, B21 = expr('P11, P12, P21, P22, P31, B11, B21')
wumpus_kb.tell(expr('~P11'))
wumpus_kb.tell(expr('B11  <=>  (P12 | P21)'))
wumpus_kb.tell(expr('B21  <=>  (P11 | P22 | P31)'))
wumpus_kb.tell(expr('~B11'))
wumpus_kb.tell(expr('B21'))

print('Test 1: ', wumpus_kb.ask_if_true(expr('B11')) == False)
print('Test 2: ', wumpus_kb.ask_if_true(expr('B21')) == True)
print('A satisfiable interpretation to the Wumpus knowledge base is:\n',
      dpll_satisfiable(Expr('&', *wumpus_kb.clauses)))

