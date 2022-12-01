import os


class Test():
    

    def create_txt(var, cont,n):
        file = open(f"var_trans.txt", "w")
        file.write(f"{var}" + os.linesep)
        file.write(f"{cont}" + os.linesep)
        file.write(f"{n}" + os.linesep)
        file.close()