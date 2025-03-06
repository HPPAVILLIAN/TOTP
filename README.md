## Python version
- 3.11.9

## Install packages
- pip install -r requirements.txt

## Start the APP
- cd C:\Users\Admin\Documents\Kathan\totp\pyth\server
- uvicorn app:app --reload

## APP UI Overview

- Home Page
<img src="./sample_images/Home Page.png">
- Valid OTP Code
<img src="./sample_images/Valid OTP Code.png">
- Invalid OTP Code
<img src="./sample_images/Invalid OTP Code.png">

## Process
- User creation/Sign Up
    - Submit User Name, Password.
    - Hashed password (MD5 of password) will be stored in DB.
    - 2FA key (QR code) will be generated from TOTP (Time based OTP) server.
    - Use Google Authenticator to add the generated 2FA key.
- User login/Sign In
    - Submit User Name, Password.
    - Hashed password (MD5 of password) will be matched with the stored in DB.
    - If match is perfect, then user will be asked to enter TOTP.
    - Submitted TOTP will be compared with generated TOTP by the server.
    - If they are same, then user will be able to login and token will be given to the user for further actions.
