import json, sys, os
from multipledispatch import dispatch
#var = sys.argv[]

class RunService:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @dispatch(int, int)    
    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY
        return self.x + self.y
    @dispatch(int, int, int)
    def move(self, deltaX, deltaY, sumX):
        self.x = self.x + deltaX
        self.y = self.y + deltaY
        os.system("ls" " -l")
        return self.x + self.y + sumX
    



#nodeRun = os.system(var + " --help")
#print("{run}".format(run = var))

def parseValue(value, splitPrefix="."):
    data = value.split(splitPrefix)
    return data

# data = parseJsonValue(var)
# print(data[-1])

# if data[-1] == "dll":
#     os.system("pwd")


c1 = RunService(2, 4)
print(c1.move(2, 3))
print(c1.move(2, 3, 8))

#dotnet ${RUN_FILE} --urls=${URLS} --ENVIRONMENT=${ENV_EXTENSION} --'$STORAGE_ROOT'=${APP_STORAGE_ROOT} --pathToConf=${PATH_TO_CONF} --log:dir=${LOG_DIR} --log:name=${NAME_SERVICE} ${PARAMETERS}


if len(sys.argv) > 1:
    print(__name__)
    print(sys.argv[0])
    print(sys.argv[1])
    data = parseValue(sys.argv[1])
    print(data)


print(sys.argv)
