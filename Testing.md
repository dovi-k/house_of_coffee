
# Testing and Validation


### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- The report did not have any issues in final testing.
![Checkout](/documentation/test-images/links-test.png)
<br>

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
- After adding my URL I recievedd an Error that it couldn't connect with the https://house-of-coffee.herokuapp.com/ url. Haven't resolved.
<details>

### [JavaScript: JSHint](https://jshint.com/)
- JSHint I used to test Javascript in this project 
- Stripe element JS had 23 warnings but no errors

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CSS code I have inputted the URL of the deployed project and no errors were found.
![Checkout](/documentation/test-images/css-val.png)

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code by pasting the link to the deployed project, few errors poped up and warnings.
I have not been able to fict the errors unfortunately yet the screenshots for the erros are bellow:
![Checkout](/documentation/test-images/html-err1.png)
![Checkout](/documentation/test-images/html-err2.png)

 


### Testing User Stories


 - As a user, I want to be able to access the website from any device, website anytime and anywhere.

First storie to check. The website was accesible from most of the devices, I have checked on ASUS ZENBOOK laptop, my phone Samsung S8 and is available any time. The Responsiveness of the site on some pages are not the best in particularly on small screens. The about page is slightly off and the footer on small screens goes to the left.


- As a user, I want user intuitive website that is easy to navigate, so that I can quickly find what I'm looking for.

The wevbsite is wuite easyt to navigate it is not burdened with navigation options, you can filter products, run search by keyword whic helps quickly to find the products.

- As a user, I want to easily access social media links of the company, so that I can lran more about the brand.

The links are easily accessible, unfortunately they are not connected with the business social media at the moment, most of them bring users to the main pages of the social media or to the creator of the webpage github and linked in accounts.

- As a user, I want to be able to read infomration about the business and what their ideas are, how they are different from other businesses so I could decide if I want to choose this brand. 

That's one of the user stories taht wasn't fully executed, you can get a sense of the business from short description in the about section on footer and About us page.


- As a user, I want to be able to easily contact the owner/manager of the company, so I could direct my questions and queries.

On the footer users can access the Contact Us form and the form is easy to fill and submit with only 3 fields and a filler image of coffees on the left side on the Desktop view. Going forward depending on the volumes of people contacting user form can be moved to the main nav. the decision was made to keep it in the footer so the main focus would be on the Product side of things.

- As a user, I want to view  product details in clear lay-out(e.g. image, price, description), so that I can make purchases.

the layout in the project is clear, however the images after uploading them on AWS not fully dispaying. you can see some of them on the github local host page. however, the price, category, flavour and description are clrealy displayed.

- As a user, I want to search and filter the products easily, so that I can easily find what I am looking for.

All the search and filetering functions are wokring in the page. You can filter by category, low to high price, high to low and alphabeticaly as welkl as view all products.

- As a user, I want to view and modify my order in the cart before completing it, so that I can apply changes beforeproceeding to payment. 

Once the products are added you can easily view the products in the cart and adjust quantity of products accordingly.

- As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.

The payments and delivery cost are clearly displayed in the scheckout page, you can also view the amount that you need to spend to get the free delivery.

- As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.

Payments are made by stripe and it seems to be safe and secure way to pay for the goods.

- As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.

Unfortunately, I have made the purchases but not all the emails go through with my information.

#### New User stories

- As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.

New users can easily register for the site, they can create a profile with all the details which makes checkout really easy and purchasing the good much easier as well. Users can view their purhcase history.

#### Returning user stories

- As a user, I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.

Log in process is pretty easy on the website, users can view their saves details.

- As a user, I want to reset my password if I forgot it, so that I can get access to my profile again. 

Users can reset their passwors if they forgot it. 

#### Website Owner(admin) stories
- As a owner, I want to have convenient and secure admin interface available only for website admin, so that I can add, edit and remove products.

Site admin can add, delete and remove products. The only downsite that there is no confimration for safety when the user deletes the product it gets deleted straight away, which can create problems in the future.

- As a owner, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries.

This user story has not been tested. The email set up has been done, however it was not properly tested.
