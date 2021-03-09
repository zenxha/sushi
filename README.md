![Sushi](https://cdn.discordapp.com/attachments/784178874303905792/812833268171800596/unknown.png)
# Sushi
Group Project for tri2!
### Links
- [Project Board](https://github.com/zenxha/sushi/projects/4)
- [Runtime Link](http://rubinfamily.dyndns.org:5000/)
- [Easter Egg Link (Use mort as username)](http://rubinfamily.dyndns.org:5000/upload)

### Collaborators
- Allen Xu ID: #72947445
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: 51984972

### Navigating our website
- Once on the website, use the navbar in the top right to check out each section
- If you do not have an account, go to signup to make an account then login via sign in
- In order to upload a review, navigate to upload.html and fill out the form, then hit upload
- To get to our easteregg section, go to sign in and type in mort as the username, then hit submit. There you can view our IAM statements, crossover report, and project plan (Gif below to show process)
- ![](https://user-images.githubusercontent.com/72947445/110531068-f90e9480-80cf-11eb-9d69-fcc691d8c900.gif)
- To use our API, go to the API section and use the url given, replacing {ID} with the id of the review you want to get

### Technicals

- Front End Aspect
  - Visuals: 
    - [Displaying quotes from an API onto our homepage](https://github.com/zenxha/sushi/blob/cd2b15bcf0891ea65179d5313b9b589c463e3676/views.py#L31-L38)![](https://user-images.githubusercontent.com/72947445/110418753-eef78200-804c-11eb-8514-9a8a3fa2577a.gif)
    - [Animated home page with CSS, used a gradient to make text easily visable.](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/base2.html#L38-L163)(Can be viewed in video above)
    - Created [background](https://github.com/zenxha/sushi/blob/8330192e9146bac29500ffc3948b079e174d306b/templates/easteregg/base.html#L29-L34) for easter egg section of the website ![](https://user-images.githubusercontent.com/72947445/110418664-d2f3e080-804c-11eb-9fa1-32645d2bcb5d.gif)
 
  - HTML:
    - Upload: Created upload page that allows users to write a review, upload an image, and select their satisfaction value on their sushi. [Code](https://github.com/zenxha/sushi/blob/6c1feeb6993cf5d9f5edc72b877c0142d69d025a/templates/homesite/loginv2.html#L152-L174)
    - Browse: [Display user uploaded information from upload.html onto browse.html](https://github.com/zenxha/sushi/blob/6c1feeb6993cf5d9f5edc72b877c0142d69d025a/templates/homesite/browse.html#L7-L26) (Utilized Trish's upload form from her tech talk)
    - IAM: Used a table like display to [display each member's IAM statements](https://github.com/zenxha/sushi/blob/8330192e9146bac29500ffc3948b079e174d306b/templates/easteregg/IAM.html#L11-L73)
    - Login/Signup: Pulls user inputted data from [login](https://github.com/zenxha/sushi/blob/main/templates/homesite/login.html#L170-L177)/[signup](https://github.com/zenxha/sushi/blob/9a807f64d1a07963446ea947469ef677274a1975/templates/homesite/signup.html#L171-L179) to check with database for account (Also used elements of Trish's tech talk to create the form)

- Back End Aspect
  - Routes: 
    - [Easteregg path where you need mort as the username](https://github.com/zenxha/sushi/blob/358412ff2e6057e202f4d1b2e697487fca2fd6a9/views.py#L63-L71)
    - [Browse page](https://github.com/zenxha/sushi/blob/358412ff2e6057e202f4d1b2e697487fca2fd6a9/views.py#L47-L60) that takes info from upload and displays it on the browse page.
    - [Upload page](https://github.com/zenxha/sushi/blob/cec8ccd2c7b006b800a97b0e1d6f891c45f91d9d/views.py#L80-L100) where uploaded info is stored onto database
    - [Image id viewer](https://github.com/zenxha/sushi/blob/cec8ccd2c7b006b800a97b0e1d6f891c45f91d9d/views.py#L102-L108) which lets you view individual images based on id
  - Database:
    - Upload 
      - We mainly use the information stored on [this database](https://github.com/zenxha/sushi/blob/fa37260ea37930cff19fd023076c2a3ee56d5a4f/model.py#L5-L11)
      - The information gets [stored from the upload page](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/views.py#L62-L82)
      - And information is [displayed on our browse page](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/views.py#L47-L60) [here](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/templates/homesite/browse.html#L14-L18)
    - Login/Signup 
      - [Compares data in signup with data from database, if doesn't match, add to database](https://github.com/zenxha/sushi/blob/main/views.py#L144-L157)
      - Check if the user has an account by [checking usernames in database](https://github.com/zenxha/sushi/blob/main/views.py#L116-L119)
      - [If password is correct, it signs the user in and redirect to upload page, if information incorrect, redirect to login.](https://github.com/zenxha/sushi/blob/main/views.py#L123-L128)
    - Review Browser
      - [Takes information from upload.html](https://github.com/zenxha/sushi/blob/main/views.py#L144-L157)
      - [Displays information on namecards on browse.html](https://github.com/zenxha/sushi/blob/2407689b21067ee1637b7f3c858f0db6245f6bff/templates/homesite/browse.html#L6-L18)
    - API viewer (Utilized recent tech talk to create this section)
      - [Querying database and returning data in the form of json to the user](https://github.com/zenxha/sushi/blob/52e9f3dadf6abfe50e7c9d476518afee48cf1a66/views.py#L172-L174)
      - [Displaying individual review based on id in form of json](https://github.com/zenxha/sushi/blob/52e9f3dadf6abfe50e7c9d476518afee48cf1a66/views.py#L176-L185)
      - [Displaying all reviews in form of json](https://github.com/zenxha/sushi/blob/52e9f3dadf6abfe50e7c9d476518afee48cf1a66/views.py#L190-L206)
- Easter Egg 
  - To get to our easter egg, use the username mort in signin and click submit. Then use the easter egg navbar to view the other sections of the easter egg
- Project WOW
  - [Our upload page](http://rubinfamily.dyndns.org:5000/upload). Each image uploaded is assigned an id, which you can view on the browse page. Once you have the image, go to the url http://rubinfamily.dyndns.org:5000/images/1, where you replace 1 with whatever id the image you just uploaded is to view the image. You can also view the image by clicking the picture in the browse page and see the full image


### Tickets Progress (Overall progress linked [here](https://github.com/zenxha/sushi/projects/4#column-12624141))

|Member|Tickets|
| --- | --- |
|Allen|<ul><li>[Worked on creating the IAM page and displaying each person's IAM statements](https://github.com/zenxha/sushi/projects/4#card-54281293)</li><li>[Worked with Chris on creating the front end for our browse page that displays the user's review (2nd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)</li><li>[Embed the crossover report into the easter egg navbar](https://github.com/zenxha/sushi/projects/4#card-55314605)</li><li>[Moved the project section from the main site navbar to the easter egg navbar](https://github.com/zenxha/sushi/projects/4#card-55314635)</li><ul>|
|Chris|<ul><li>[Work on the user sessions as well as user authentication](https://github.com/zenxha/sushi/projects/4#card-53703118)</li><li>[Worked on creating the front end for the browse page that displays user info and implementing CSS on the page(2nd and 3rd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)</li><ul>|
|Devam|<ul><li>[Work on user login and authentication (still incomplete due to technical issues. We have it running, but not storing in database)](https://github.com/zenxha/sushi/projects/4#card-53785877)</li><li>[Helped secure the route to easter egg so it is only accessible by entering mort as the username, and can't be viewed by just typing in the url (checkbox 2 and 3)](https://github.com/zenxha/sushi/projects/4#card-53782464)|
|Komay|<ul><li>[Worked on integrating the backend login/auth system with the frontend html form](https://github.com/zenxha/sushi/projects/4#card-54354857)</li><li>[Finished 3rd checkbox of the ticket which only allows the correct account to access easteregg](https://github.com/zenxha/sushi/projects/4#card-53782464)</li><li>[Worked on the backend aspect of taking the informatoin from upload.html and displaying it on browse.html(1st and 3rd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)</li><ul>|


### College Board Requirements
- Instructions for input from one of the following:
  - the user (including user actions that trigger events)
  - a device
  - an online data stream
  - a file
- Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
- At least one procedure that contributes to the program’s intended purpose,
where you have defined:
  - the procedure’s name
  - the return type (if necessary)
  - one or more parameters
- An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
- Calls to your student-developed procedure
- Instructions for output (tactile, audible, visual, or textual) based on input and
program functionality

## Our Idea
- We aim for a simple and clean site that contains everything about sushi. On the site you’ll be able to upload images of sushi and review sushi and give your opinon on each sushi you eat.

