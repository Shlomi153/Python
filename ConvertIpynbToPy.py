#Created by Shlomi Kiko
#Goal: This program converts Jupyter notebooks format ipynb to .py format so that it can be run automatically via a scheduler and executes it.
#Test Environment

import os
import subprocess
import fnmatch
import shutil
import glob
import json 


try:
    TestEnv = """
    ###########################################################################
    #Test environment:
    ###########################################################################
    """
    print(TestEnv)

    testSourceDir = r'C:\userdata\JupyterLab\Test_Spark'
    testSourceDirFiles = os.listdir(testSourceDir)

    testDir = r'C:\Python\TestDWH'
    filesToConvert = []

    #Filter out unecessary files and append relevant files to list - Test
    for file in testSourceDirFiles:
        if not fnmatch.fnmatch(file, '*checkpoint*') and not fnmatch.fnmatch(file, 'TestLogs') and not fnmatch.fnmatch(file, '*.py'):
            testSourceFilePath = testSourceDir + '\\' + file
            filesToConvert.append(testSourceFilePath)

    #Convert to py format so that we can run it for all relevant files - Test
    for file in filesToConvert:
        code = json.load(open(file))

        with open(f'{file}.py', 'w+') as pyFileTest:
            for cell in code['cells']:
                if cell['cell_type'] == 'code':
                    for line in cell['source']:
                        pyFileTest.write(line)
                    pyFileTest.write('\n')
                elif cell['cell_type'] == 'markdown':
                    pyFileTest.write('\n')
                    for line in cell['source']:
                        pyFileTest.write('#' + line)
                    pyFileTest.write('\n')

    print('Completed converting all the Test Notebooks into .Py format.\n')

    #Move .Py files to another location in order to avoid confusion - Test
    testSourcePyList = glob.glob(testSourceDir + '\\' + '*.py')
    testPyFilesPath = []

    for sourceFilePath in testSourcePyList:
        fileName = os.path.basename(sourceFilePath)
        testPyFilesPath.append(testTestDir + '\\' + fileName)
        shutil.move(sourceFilePath, testDir + '\\' + fileName)

    print('Files moved successfully for Test environment!\n')


    #Final confirmation
    finalConfirmation = """
    ###########################################################################
    #Files converted and moved successfully!
    ###########################################################################
    """
    print(finalConfirmation)

    execPyFiles = """
    #########################################################################
    #Execute .Py files
    #########################################################################
    """
    print(execPyFiles)
    
    try:
        for file in testPyFilesPath:
            subprocess.run(["python", file], check=True)
    except Exception as e:
        if e is None:
            raise Exception('Job Failed due to unknown exception')
        else:
            raise Exception('Job failed due to exception: ' + str(e))

    print('All Test files executed successfully!\n')

except Exception as e:
    if e is None:
        raise Exception('Job Failed due to unknown exception')
    else:
        raise Exception('Job failed due to exception: ' + str(e))
