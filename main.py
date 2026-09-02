print("AI College Complaint Prioritizer")
complaint = input("Enter your complaint: ").lower()

priority = 0
department = "General"
action = "Review complaint"

if "wifi" in complaint or "internet" in complaint:
    department = "Network Team"
    priority = 40
    action = "Check network connection"

elif "projector" in complaint or "computer" in complaint:
    department = "IT Department"
    priority = 40
    action = "Send IT Technician"

elif "clean" in complaint or "washrooms" in complaint:
    department = "Housekeeping"
    priority = 40
    action = "Send housekeeping staff"

elif "water" in complaint or "electricity" in complaint:
    department = "Maintenance"
    priority = 40
    action = "Send maintenance staff"

elif "fire" in complaint or "danger" in complaint:
    department = "Emergency Team"
    priority = 100
    action = "Activate emergency response"

if "tomorrow" in complaint or "urgent" in complaint:
    priority += 30

    if priority > 100:
        priority = 100

print("\n====AI Analysis====")
print("Department:", department)
print("Priority Score:", priority, "%")
print("Recommended Action: ", action)

if priority >= 80:
    print("Urgency: HIGH")

elif priority >= 50:
    print("Urgency: MEDIUM")

else:
    print("Urgency: LOW")
