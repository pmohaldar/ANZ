 Feature: Calculate the borrowing estimation
  # Enter feature description here

  Scenario: Once all the fields are filled , borrowing estimation should be shown
  Given Once the browser is launched give the url
  When Fill in all the Value fields for applicant type is single and property is home to buy

  When Click on Workout how much I can borrow
  Then It should show the estimated amount to be borrowed