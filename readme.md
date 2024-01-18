# Named Entity Recognition 


# Introduction 

This projects helps to identify and classify the named entities present in the given sentence using CRF algorithm. 

example: ViratKohli is great cricketer from India <br><br> 
The above sentence contains two entities: <br> 
ViratKohli - person <br> 
India - geolocation <br> 

Named entities gives valuable information about the sentence.

--- 


# Requirements 

python <br>
numpy <br>
pandas <br>
nltk <br>
scikit-learn <br>
sklearn-crfsuite <br>
flask <br>

---


# Named Entity API Module 

**/named-entity** 
Request this url with **post** method, where the sentence is sent through body of this request. <br><br>
This request returns named entities present in the given sentence.

**Input json format for sending sentence** 
```
{
    "sentence": "ViratKohli is great cricketer from India"
}
```





