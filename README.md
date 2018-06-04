# Silliness
A collection of random things that I found fun to do

A list follows of what things there are here.

1) A base64 to base10 converter that grew into a fun encoding scheme. You can use this to encode a string as a huge int. Fun!


Explanations of each.

Base64 to Base10 converter

Have you ever wanted to know how big a base 64 number is? Have you ever wanted to encode a base 64 number in plain old base 10? Have you ever wondered just how big of a number "C3P0" of "R2D2" is in base 64? Neither had I, but you can now satisfy your endless curiousity!

This small project grew out of my co-worker saying "I wonder how big of a number BB8 is...". She promptly started trying to calculate it out by hand, making me cry inside and decide she needed a program for it. A few minutes later, we were able to turn base64 into base 10, base 10 into base 64, and SOMEONE had the bright idea to make a base64 encoded string into a base10 number. Once that was completed, the next step was ineviatable: Caeser Ciphering the base64 encoded string, AND THEN turning it into a decimal number. Surprisingly, this worked without incident.

The base64 to base10 encoder can do the following:
  convert base64 into a base10 int  
  convert a base10 int into any base <= base64 (ie: base42)  
  convert your favorite StarWars droid names into reasonable base10  
  convert a string into a base64 encoded string, which is then turned into base 10  
  convert a base10 int into a readable string (provided it IS a readable string)  
  caeser cipher the base64 encoded text before turning it into a base10 int  
  caeser cipher the base10 after encoding to base10 has completed  

If you thought anything on this was fun to use, or you'd like to use this in a project, please be sure to give me the credit for my work. If you'd like to donate, that also wouldn't be remiss.

Bitcoin: 1F6SExymCmQWx3r6Bjr5uYjinHqdksWMKQ
Defcoin: DG2KCYZxy8s6Navqe7rQA5N11WPKdeJ9dH
