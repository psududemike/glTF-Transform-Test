import csv
from argparse import ArgumentParser

def getMeshSize(csv):
    size = 0
    row = next(csv)
    while row != None:
        if ''.join(row) == ' MESHES':
            next(csv) #drop dashes
            next(csv) #drop header
            row = next(csv) #first row of data
            while ''.join(row) != '':
                # print (row[-1])
                if int(row[-1]) > 0:
                    size += int(row[-1])
                row = next(csv)
        else:
            row = next(csv)
            continue
 
        # print ("Mesh Size is " + str(size))
        return size 


def getVertices(csv):
    nVerts = 0
    row = next(csv)
    while row != None:
        if ''.join(row) == ' MESHES':
            next(csv) #drop dashes
            next(csv) #drop header
            row = next(csv) #first row of data
            while ''.join(row) != '':
                # print (row[5])
                if int(row[5]) > 0:
                    nVerts += int(row[5])
                row = next(csv)
        else:
            row = next(csv)
            continue
 
        # print ("Number of Vertices is " + str(nVerts))
        return nVerts 

def getMeshes(csv):    
    meshes = 0
    row = next(csv)
    while row != None:
        if ''.join(row) == ' MESHES':
            next(csv) #drop dashes
            next(csv) #drop header
            row = next(csv) #first row of data
            while ''.join(row) != '':
                # print (row[5])
                if int(row[0]) > 0:
                    meshes = int(row[0])
                row = next(csv)
        else:
            row = next(csv)
            continue
        
        # adjust for index from 0
        meshes +=1
        # print ("Number of Meshes is " + str(meshes))
        return meshes 

def getMaterials(csv):
    print ("Output the number of materials")

def getTextureSize(csv):
    print ("Getting the texture size of this file")

def compare(original, optimized):
    if original != 0:
        print("Optimized file is " + str((optimized/original)*100) + "% of the original")
    else:
        print("Cannot compare these files")

parser = ArgumentParser()
parser.add_argument('inputData')
parser.add_argument('outputData')
args = parser.parse_args()

print ("Outputting a summary of key datapoints between " + args.inputData + " and " + args.outputData)
with open(args.inputData, newline='') as inputCSV:
    with open(args.outputData, newline="") as outputCSV:
        originalreader = csv.reader(inputCSV)
        optimizedreader = csv.reader(outputCSV)
        print ("Comparing Mesh Sizes")
        compare(getMeshSize(originalreader),getMeshSize(optimizedreader))

with open(args.inputData, newline='') as inputCSV:
    with open(args.outputData, newline="") as outputCSV:
        originalreader = csv.reader(inputCSV)
        optimizedreader = csv.reader(outputCSV)
        print ("Comparing Vertices")
        compare(getVertices(originalreader),getVertices(optimizedreader))

with open(args.inputData, newline='') as inputCSV:
    with open(args.outputData, newline="") as outputCSV:
        originalreader = csv.reader(inputCSV)
        optimizedreader = csv.reader(outputCSV)
        print ("Comparing Number of Meshes")
        compare(getMeshes(originalreader),getMeshes(optimizedreader))