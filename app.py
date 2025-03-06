from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from pyotp import TOTP
import qrcode

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Generate a secret key
secret_key = "7J64V3P3E77J3LKNUGSZ5QBNTLRLTKVL"

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/generate_qr_code")
def generate_qr_code():
    # Create a TOTP object
    totp = TOTP(secret_key).provisioning_uri("kathan", issuer_name="TOTP App")

    # Generate a QR code
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(totp)
    qr_code.make(fit=True)

    # Save the QR code to a file
    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    return {"message": "QR code generated successfully"}

# /************* ✨ Codeium Command 🌟 *************/
# /*************  ✨ Codeium Command 🌟  *************/
from fastapi.responses import HTMLResponse

@app.post("/verify_otp")
def verify_otp(otp_code: str = Form(...)):
    # Create a TOTP object
    totp = TOTP(secret_key)

    # Verify the OTP code
    if totp.verify(otp_code):
        msg = "OTP code is Valid"
        return HTMLResponse(
            f"""
            <script>
                alert("OTP code is Valid");
            </script>
            """,
            status_code=200,
        )
    else:
        msg = "OTP code is Invalid"

    return HTMLResponse(
        f"""
        <script>
            alert("{msg}");
        </script>
        """,
        status_code=200,
    )
    return HTMLResponse(
            f"""
            <script>
                alert("OTP code is valid");
            </script>
            """,
            status_code=200,
        )
# /******  78b04daf-5ff2-4b55-9b3e-df195095c18e  *******/
# /****** 3bd193b7-cf2c-49db-9907-46d990d17243 *******/

@app.get("/qr_code.png")
def get_qr_code():
    return FileResponse("qr_code.png", media_type="image/png")
