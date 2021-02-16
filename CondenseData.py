
for x in range(194, 1420):
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
        ##Split string and remove everything but the list of annotations
        x = annotationLine.split('"prop_labels": [')
        annotationsSecondSplit = x[1].split('], "prop_offsets":')
        annotationsSecondSplit
        annotations = annotationsSecondSplit[0].split(", ")
        print(annotations)
        
        
    except:
        print("file doesnt exist")
    
    try:
        f = open(textFileName, "r")
        unformattedTextLine = f.readline()
        f.close()
        ##Removes '.' on last sentence to allow split to work properly
        unformattedTextLine = unformattedTextLine[:-1]
        print(unformattedTextLine)
        textLine = unformattedTextLine.replace('"', '""')
        
        ##split string into each sentence in the file
        splitText = textLine.split('. ')
        ## re-add '.' to the end of each sentence
        for index, text in enumerate(splitText):
	        splitText[index] = text + "."
        
        f = open("test.txt", "a")

        for index, lines in enumerate(splitText):
            if annotations[index] != '"testimony"' and annotations[index] != '"reference"':
                dataLine = '"' + splitText[index] + '",' + annotations[index] + "\n"
                print(dataLine)
                f.write(dataLine)
        f.close()
    except:
        print("file doesnt exist")
    
print("SCRIPT COMPLETE")
    
input()