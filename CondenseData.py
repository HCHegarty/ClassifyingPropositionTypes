
for x in range(0, 1420):
    ##add the 0s in front of the IDs in the dataset
    rightID = str(x)
    if len(rightID) == 3:
        iD = "00" + rightID
    else:
        iD = "0" + rightID
    ##get filenames of both the text file and the annotation file
    annotateFileName = iD + ".ann.json"
    textFileName = iD + ".txt"
    
    print(iD)

    ##Open and read annotation file into string
    try:
    
        f = open(annotateFileName, "r")
        annotationLine = f.readline()
        f.close()
        ##Split string and remove everything but the list of propositions and offsets of where the propositions are in the comment
        ##trims all before proposition list
        x = annotationLine.split('"prop_labels": [')
        ##splits propositions and offsets and trims middle unnecessary parts
        annotationsSecondSplit = x[1].split('], "prop_offsets": [[')
        ##trims all code after after offsets
        annotationThirdSplit = annotationsSecondSplit[1].split(']], "reas')
        ## creates list of propositions
        annotations = annotationsSecondSplit[0].split(", ")
        ## creates list of offsets in the format "X, X"
        propOffsets = annotationThirdSplit[0].split("], [")
        #print(propOffsets)
    
        
    
        f = open(textFileName, "r")
        wholeText = f.readlines()
        wallOfText = wholeText[0]
        f.close()

        f = open("test.txt", "a")

        #match offsets to sentences in text
        for index, offsets in enumerate(propOffsets):
            print(offsets)
            offset = offsets.split(', ')
            a = int(offset[0])
            b = int(offset[1])
            if a!=0:
                a=a+1
            propText = wallOfText[a:b]
            #print(propText)
            dataLine = '"' + propText+ '",' + annotations[index] + "\n"
            if annotations[index] != '"testimony"' and annotations[index] != '"reference"':                     
                print(dataLine)
                f.write(dataLine)
        f.close()

    except:
        print("file doesnt exist")

print("SCRIPT COMPLETE")
    
input()

