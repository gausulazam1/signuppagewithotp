from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

print("✅ main.py is running...")  # Confirming the app runs

# 🗂️ In-memory store
otp_store = {}  # phone -> otp
users = {}      # phone -> True/False (verified)

# 📦 Input models
class PhoneNumberInput(BaseModel):
    phone: str

class OTPVerifyInput(BaseModel):
    phone: str
    otp: str

# 📤 Send OTP
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
    print(f"📲 OTP for {phone}: {otp}")
    print("========================\n")

    # ✅ Include OTP in response (testing only)
    return {
        "message": message,
        "note": f"OTP sent to {phone}. Check terminal.",
        "otp": otp  # ❗ Testing purpose only
    }

# 🔐 Verify OTP
@app.post("/verify-otp")
def verify_otp(data: OTPVerifyInput):
    phone = data.phone.strip()
    otp = data.otp.strip()

    if phone not in otp_store:
        raise HTTPException(status_code=400, detail="⚠️ Please request OTP first.")

    if otp_store[phone] != otp:
        raise HTTPException(status_code=400, detail="❌ Incorrect OTP")

    users[phone] = True
    del otp_store[phone]

    return {
        "message": "✅ OTP verified. Logged in successfully!",
        "user": phone
    }



















































# otp in the terminal 
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import random

# app = FastAPI()

# # In-memory storage
# otp_store = {}
# users = {}

# class PhoneNumberInput(BaseModel):
#     phone: str

# class OTPVerifyInput(BaseModel):
#     phone: str
#     otp: str

# @app.post("/send-otp")
# def send_otp(data: PhoneNumberInput):
#     phone = data.phone.strip()

#     if phone in users:
#         message = "User exists. Sending OTP for login..."
#     else:
#         users[phone] = False
#         message = "New user. Sending OTP for signup..."

#     otp = str(random.randint(100000, 999999))
#     otp_store[phone] = otp

#     # Add prints for debug
#     print(" Function reached: send_otp")
#     print(" Phone number received:", phone)
#     print(" " \
#     "OTP generated:", otp)

#     return {"message": message, "note": "OTP sent. Check terminal."}

# @app.post("/verify-otp")
# def verify_otp(data: OTPVerifyInput):
#     phone = data.phone.strip()
#     otp = data.otp.strip()

#     if phone not in otp_store:
#         raise HTTPException(status_code=400, detail="Please request OTP first.")
    
#     if otp_store[phone] != otp:
#         raise HTTPException(status_code=400, detail="Incorrect OTP")

#     users[phone] = True
#     del otp_store[phone]

#     return {"message": " OTP verified. Logged in successfully!"}
































































# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import random

# app = FastAPI()

# # ✅ In-memory database
# otp_store = {}   # phone -> otp
# users = {}       # phone -> is_verified

# # 📥 Phone number input
# class PhoneNumberInput(BaseModel):
#     phone: str

# # 📥 OTP input
# class OTPVerifyInput(BaseModel):
#     phone: str
#     otp: str

# # 🔘 Send OTP endpoint
# @app.post("/send-otp")
# def send_otp(data: PhoneNumberInput):
#     phone = data.phone.strip()

#     # Check if user already exists
#     if phone in users:
#         message = "User exists. Sending OTP for login..."
#     else:
#         users[phone] = False
#         message = "New user. Sending OTP for signup..."

#     # Generate and store OTP
#     otp = str(random.randint(100000, 999999))
#     otp_store[phone] = otp
#     print(f"\n📲 OTP for {phone}: {otp}\n")

#     return {"message": message, "note": "OTP sent. Check terminal."}

# # 🔐 Verify OTP endpoint
# @app.post("/verify-otp")
# def verify_otp(data: OTPVerifyInput):
#     phone = data.phone.strip()
#     otp = data.otp.strip()

#     if phone not in otp_store:
#         raise HTTPException(status_code=400, detail="Please request OTP first.")

#     if otp_store[phone] != otp:
#         raise HTTPException(status_code=400, detail="❌ Incorrect OTP")

#     users[phone] = True
#     del otp_store[phone]

#     return {"message": "✅ OTP verified. Logged in successfully!"}










































# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import random

# app = FastAPI()

# # In-memory DB (dict) for users and OTPs
# users_db = {}
# otp_db = {}

# class PhoneInput(BaseModel):
#     phone: str

# class OTPInput(BaseModel):
#     phone: str
#     otp: str

# # Step 1: Send OTP
# @app.post("/send-otp")
# def send_otp(data: PhoneInput):
#     phone = data.phone

#     # Check if already registered
#     if phone in users_db:
#         msg = "Phone number already registered. Logging in..."
#     else:
#         msg = "Phone number not registered. Signing up..."

#     # Generate 6-digit OTP
#     otp = str(random.randint(100000, 999999))
#     otp_db[phone] = otp

#     print(f"📲 OTP for {phone}: {otp}")  # Shown in terminal

#     return {"message": msg + " OTP sent (check terminal)."}


# # Step 2: Verify OTP
# @app.post("/verify-otp")
# def verify_otp(data: OTPInput):
#     phone = data.phone
#     otp = data.otp

#     if phone not in otp_db:
#         raise HTTPException(status_code=400, detail="Please request OTP first.")

#     if otp_db[phone] != otp:
#         raise HTTPException(status_code=401, detail="Invalid OTP")

#     # Signup or login
#     if phone not in users_db:
#         users_db[phone] = {"phone": phone}
#         return {"message": "✅ Signup successful!"}
#     else:
#         return {"message": "✅ Login successful!"}
