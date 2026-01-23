s = "19th Jan: 1. Finished the assigned SOPs. 2. Completed the Axis Bank opening Procedure with the help of Mohan. 3. Sent the GMC Policy details to Mohan. 4 . Filled the MS List for Laptop Details. 20th Jan: 1. Finished setting up MS 365 account and apps with the help of Khushi. 2. Started learning the Udemy certification content. 3. Finished setting up the signature on the xogene email id. 4. Attended a meeting with Nisha regarding onboarding details. 21st Jan: 1. Finished with the pending SOPs including Employee Handbook and marked them as completed in the SOPTracker. 2. Started with the Training videos on TalentLMS and finished 'Prime 2.3 Training 01' and 'Training 1' of Xogene Disclosure. 3. Attended a meeting with Nisha regarding onboarding details. 4. Attended a meeting with my assigned Buddy - Avinash. 5. Attended the Daily Dev Scrums meet. 22nd Jan: 1. Finished with Xogene Disclosure TalentLMS Training 2-6 modules. 2. Started with the Udemy course"

word_to_find = input("Enter the word to find its frequency: ")

positons = []
index = s.find(word_to_find)
while index != -1:
    positons.append(index)
    index = s.find(word_to_find, index + 1)

print(f"The word '{word_to_find}' appears {s.count(word_to_find)} times in the report.")
print(f"Positions of '{word_to_find}': {positons}")