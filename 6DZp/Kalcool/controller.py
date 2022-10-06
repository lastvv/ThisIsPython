from unittest import result
import view
import modul_summ
def knopki():
    a = view.enter()
    b = view.enter()
    result = modul_summ.sum(a,b)
   # view.view(result)
    return (result)
print(knopki())