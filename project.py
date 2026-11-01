hospital_queue = []
emergency_queue = []
in_consultation = []
patient_records = []

token_number = 101

doctors = {
    "1": "Dr. Sharma",
    "2": "Dr. Patil",
    "3": "Dr. Khan"
}


def add_patient(patient, age, contact, priority, doctor, date, time):
    global token_number

    patient_data = {
        "token": token_number,
        "name": patient,
        "age": age,
        "contact": contact,
        "priority": priority,
        "doctor": doctor,
        "date": date,
        "time": time,
        "status": "Waiting"
    }

    patient_records.append(patient_data)

    if priority == "E":
        emergency_queue.append(patient_data)
    else:
        hospital_queue.append(patient_data)

    print("\nPatient registered successfully!")
    print("Token Number:", token_number)
    print("Assigned Doctor:", doctor)

    token_number += 1


def next_patient():

    if emergency_queue:
        patient = emergency_queue.pop(0)

    elif hospital_queue:
        patient = hospital_queue.pop(0)

    else:
        print("No patients waiting")
        return

    patient["status"] = "In Consultation"
    in_consultation.append(patient)

    print("\nPatient called for consultation")
    print("Token:", patient["token"])
    print("Name:", patient["name"])
    print("Doctor:", patient["doctor"])
    print("Status:", patient["status"])


def pending_patient():

    print("\n--- EMERGENCY QUEUE ---")

    for patient in emergency_queue:
        print(patient["token"], patient["name"],
              "| Doctor:", patient["doctor"],
              "| Status:", patient["status"])

    print("\n--- NORMAL QUEUE ---")

    for patient in hospital_queue:
        print(patient["token"], patient["name"],
              "| Doctor:", patient["doctor"],
              "| Status:", patient["status"])


def cancel_patient(token):

    for queue in [emergency_queue, hospital_queue]:

        for patient in queue:

            if patient["token"] == token:
                queue.remove(patient)
                patient["status"] = "Cancelled"

                print("Patient", patient["name"],
                      "booking cancelled")
                return

    print("Waiting patient token not found")


def complete_patient(token):

    for patient in in_consultation:

        if patient["token"] == token:

            patient["status"] = "Completed"
            in_consultation.remove(patient)

            print("Consultation completed for:",
                  patient["name"])
            return

    print("Patient not found in consultation")


def display_records():

    if not patient_records:
        print("No patient records available")
        return

    print("\n--- ALL PATIENT RECORDS ---")

    for patient in patient_records:

        print("\nToken:", patient["token"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Contact:", patient["contact"])
        print("Priority:", patient["priority"])
        print("Doctor:", patient["doctor"])
        print("Appointment:", patient["date"], patient["time"])
        print("Status:", patient["status"])


def menu():

    while True:

        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1. Register Patient")
        print("2. Process Next Patient")
        print("3. Display Pending Patients")
        print("4. Cancel Patient Booking")
        print("5. Complete Consultation")
        print("6. Display All Patient Records")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            patient = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            contact = input("Enter contact number: ")

            print("\nSelect Priority:")
            print("E. Emergency")
            print("N. Normal")

            priority = input("Enter priority: ").upper()

            if priority not in ["E", "N"]:
                print("Invalid priority")
                continue

            print("\nSelect Doctor:")
            for key, doctor in doctors.items():
                print(key + ".", doctor)

            doctor_choice = input("Choose doctor: ")

            if doctor_choice not in doctors:
                print("Invalid doctor selection")
                continue

            doctor = doctors[doctor_choice]

            date = input("Enter appointment date: ")
            time = input("Enter appointment time: ")

            add_patient(
                patient, age, contact,
                priority, doctor, date, time
            )

        elif choice == '2':
            next_patient()

        elif choice == '3':
            pending_patient()

        elif choice == '4':
            token = int(input("Enter token number: "))
            cancel_patient(token)

        elif choice == '5':
            token = int(input("Enter completed patient token: "))
            complete_patient(token)

        elif choice == '6':
            display_records()

        elif choice == '7':
            print("Exiting...")
            print("Thank you!")
            break

        else:
            print("Invalid choice")


menu()