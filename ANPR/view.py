from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from encode_decode.img_enc_dec import encodeImageIntoBase64,decodeImage
from number_plate_detector.getNumberPlateVals import detect_license_plate
from number_plate_detector.predict_images import DetectVehicleNumberPlate
import json
inputFileName = "inputImage.jpg"
imagePath = "images/" + inputFileName
image_display = True
pred_stagesArgVal = 2
croppedImagepath = "images/croppedImage.jpg"


class ClientApp:
    def __init__(self):
        # modelArg = "datasets/experiment_faster_rcnn/2018_08_02/exported_model/frozen_inference_graph.pb"
        self.modelArg = "datasets/experiment_ssd/2018_07_25_14-00/exported_model/frozen_inference_graph.pb"
        self.labelsArg = "datasets/records/classes.pbtxt"
        self.num_classesArg = 37
        self.min_confidenceArg = 0.5
        # filepath = "autoPartsMapping/partNumbers.xlsx"
        # self.regPartDetailsObj = ReadPartDetails(filepath)
        self.numberPlateObj = DetectVehicleNumberPlate()

def getPrediction(inpImage):
    decodeImage(inpImage, imagePath)
    try:
        labelledImage = clApp.numberPlateObj.predictImages(imagePath, pred_stagesArgVal,
                                                           croppedImagepath, clApp.numberPlateObj)
        if labelledImage is not None:
            encodedCroppedImageStr = encodeImageIntoBase64(croppedImagepath)
            ik = encodedCroppedImageStr.decode("utf-8")
            numberPlateVal = detect_license_plate()
            if len(numberPlateVal) == 10:
                responseDict = {"base64Image": ik, "numberPlateVal": numberPlateVal}
                return responseDict
            else:
                responseDict = {"base64Image": "Unknown", "numberPlateVal": "Unknown"}
                return responseDict
        else:
            responseDict = {"base64Image": "Unknown", "numberPlateVal": "Unknown"}
            return responseDict
    except Exception as e:
        print(e)
    responseDict = {"base64Image": "Unknown", "numberPlateVal": "Unknown"}
    return responseDict

clApp = ClientApp()
def index(request):
    return render(request,"index.html")

@csrf_exempt
def detection(request):
    if request.is_ajax():
        image = request.POST["imgData"]
        result = getPrediction(image)
        print(result)
        result=json.dumps(result,ensure_ascii=False)
        return HttpResponse(result,content_type="application/json")

