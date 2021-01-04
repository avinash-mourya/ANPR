import base64
import requests
import json
import re
# import easyocr
import tesserocr
# from PIL import Image
# url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDnBUSdTtkhhHmCbolbH5fR-_m4VA0X0Cc'

# AIzaSyDrfUf8BMPMRcHQzAi1h4MZ56pGPeIeNMs
def detect_license_plate():
    # img_base64 = base64.b64encode(imagePath)
    # headers = {'content-type': 'application/json'}
    #
    # data = """{
    #   "requests": [
    #     {
    #       "image": {
    #                "content": '""" + encodedImage[:-1] + """'
    #
    #                 },
    #
    #       "features": [
    #         {
    #           "type": "TEXT_DETECTION"
    #         }
    #       ]
    #     }
    #   ]
    # }"""
    # r = requests.post(url, headers=headers, data=data)
    # result = json.loads(r.text)
    # print(result)
    # try:
    #     result = result['responses'][0]['textAnnotations'][0]['description']
    # except Exception as e:
    #     return r

    #using esayocr
    # reader = easyocr.Reader(['en'])  # need to run only once to load model into memory
    # result = reader.readtext('images/croppedImage.jpg')
    # print(result)

    #use tesseract-ocr
    # print(tesserocr.tesseract_version())  # print tesseract-ocr version
    # print(tesserocr.get_languages())  # prints tessdata path and list of available languages
    # image = Image.open('images/croppedImage.jpg')
    # result = tesserocr.image_to_text(image)
    # print(result)  # print ocr text from image
    # or
    result = tesserocr.file_to_text('images/croppedImage.jpg')
    print(result)
    result = result
    result = result.replace('\n', '').replace(' ', '')
    result =re.sub('\W+','', result)
    mystates = ['AP','AR','AS','BR','CG','GA','GJ','HR' ,'HP' ,'JK','JH','KA','KL','MP','MH','MN','ML','MZ','NL' ,'OD','PB' ,'RJ','SK','TN','TS','TR','UA','UK','UP','WB','AN','CH','DN','DD','DL' ,'LD','PY']
    
    if(len(result) > 0):
        #res=re.findall("\s*[AP,AR,AS,BR,CG,GA,GJ,HR,HP,JK,JH,KA,KL,MP,MH,MN,ML,MZ,NL,OD,PB,RJ,SK,TN,TS,TR,UA,UK,UP,WB,AN,CH,DN,DD,DL,LD,PY]{2}\s*[0-9]{1,2}\s*[A-Z]{1,2}\s*[0-9]{1,4}\s*]?",cleanString)    
        for word in mystates:
            if(word in result):
                res = re.findall(word + "[0-9]{1,2}\s*[A-Z]{1,2}\s*[0-9]{1,4}\s*]?", result)
                if(len(res) >0):
                    return(res[0])
    return result
