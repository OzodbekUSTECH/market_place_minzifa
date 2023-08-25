from repositories import BaseRepository
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema




class RolePermissionsRepository(BaseRepository):    
    
    async def delete_permission_for_role(self, role_permission_data: DeleteRolePermissionsSchema) -> RolePermissionsSchema:
        instance = self.session.query(self.model).filter_by(role_id=role_permission_data.role_id, permission_id=role_permission_data.permission_id).first()
        self.session.delete(instance)
        return instance
    
    async def has_role_permission(self, role_data: CreateRolePermissionsSchema) -> bool:
        instance = self.session.query(self.model).filter_by(role_id=role_data.role_id, permission_id=role_data.permission_id).first()
        return instance is not None
        