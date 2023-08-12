from repositories.base import BaseRepository
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema
from sqlalchemy import func


class RolesRepository(BaseRepository):
    
    async def get_permissions_of_role(self, role_id: int):
        role = await self.get_by_id(role_id)
        return [perm.permission for perm in role.role_permissions]

    async def has_already_role_name(self, role_data: CreateRoleSchema) -> bool:
        role_names = self.session.query(self.model).all()
        existing_role_names = [name[0].lower() for name in role_names]  

        return role_data.name.lower() in existing_role_names
        
        

        