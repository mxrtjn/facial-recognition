import os, sys

dataSetPath = os.getcwd()+'/dataSet2'

#print("The dir is: %s"%os.listdir(dataSetPath))
counter = 0
counterFile = 0
for fold in os.listdir(dataSetPath):
    if not os.path.isdir(os.path.join(dataSetPath, fold)):#if not is a folder
        continue
    counter = counter + 1
    counterFile = 0
    #print(fold)
    for file in os.listdir(os.path.join(dataSetPath, fold)):
        if not os.path.isdir(os.path.join(dataSetPath, fold, file)):
            counterFile = counterFile + 1
            os.rename(os.path.join(dataSetPath, fold, file), os.path.join(dataSetPath, fold, str(counter) + '.' + str(counterFile) + '-' + fold + '.jpg'))
    os.rename(os.path.join(dataSetPath, fold), os.path.join(dataSetPath, str(counter) + '-' + fold)) #renaming folder
    #        print('   ' + file)
    #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    #if counter > 1:
    #    break



#os.rename(dataSetPath+'/Aaron_Eckhart',dataSetPath+'/1.Aaron_Eckhart')