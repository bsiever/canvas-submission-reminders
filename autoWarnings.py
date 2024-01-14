
from canvasapi import Canvas
from datetime import datetime,timedelta
import os  # For environment variables

API_URL = os.environ.get('CANVAS_URL')
API_KEY = os.environ.get('CANVAS_KEY')
COURSE_ID = os.environ.get('CANVAS_COURSE_ID')

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

def newConversation(userIds, subject, message):
    # Create a new conversation
    canvas.create_conversation(userIds, message, subject=subject, force_new=True, group_conversation=False, context_code=f'course_{course.id}')

assignments = [a for a in course.get_assignments()]
users = [u for u in course.get_users(enrollment_type=["student", "observer", "student_view"])]
userIds = set([u.id for u in users])

# Iterate through all assignments with online submissions.  
checkTime = datetime.utcnow().replace(tzinfo=None)
for a in assignments:
    if a.due_at!=None and any('online' in item for item in a.submission_types):
        # If the due date is less than 24 hours away _AND_ submission is on Canvas, check for it
        due_time_utc = datetime.strptime(a.due_at, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
        if checkTime - due_time_utc  < timedelta(hours=24):
            # print(f'Due time: {due_time_utc} / now: {checkTime}')
            # print(f'{a.name} is due soon')
            submissions = [s for s in a.get_submissions()]
            unsubmitted = [s.user_id for s in submissions if s.submission_type == None]
            subject = f'{a.name} not submitted --- due soon!'
            message = f'{course.name}: {a.name}is due soon and you have not submitted it yet.  Please submit it as soon as possible!'    
            # print(f'{unsubmitted} students have not submitted')
            # print(f'Subject: {subject}\n Body: {message}')
            # Message to individuals
            newConversation(unsubmitted, subject, message)
            # Test message to self
            # newConversation([canvas.get_current_user().id], subject, message)
