from copy import copy
from executivePass import ExecutivePass

def run_app():
     ron_pass = ExecutivePass.obtain('Ron')
     print("Ron obtained the executive pass")
     print(f"  Ron's pass: {ron_pass}")
     
     sal_pass = ExecutivePass.obtain('Sal')
     print("sal obtained the executive pass from Ron")
     print(f"  Sal's pass: {sal_pass}")
     print("Ron and Sal have the same pass:", ron_pass is sal_pass)
     print()
     
     sal_pass = ExecutivePass.delete()
     
     pat_pass = ExecutivePass.obtain('Pat')
     print("Successfully obtained a new executive pass for Pat")
     print(f"  Pat's pass: {pat_pass}")
     print()
     
     leo_pass = pat_pass
     print("Leo obtained the executive pass from Pat")
     print("Now Pat and Leo have the same pass:", pat_pass is leo_pass)
     print(f"  Pat's pass: {pat_pass}")
     print(f"  Leo's pass: {leo_pass}")
     
     print("Try to explicitly create a new executive pass")
     tim_pass = ExecutivePass()
     
     print()
     print("Try to make a copy the executive pass")
     bob_pass = copy(pat_pass)
     
if __name__ == "__main__":
     run_app()