# VisualReconition-IBM WATSON
==============================
This project is from Gp 2.2, consists of creating an app using the OPENCV API, in conjunction with the WATSON-VISUAL RECOGNITION API.

###Professor:
-  [Rodrigo Barba](mailto:lrbarba@utpl.edu.ec)

###Student:
-  [Charlie Cárdenas](cacardenas7@utpl.edu.ec)

##FACE DETECTION - OPENCV

A face recognition algorithm is used so that each shot taken is cut to a width and height of 380px, as it is mandatory for the use of API VISUAL RECOGNITION.

##VISUAL RECOGNITION - IBM WATSON

The IBM Watson™ Visual Recognition service uses deep learning algorithms to identify scenes, objects, and celebrity faces in images you upload to the service. You can create and train a custom classifier to identify subjects that suit your needs.

Descriptions of Python classes referred to in this reference are available in the Python documentation for the Watson Developer Cloud Python SDK.

####Installation Visual Recognition - Python
-------------------
	•pip install --upgrade watson-developer-cloud
	
####Requirements
-------------------
	•OpenCV
	•Anaconda v 4.2.0 for Windows
####Running SaCI
-------------------
	- python face.py

When you execute this line, it will show a json with the obtained data
![Jackie Chan](http://vignette2.wikia.nocookie.net/doblaje/images/e/ed/Jackie-chan.jpg/revision/latest?cb=20120718011439&path-prefix=es)
-------------------------
        "faces": [
        {
          "gender": {
            "gender": "MALE",
            "score": 0.993307
          },
          "age": {
            "max": 64,
            "score": 0.432146,
            "min": 55
          },
          "identity": {
            "score": 0.993307,
            "name": "Jackie Chan",
            "type_hierarchy": "/people/celebrities/stars/jackie chan"
          },
          "face_location": {
            "width": 178,
            "top": 72,
            "left": 111,
            "height": 213
          }
        }
      ]
    }
![Jefferson Perez](http://cdnb.20m.es/quefuede/files/2013/01/jeffersonperez.jpg)
-------------------------      
	 "faces": [
        {
          "gender": {
            "gender": "MALE",
            "score": 0.993307
          },
          "age": {
            "max": 44,
            "score": 0.490723,
            "min": 35
          },
          "identity": {
            "score": 0.993307,
            "name": "Jefferson P\u00e9rez",
            "type_hierarchy": "/counties/jefferson/jefferson p\u00e9rez"
          },
          "face_location": {
            "width": 126,
            "top": 55,
            "left": 141,
            "height": 131
          }
        }
      ]
 
In the case when running our line of code with 2 celebrities, it throws us correctly.
Now we will use a Teacher of La Utpl

![Rodigo Barba](https://github.com/VAUTPL/VisualReconition/blob/master/rodrigobabatest12%20.jpg)
-------------------------      
	 "images": [
        {
          "classifiers": [
            {
	    	"classes": [
	    		{
			 "class": "Rodrigo_Barba"
			 "score":  0.998888
			},
		"classes": [
	    		{
			 "class": "Pablo_Torres"
			 "score":  0.335421
			},
		"classes": [
	    		{
			 "class": "Guido_Riofrio"
			 "score":  0.145565
			},		
                ]
 
	
