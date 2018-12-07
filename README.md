Picturlate
=====

A cross platform app to help people learn to read and write in a foreign language. 
Written in **Javascript**, **CSS** using the *React Native*  framework for front end and *Flask* and **Python** for back end. Made at Hack Western 5.<br><br>
Users can open up the app, choose a language they're interested in learning, and then click a picture of any object in their surrounding. The app detects what object it is and translates it into the language chosen and also returns a list of other synonyms for the same object.
<br><br>
Uses [**Google Cloud Platform APIs**](https://cloud.google.com/), namely [*Cloud Vision*](https://cloud.google.com/vision/), [*Cloud Translation*](https://cloud.google.com/translate/), and [*Cloud Text-to-Speech*](https://cloud.google.com/text-to-speech/) to run on the back end. Cloud Vision helps detect the object, and translate API translates the results into the chosen language. <br>

Supported Languages are  
* French
* Russian
* Japanese
* Cantonese
* Hindi
* Spanish

As a next step, the users will be able to listen to the translated word in the chosen language by clicking on the word. This is done using the *text-to-speech API*
