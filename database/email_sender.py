from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from schemas.emails import SendEmailMessageSchema
import models
from config import settings
from fastapi import UploadFile
from utils.locale_handler import LocaleHandler
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

from jinja2 import Environment, FileSystemLoader


class EmailSender:
    def __init__(
        self,
    ):
        self.fm = FastMail(conf)

    async def _render_html_template(
        self,
        user: models.User,
        locale: str,
        template_name: str,
        **kwargs
    ):
        env = Environment(
            loader=FileSystemLoader("templates")
        )  # Замените "templates" на путь к вашему каталогу с шаблонами
        template = env.get_template(template_name)
        html_content = template.render(user=user, locale=locale, **kwargs)
        return html_content

    async def _send_message(
        self,
        emails: list | str,
        subject: str,
        body: str,
        attachments: list[UploadFile] = [],
    ) -> None:
        message = MessageSchema(
            subject=subject,
            recipients=[emails] if isinstance(emails, str) else emails,
            body=body,
            attachments=attachments,
            subtype=MessageType.html,
        )

        await self.fm.send_message(message)

    async def send_welcome_email_message(
        self,
        user: models.User,
        locale: str,
        subject: str,
        template_name: str,
        **kwargs
    ) -> None:
        html_content = await self._render_html_template(user, locale, template_name, **kwargs)
        await self._send_message(emails=user.email, subject=subject, body=html_content)

    async def send_reset_password_link(
        self, locale: str, email: str, token: str
    ) -> None:
        reset_link = f"{settings.RESET_LINK}{token}"

        body = f"<p>Click the link below to reset your password:</p><p><a href='{reset_link}'>{reset_link}</a></p>"
        subject = (
            "Восстановление пароля на MINZIFATRAVEL MARKET PLACE"
            if locale == "ru"
            else "Reset Password MARKET PLACE MINZIFATRAVEL"
        )
        await self._send_message(
            emails=email,
            subject=subject,
            body=body,
        )

    async def send_message_to_emails(
        self, emails: list, message_data: SendEmailMessageSchema
    ) -> None:
        await self._send_message(
            emails=emails,
            subject=message_data.subject,
            body=message_data.body,
            attachments=message_data.attachments,
        )

    # async def send_message_to_all_emails(self, mail_data: SendMailMessageSchema):
    #     emails = await self.maillist_service.get_emails_without_pagination()
    #     all_emails = []
    #     for email in emails:
    #         all_emails.append(email.email)

    #     message = MessageSchema(
    #         subject = mail_data.subject,
    #         recipients=all_emails,
    #         body = mail_data.body,
    #         subtype=MessageType.html
    #     )
    #     await self.fm.send_message(message)


email_sender = EmailSender()
