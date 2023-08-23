from fastapi import HTTPException, status
from models import User


class PermissionChecker:
    def __init__(self, permission_endpoint: str, cur_user = None):
        self.allowed_permission = permission_endpoint
        self.current_user = cur_user

    @staticmethod
    def checker():
        
        if PermissionChecker.allowed_permission not in [rp.permission.endpoint for rp in PermissionChecker.current_user.role.role_permissions]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Insufficient privileges."
            )
        return True
#related to users
register_user = PermissionChecker("register_user")
read_users = PermissionChecker("read_users")
update_user = PermissionChecker("update_user")
delete_user = PermissionChecker("delete_user")


#related to roles
read_roles = PermissionChecker("read_roles")
read_role_permissions = PermissionChecker("read_role_permissions")
create_role = PermissionChecker("create_role")
update_role = PermissionChecker("update_role")
delete_role = PermissionChecker("delete_role")

#related to permissions
read_permissions = PermissionChecker("read_permissions")
create_permission = PermissionChecker("create_permission")
update_permission = PermissionChecker("update_permission")
delete_permission = PermissionChecker("delete_permission")


#related to role permissions
give_role_permission = PermissionChecker("give_role_permission")
delete_role_permission = PermissionChecker("delete_role_permission")


#related to emails
read_mails = PermissionChecker("read_mails")
send_message_emails = PermissionChecker("send_message_emails")
update_email = PermissionChecker("update_email")
delete_email = PermissionChecker("delete_email")

