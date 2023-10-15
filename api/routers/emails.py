from fastapi import APIRouter, Form, UploadFile, File, BackgroundTasks
from schemas.emails import CreateEmailSchema, EmailSchema, SendEmailMessageSchema
from services import emails_service
from schemas import IdResponseSchema
from repositories import Page
from database import UOWDependency

router = APIRouter(prefix="/emails", tags=["Emails (Subscribers)"])


@router.post("/subscribe", response_model=IdResponseSchema)
async def subscribe_email(
    uow: UOWDependency,
    mail_data: CreateEmailSchema,
):
    return await emails_service.create_email(uow, mail_data)


@router.get("", response_model=Page[EmailSchema])
async def get_list_of_emails(
    uow: UOWDependency,
    language: str | None = None
):
    return await emails_service.get_list_of_emails(uow, language)


@router.get("/{id}", response_model=EmailSchema)
async def get_email_by_id(
    uow: UOWDependency,
    id: int
):
    return await emails_service.get_email_by_id(uow, id)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_email(
    uow: UOWDependency,
    id: int,
):
    return await emails_service.delete_email(uow, id)


@router.post("/send/{language}")
async def send_message_to_emails(
    uow: UOWDependency,
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

    background_tasks.add_task(emails_service.send_message_to_emails, uow, message_data)

    return {"message": "Background task started to send all mails"}    
