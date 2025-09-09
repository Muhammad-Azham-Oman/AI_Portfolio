from mcp.server.fastmcp import FastMCP
from hrms import *
from utils import seed_services
from typing import List,Dict
from emails import EmailSender
import os
from dotenv import load_dotenv
load_dotenv()

email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        port=587,
        username=os.getenv("Comp_EMAIL"),
        password=os.getenv("Comp_EMAIL_PWD"),
        use_tls=True
    )

mcp = FastMCP("Company_HR_assistant")

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
meeting_manager = MeetingManager()
ticket_manager = TicketManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

@mcp.tool()
def add_employee(emp_name : str, manager_id:str, email : str) -> str:
    emp= EmployeeCreate(
        name=emp_name,
        manager_id = manager_id,
        emp_id = employee_manager.get_next_emp_id(),
        email = email
    )

    employee_manager.add_employee(emp)

    return f"New Employee {emp_name} added successfully."

@mcp.tool()
def get_employee_details(name : str) -> Dict[str, str]:

    matches = employee_manager.search_employee_by_name(name)
    emp_id = matches[0]
    if len(matches) == 0:
        raise ValueError(f"Employee {name} not found")
    emp_id = matches[0]
    return employee_manager.get_employee_details(emp_id)

@mcp.tool()
def send_email(subject : str, body : str, to_emails : str) -> str:
    email_sender.send_email(
        subject=subject,
        body=body,
        to_emails=to_emails,
        from_email=email_sender.username
    )
    return f"Email successfully sent to {to_emails}"

@mcp.tool()
def create_ticket(emp_id : str, item : str, reason : str) -> str:
    req = TicketCreate(
        emp_id = emp_id,
        item = item,
        reason = reason
    )

    return ticket_manager.create_ticket(req)

@mcp.tool()
def schedule_meeting(emp_id : str, meeting_dt):
    pass

@mcp.prompt("on_boarding_employee")
def on_boarding_employee(emp_name:str, manager_name:str):
    return f'''
    for adding new employee use these details:
    - The employee name is {emp_name}
    - The manager is {manager_name}
    Then do these steps:
    - Add the employee to the HR management system.
    - Send the wellcome email to the new employee with login conditionals and manager name.
    - Send the email to the manager asking him about the new employee joining.
    - Raise tickets for new laptop and id_card.
    '''

if __name__ == "__main__":
    mcp.run(transport="stdio")