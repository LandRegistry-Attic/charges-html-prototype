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

# 1: Conveyancer creates a case

@app.route('/charges/conveyancer-start')
def charges_login():
  return render_template('charges/login.html', next_page="case-list")

@app.route('/charges/case-list')
def charges_case_list():
  json_data=open('app/static/data/cases.json', "r")
  data = json.load(json_data)
  return render_template('charges/conveyancer-case-list.html', data=data, next_page="conveyancer-get-client-assurance")

@app.route('/charges/conveyancer-get-client-assurance')
def charges_conveyancer_get_client():
  return render_template('charges/conveyancer-get-client-assurance.html')

@app.route('/charges/conveyancer-find-property')
def charges_conveyancer_find_property():
  return render_template('charges/conveyancer-find-property.html', next_page='conveyancer_select_property')

@app.route('/charges/conveyancer-select-property')
def charges_conveyancer_select_property():
  return render_template('charges/conveyancer-select-property.html')

@app.route('/charges/conveyancer-select-task')
def charges_conveyancer_select_task():
  return render_template('charges/conveyancer-select-task.html')

@app.route('/charges/conveyancer-add-clients')
def charges_conveyancer_add_clients():
  return render_template('charges/conveyancer-add-clients.html')

@app.route('/charges/conveyancer-add-client-1')
def charges_conveyancer_add_client_1():
  return render_template('charges/conveyancer-add-client-1.html')

@app.route('/charges/conveyancer-add-client-2')
def charges_conveyancer_add_client_2():
  return render_template('charges/conveyancer-add-client-2.html')

@app.route('/charges/conveyancer-confirm')
def charges_conveyancer_confirm():
  return render_template('charges/conveyancer-confirm.html')

@app.route('/charges/conveyancer-token')
def charges_conveyancer_token():
  return render_template('charges/conveyancer-token.html')


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


# Create Mortgage Login Page
@app.route('/create-mortgage/login')
def transfer_login():
  return render_template('charges/login.html', next_page="conveyancer-case-list")

# Create Mortgage Conveyancer case list page
@app.route('/create-mortgage/conveyancer-case-list')
def conveyancer_mortgage_case_list():
  json_data=open('app/static/data/mortgage-cases.json', "r")
  data = json.load(json_data)
  return render_template('charges/conveyancer-case-list.html', data=data)

# Transfer prototypes, mortgage details page
@app.route('/create-mortgage/mortgage-details')
def transfer_mortgage_details():
  return render_template('charges/mortgage-details.html')

# Transfer prototypes, mortgage details entered page
@app.route('/create-mortgage/mortgage-details-entered')
def transfer_mortgage_details_entered():
  return render_template('charges/mortgage-details-entered.html')

# Transfer prototypes, summary page
@app.route('/create-mortgage/summary')
def transfer_summary():
  json_data=open('app/static/data/complete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('charges/summary.html', editable=True, conveyancer="buyer", data=data)

# Transfer prototypes, done page
@app.route('/create-mortgage/done')
def transfer_done():
  return render_template('charges/done.html')


if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
