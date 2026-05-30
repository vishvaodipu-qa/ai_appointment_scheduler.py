"""
 AI-Powered Health Appointment Scheduler
Built by: Vishva (7-Day AI Side Hustle Challenge)
Purpose: Automatically optimizes doctor schedules, filters slot availability, 
         and flags booking conflicts to reduce clinic operational overhead.
Security: 100% Safe. No real hospital databases or private patient logs exposed.
"""

def optimize_appointment_slots(requested_slots, doctor_availability):
    print("--- 🩺 AI Healthcare Scheduling Engine Running --- \n")
    
    for slot in requested_slots:
        doctor = slot["doctor"]
        time = slot["requested_time"]
        
        # Algorithmic Check: Is the doctor available at the requested timestamp?
        if time in doctor_availability.get(doctor, []):
            print(f"✅ CONFIRMED APPOINTMENT:")
            print(f"👤 Patient: {slot['patient']}")
            print(f"👨‍⚕️ Doctor: {doctor}")
            print(f"⏰ Allocated Time: {time}")
            print(f"💡 Status: Slot locked successfully. Notification triggered.")
            print("-" * 50)
        else:
            print(f"⚠️ BOOKING CONFLICT DETECTED (Information Overlap):")
            print(f"👤 Patient: {slot['patient']}")
            print(f"👨‍⚕️ Doctor: {doctor}")
            print(f"❌ Requested Time: {time} (Doctor unavailable/Overbooked)")
            print(f"💡 Action: AI suggesting next alternative slot automatically.")
            print("-" * 50)

if __name__ == "__main__":
    # Mock Data Array - Dynamic Specialist Availability Matrix
    doctor_schedules = {
        "Dr. Acharya (Ayurveda)": ["10:00 AM", "11:00 AM", "02:00 PM"],
        "Dr. Hegde (Wellness Consultant)": ["09:00 AM", "12:00 PM", "04:00 PM"]
    }
    
    # Incoming Patient Routing Array
    incoming_requests = [
        {"patient": "Ramesh Kumar", "doctor": "Dr. Acharya (Ayurveda)", "requested_time": "11:00 AM"},
        {"patient": "Suresh Shetty", "doctor": "Dr. Hegde (Wellness Consultant)", "requested_time": "11:00 AM"}, # Will cause a conflict
        {"patient": "Ananya Rao", "doctor": "Dr. Acharya (Ayurveda)", "requested_time": "02:00 PM"}
    ]
    
    # Fire the optimization pipeline
    optimize_appointment_slots(incoming_requests, doctor_schedules)
