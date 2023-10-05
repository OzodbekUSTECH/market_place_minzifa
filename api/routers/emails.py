from fastapi import APIRouter, Form, UploadFile, File, BackgroundTasks
from schemas.emails import CreateEmailSchema, EmailSchema, SendEmailMessageSchema
from services import emails_service
from schemas import IdResponseSchema
from repositories import Page

router = APIRouter(prefix="/emails", tags=["Emails (Subscribers)"])


@router.post("/subscribe", response_model=IdResponseSchema)
async def subscribe_email(
    mail_data: CreateEmailSchema,
):
    return await emails_service.create_email(mail_data)


@router.get("", response_model=Page[EmailSchema])
async def get_list_of_emails(language: str | None = None):
    return await emails_service.get_list_of_emails(language)


@router.get("/{id}", response_model=EmailSchema)
async def get_email_by_id(id: int):
    return await emails_service.get_email_by_id(id)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_email(
    id: int,
):
    return await emails_service.delete_email(id)


@router.post("/send/{language}")
async def send_message_to_emails(
    background_tasks: BackgroundTasks,
    language: str,
    subject: str = Form(),
    body: str = Form(),
    attachments: list[UploadFile] = File(None), 
):
    message_data = SendEmailMessageSchema(
        language=language,
        subject=subject,
        body=body,
        attachments=attachments
    )

    background_tasks.add_task(emails_service.send_message_to_emails, message_data)

    return {"message": "Background task started to send all mails"}    
