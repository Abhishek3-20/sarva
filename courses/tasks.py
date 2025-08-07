from celery import shared_task

@shared_task
def send_course_enrollment_email(user_email, course_title):
    # Your email sending logic here
    print(f"Sending enrollment email to {user_email} for course {course_title}")
    return True