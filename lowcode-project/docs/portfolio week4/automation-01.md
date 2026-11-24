# Week 4 — Automation 1: Medical Clinic Test Results Workflow

## Business Problem

In a medical clinic, administrative staff often need to check if new test results have arrived, update patient records and inform the team. Doing these tasks manually can take time and sometimes lead to mistakes or delays.

I chose this project because I am interested in how technology can improve administrative work in healthcare. I believe automation can help clinics save time, reduce errors and keep information more organised.

My main goal is to create a system that can automatically receive and organise medical test results, making daily tasks easier for administrative staff.

For my first prototype, I used Make.com to build a simple workflow. When the webhook receives fictional registration data, the information is automatically added to Google Sheets and an email notification is sent through Gmail.

This is only the first stage of my project. The automation does not process medical test results yet, but it helped me understand how different tools can work together. I also learned how to test the workflow and fix problems when something did not work as expected.

All the information I used during testing was fictional.

## Flask Webhook and Data Validation

I also created a Flask webhook using Python to receive registration data in JSON format. The webhook checks if the required fields (name, email and company) are present and if the email address has a valid format.

I tested the webhook using curl in the VS Code terminal. The tests showed that valid data was accepted and incorrect or missing information was rejected.

I also added a simple idempotency check to prevent the same registration from being processed twice. When I sent the same request two times, the webhook returned the same reference number. This helped me understand why checking for duplicate requests is important in automation.

## Workflow Steps

For my first prototype, I created an automation in Make.com using three modules: Webhook, Google Sheets and Gmail.

Later, I added an HTTP module to connect Make.com to my Flask application through ngrok.

The final workflow included four modules:

Webhook (Trigger): Receives fictional registration data, including name, email and company.

HTTP (Make a Request): Sends the registration data to my Flask application through ngrok.

Google Sheets (Add a Row): Saves the registration information in a spreadsheet.

Gmail (Send an Email): Sends an email notification when new information is received.

## Workflow Diagram

The diagram below shows the four modules of my final automation.

Webhook (Trigger)
        |
        v
HTTP (Flask via ngrok)
        |
        v
Google Sheets (Add a Row)
        |
        v
Gmail (Send an Email)

The webhook receives fictional registration data. The HTTP module sends the data to Flask through ngrok. Google Sheets saves the information, and Gmail sends an email notification.

## Testing and Results
I tested my Flask application using fictional registration data and HTTP POST requests.

First, I sent a valid registration with a name, email and company. The application returned HTTP 200 OK and generated a reference number.

Next, I tested a registration without an email address. The application returned HTTP 400 Bad Request because a required field was missing.

I also tested an invalid email address. The application returned HTTP 400 Bad Request with an error message.

Finally, I sent a request using plain text instead of JSON. The application returned HTTP 415 Unsupported Media Type.

## Final Automation Test

After testing Flask separately, I managed to connect it to Make.com using HTTP and ngrok.

At first, my automation had only three modules, but later I was able to add the HTTP module to connect it to my Python application.

For testing, I used fictional information from a patient called Ana Costa, from Test Clinic. The data was received by the webhook, sent to Flask, saved in Google Sheets, and then I received an email notification in Gmail.

On 23 November 2026, I tested the complete automation, and all four modules worked correctly.

During the development process, I had some difficulties understanding how to connect the different tools and make everything work together.

It is still a simple project that uses only fictional data, but it was important for me to put into practice what I am learning in the course.

## Commands Used During Testing

With the help of ChatGPT, I used different commands in the VS Code terminal to run and test my application.

### Running Flask

I used this command to start my Flask application:

```bash
python app.py
```

The application ran locally on port 5001.

### Testing Flask with ngrok

I used curl to send fictional registration data to my Flask application through ngrok.

```bash
curl -i -X POST 'https://YOUR-NGROK-URL/hooks/signup' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ana Costa","email":"ana@example.com","company":"Test Clinic"}'
```

This helped me check that Flask could receive and process requests through ngrok.

### Testing the Make.com Webhook

I also used curl to send fictional registration data directly to my Make.com webhook.

```bash
curl -i -X POST 'https://hook.eu1.make.com/YOUR-WEBHOOK-ID' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ana Costa","email":"ana@example.com","company":"Test Clinic"}'
```

This test helped me check the complete workflow, from receiving the data to saving it in Google Sheets and sending an email notification.

These commands helped me understand how to test APIs and connect different applications.

## Project Evidence

I saved screenshots to document the tests and results of my automation.

The screenshots show:

1. **Make.com:** The complete workflow executed successfully with four modules.
2. **Google Sheets:** Fictional registration data was saved in the spreadsheet.
3. **Gmail:** An automatic email notification was received.
4. **Flask:** The application received an HTTP POST request and returned status 200.
5. **ngrok:** The connection between the public HTTPS address and my local Flask application.

All screenshots are saved in the `docs/portfolio/screenshots` folder.