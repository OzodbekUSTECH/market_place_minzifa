from models import User
from utils.exceptions import CustomExceptions
from enum import Enum

class Permissions(Enum):
    CONTROL_USERS = "crud_users"
    CONTROL_ROLES_AND_PERMISSIONS = "crud_roles"
    CONTROL_SUBSCRIBED_MAILS = "crud_maillist"

permissions_list = [permission.value.lower() for permission in Permissions]


class PermissionHandler:

    @staticmethod
    async def has_permission(
        required_permission: str,
        current_user: User,
        user_id: int = None
    ) -> bool:
        if user_id != current_user.id and required_permission not in [rp.permission.endpoint for rp in current_user.role.role_permissions]:
            raise CustomExceptions.forbidden("Access denied. Insufficient privileges.")
        return True
    
    # @staticmethod
    # async def is_allowed_permission_endpoint(
    #     endpoint: str
    # ) -> bool:
    #     if endpoint.lower() not in permissions_list:
    #         raise CustomExceptions.not_found("Not allowed endpoint")
    #     return True

    