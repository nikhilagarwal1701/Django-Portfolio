function getDownloadURL(url){
    mandatoryPart = "https://drive.google.com/uc?export=view&id="
    variablePart = url.substirng(31)
    console.log(mandatoryPart + variablePart);
    return mandatoryPart + variablePart
}