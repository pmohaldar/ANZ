

  Feature: Once the workout button is clicked , message should be shown
  # Enter feature description here

  Scenario: when one field is only filled and "workout how " button is clicked error message should be thrown
  Given Once the browser is launched give the url
  When Living expense field is filled
  When Click on Workout how much I can borrow
  Then Error message "Based on the details you've entered, we're unable to give you an estimate of your borrowing power with this calculator. For questions, call us on 1800 035 500."should be shown