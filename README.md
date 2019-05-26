#         Selenium_buyme.co.il
Automating “BuyMe” website: 
System description 
A site that offers an immediate and innovative service for purchasing and sending gift  voucher by email or text message.  
The “BuyMe” system is directly connected to hundreds of stores and dozens of chains throughout the country. 
Everywhere and anytime you can browse the site, choose a store, load an online voucher (Gift Card) and send to someone dear. 
 
Project goal: 
“BuyMe” website sanity test.  
 
Solution architecture:  
General: 
Development platform: Automation will be developed in Python. 
IDE: PyCharm. 
Third-Party usage: Selenium web-driver. 
Distribution type: Private. 
Networking type: None (offline). 
Website address: https://buyme.co.il/   
 
Guidelines:  
1. Use the correct way to wait for elements. 2. Choose “safe” locators as much as possible. 3. Website URL will be dynamic and stored inside an external text file which will be sent with the project.  4. Each action will have documentation. 5. All variables need to have valuable names 
Steps:  A. Registration screen 
 
 
 
B. Home Screen 
 
 
C. Choose business screen 
D. Sender & Receiver information screen 
Pick a Buisness
Type a price
Press radio button "למישהו אחר"
Enter receiver name
Enter sender name
Enter a blessing
Upload a picture
Pick the event (Wedding/birthday)
Press radio button "מיד אחרי התשלום"
Pick Email / SMS option
Enter address/ number and press save
submit
Enter the website
Press on button " כניסה  |הרשמה"
Press on button "להרשמה"
Enter first name
Enter email address
Once logged in
Pick a price point
Pick the area
Pick category
Press the search button
Enter password
Enter password again
Press on  radio button "אני מסכים"
Press button  הרשמה" ... "
Extras:   
Loading screen-      Print the size (height & width) of one of the loading dots:   
   
   Home screen-   1. Press on “כניסה” button.   2. Don’t enter credentials   3. Press on “BUYME -כניסה ל” button.   4. Validate error messages (red text)   
 
Choose gift screen   Scroll to the bottom of the screen and take a screenshot.      
       
 
 
  
    
    
Sender & Receiver information screen   A.    
Validate the text color of the step name (   )  למי לשלוח
   
B.    After filling up all the information, gift preview screen on the left side will contain the new information.      Validate the below information (compare the text fields with what you had enter to preview text fields):   1. Sender name   2. Receiver name   3. Blessing      
   
   
