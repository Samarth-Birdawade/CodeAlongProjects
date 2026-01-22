id = 1
firstName = "Samarth"
lastName = "   Birdawade   "
phoneNo = "+91 1234567891"
insuranceNo = "123-45-6789"
hasInsurance = True
billingAmount = "10000"

print(type(billingAmount))
billingAmount = float(billingAmount)
print(type(billingAmount))

print(f'ID: {id}, \nFirst Name: {firstName}, \nLast Name: {lastName.strip()}, \nPhone Number: {phoneNo.removeprefix("+91 ")}, \nHas Insurance: {hasInsurance}, \nBilling Amount: {billingAmount}, \nInsurance Number (last 4 digits): {insuranceNo[7:len(insuranceNo)]}')


# Same Data but in JSON format
insurance_details = {
    "id": id,
    "first_name": firstName,
    "last_name": lastName.strip(),
    "phone_no": phoneNo.removeprefix("+91 "),
    "has_insurance": hasInsurance,
    "billing_amount": billingAmount,
    "insurance_no_last_4": insuranceNo[7:len(insuranceNo)]
}

for key, value in insurance_details.items():
    print(f"{key}: {value}")