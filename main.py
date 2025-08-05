from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

print("main.py is running...")  # Confirming the app runs

# In-memory store
otp_store = {}  # phone -> otp
users = {}      # phone -> True/False (verified)

# Input models
class PhoneNumberInput(BaseModel):
    phone: str

class OTPVerifyInput(BaseModel):
    phone: str
    otp: str

#  Send OTP
@app.post("/send-otp")
def send_otp(data: PhoneNumberInput):
    phone = data.phone.strip() 

    if phone in users:
        message = "User exists. Sending OTP for login..."
    else:
        users[phone] = False
        message = "New user. Sending OTP for signup..."

    otp = str(random.randint(1000, 9999))
    otp_store[phone] = otp

    # 🖨️ Print OTP in terminal
    print("\n========================")
    print(f"OTP for {phone}: {otp}")
    print("========================\n")

    #  Include OTP in response (testing only)
    return {
        "message": message,
        "note": f"OTP sent to {phone}. Check terminal.",
        "otp": otp  #  Testing purpose only
    }

# Verify OTP
@app.post("/verify-otp")
def verify_otp(data: OTPVerifyInput):
    phone = data.phone.strip()
    otp = data.otp.strip()

    if phone not in otp_store:
        raise HTTPException(status_code=400, detail=" Please request OTP first.")

    if otp_store[phone] != otp:
        raise HTTPException(status_code=400, detail=" Incorrect OTP")

    users[phone] = True
    del otp_store[phone]

    return {
        "message": " OTP verified. Logged in successfully!",
        "user": phone
    }
