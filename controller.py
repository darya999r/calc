import module_racio as rac
import module_complex as comp
import logger as log

def separator(expression):
    if ("i" in expression) or ("j" in expression):
        res = comp.count_opz(comp.opz(comp.preparation(expression)))
        print(f'Выражение {expression} = {res}')
        log.datetime(expression, res)
    else:
        res = rac.count_opz(rac.opz(rac.preparation(expression)))
        print(f'Выражение {expression} = {res}')
        log.datetime(expression, res)