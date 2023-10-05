import models
reg_messages = {
    "Путешественник": {
        "ru": """
        Русский путешественник 
    """,
        "en": """
        English Traveler
    """
    }
}
class EmailMessageTemplateHandler:

    async def get_message_by_language(self, language: str):
        ...

    async def get_email_message(
            self,
            language: str,
            user: models.User,
    ):
        if user.role.name["ru"] == "Путешественник":
            email_body = await self.get_message_by_language(language)

        