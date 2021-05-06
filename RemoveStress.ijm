macro "RemoveStress"{
    input = File.openDialog("Choose the file to Open: ");
    inputString = File.openAsString(input);
    values = split(inputString, ",");
    for(i = 0; i < values.length; i++){
        Stack.setSlice(values[i]);
        run("Delete Slice");
    }
}