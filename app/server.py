import os
import json

from flask import Flask, render_template
from flask.ext.assets import Environment

app = Flask(__name__)
app.debug = True

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
  return {
    'asset_path': '/static/govuk-template/',
    'prototypes_asset_path': '/static/'
  }

@app.route('/')
def home():
  return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('common/proto-404.html'), 404

@app.route('/404')
def edge_of_proto(e):
    return render_template('common/proto-404.html')

# ---------------------------------------------------------------------------

# LAST OF THE ALPHA PROTOTYPES!

# Transaction flows, citizens sign transfer and charge v3 -----------------

# Step 1a - external process step - show user email
@app.route('/charges/citizen-1-email')
def transfer_and_charge_citizen_1_email_3_0():
  return render_template('charges/citizen-1-email-2.0.html', next_page="citizen-1-start")

@app.route('/charges/citizen-1-start')
def transfer_and_charge_citizen_1_start_3_0():
  return render_template('charges/citizen-1-start-2.0.html', next_page="citizen-1-login")

# Step 1 - login with GOV.UK Verify
@app.route('/charges/citizen-1-login')
def transfer_and_charge_citizen_1_login_3_0():
  return render_template('charges/citizen-1-login-2.0.html', next_page="citizen-1-enter-token")

# Step 2 - Client 1 enters token
@app.route('/charges/citizen-1-enter-token')
def transfer_and_charge_citizen_1_enter_token_3_0():
  return render_template('charges/citizen-1-enter-token-2.0.html', next_page="citizen-1-sign-mortgage")

# Step 3 - Client 1 signs mortgage deed
@app.route('/charges/citizen-1-sign-mortgage')
def transfer_and_charge_citizen_1_sign_mortgage_3_0():
  return render_template('charges/citizen-1-sign-mortgage-2.0.html', next_page="citizen-1-sms")

# Step 3a - external process step - show user sms message
@app.route('/charges/citizen-1-sms')
def transfer_and_charge_citizen_1_sms_3_0():
  return render_template('charges/citizen-1-sms-2.0.html', next_page="citizen-1-2-factor-auth")

# Step 4 - Client 1 2 factor authentication
@app.route('/charges/citizen-1-2-factor-auth')
def transfer_and_charge_citizen_1_2_factor_auth():
  return render_template('charges/citizen-1-2-factor.html', next_page="citizen-1-semi-confirmed")

# Step 5 - Client 1 - semi confirmation
@app.route('/charges/citizen-1-semi-confirmed')
def transfer_and_charge_citizen_1_semi_confirmed_3_0():
  return render_template('charges/citizen-1-semi-confirmed-2.0.html')
# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, client(s) confirm v2.2 --------
@app.route('/charges/client-start')
def client_start_2_2():
  return render_template('charges/client-start.html')

@app.route('/charges/client-login')
def client_verify_2_2():
  return render_template('charges/verify-intro.html')

# GOV.UK verify -  Sub flow Step 2 - who verified you
@app.route('/charges/client-who-verified-you')
def relationship_starts_client_verify_who_1():
  return render_template('charges/verify-who.html')

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/charges/client-experian-sign-in')
def relationship_starts_client_verify_experian_sign_in_1():
  return render_template('charges/verify-sign-in.html')

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/charges/client-experian-sign-in-part-2')
def relationship_starts_client_verify_experian_sign_in_2nd_part_1():
  return render_template('charges/verify-sign-in-2.html')

#       end Sub flow - GOV.UK Verification ---------------------

# Step 2 - Client 1 enters token
@app.route('/charges/client-enter-token')
def client_enter_token_2_1():
  return render_template('charges/client-enter-token-2.1.html')

# Step 3 - Client 1 confirms
@app.route('/charges/client-confirm')
def client_confirm_2_2():
  return render_template('charges/client-confirm-2.2.html')

# Step 4 - Client 1 receives confirmation
@app.route('/charges/client-semi-confirmed')
def client_semi_confirmed_2_2():
  return render_template('charges/client-semi-confirmed-2.2.html')

# Step 5 - Client can now view the register if they want to.
@app.route('/charges/client-view-register')
def client_view_register_2_1():
  return render_template('charges/register-2.1-no-pending.html')


if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
