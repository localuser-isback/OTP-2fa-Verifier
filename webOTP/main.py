from flask import Flask, render_template, request
import pyotp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_otp():
    if request.method == 'POST':
        mode = request.form.get('mode')

        if mode == "1":
            user_otp = request.form.get('otp')
            if user_otp is not None and len(user_otp) > 0:
                totp = pyotp.TOTP(user_otp)
                current_code = totp.now()
            else:
                current_code = "OTP Code is required."
        elif mode == "2":
            user_otp = request.form.get('otp')
            custom_counter = request.form.get('custom_counter', default=0)
            if user_otp is not None and len(user_otp) > 0:
                try:
                    custom_counter = float(custom_counter)
                except ValueError:
                    custom_counter = 0
                hotp = pyotp.HOTP(user_otp)
                current_code = hotp.at(custom_counter)
            else:
                current_code = "OTP Key is required."
        else:
            return "Please select a valid option."

        return render_template('index.html', current_code=current_code)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
