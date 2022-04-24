import yagmail
import os
import glob

receiver = "sankpaljaykumar@gmail.com"  # receiver email address
body = "Attendence File"  # email body

list_of_files = glob.glob('C:/Users/Jaykumar/Desktop/mini2/Attendance/*.csv') 
latest_file = max(list_of_files, key=os.path.getctime)
basename = os.path.basename(latest_file)


filename = "Attendance"+os.sep+basename

yag = yagmail.SMTP("js1910492@gmail.com", "JohnSmith@2316")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)

