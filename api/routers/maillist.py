from fastapi import APIRouter, Depends, BackgroundTasks
from utils.dependency import get_maillist_services
from services.maillist import MailListService
from schemas.maillist import CreateMailListSchema, MailListSchema, SendMailMessageSchema, UpdateMailListSchema
from repositories.base import Pagination
from database.mail import EmailSender
from utils.permissions import read_mails, read_mail, send_message_emails, update_email, delete_email
router = APIRouter(
    prefix="/mails",
    tags=["Mailing list"]
)


@router.post('/subscribe', name="subscribe to newsletter", response_model=MailListSchema)
async def subscribe_to_newsletter(
    mail_data: CreateMailListSchema,
    maillist_services: MailListService = Depends(get_maillist_services)
):
    return await maillist_services.subscribe(mail_data)


@router.get('', name='get all mails', response_model=list[MailListSchema], dependencies=[Depends(read_mails)])
async def get_all_mails_data(
    pagination: Pagination = Depends(),
    maillist_services: MailListService = Depends(get_maillist_services)
):
    return await maillist_services.get_all_mails(pagination)



@router.get('/{mail_id}', name="get mail by ID", response_model=MailListSchema, dependencies=[Depends(read_mail)])
async def get_mail_data_by_id(
    mail_id: int,
    maillist_services: MailListService = Depends(get_maillist_services)
):
    return await maillist_services.get_mail_by_id(mail_id)



@router.post('/send/all', name="send any message to all subscribed mails", dependencies=[Depends(send_message_emails)])
async def send_message_to_all_subscribed_mails(
    mail_data: SendMailMessageSchema,
    background_tasks: BackgroundTasks,
    email_sender: EmailSender = Depends()
):
    
    background_tasks.add_task(email_sender.send_message_to_all_emails, mail_data)

    return {"message": "sent for all"}


@router.put('/{mail_id}', name="change the email address data", response_model=MailListSchema, dependencies=[Depends(update_email)])
async def update_email_data(
    mail_id: int, 
    email_data: UpdateMailListSchema,
    maillist_services: MailListService = Depends(get_maillist_services)
):
    return await maillist_services.update_email(mail_id, email_data)


@router.delete('/{mail_id}', name="delete mail data", response_model=MailListSchema, dependencies=[Depends(delete_email)])
async def update_mail_data(
    mail_id: int, 
    maillist_services: MailListService = Depends(get_maillist_services)
):
    return await maillist_services.delete_email(mail_id)